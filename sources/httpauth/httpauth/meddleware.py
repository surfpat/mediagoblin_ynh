import six
import logging

from mediagoblin.auth.tools import get_default_privileges
from mediagoblin.db.models import User, Privilege
from mediagoblin.meddleware import BaseMeddleware
from mediagoblin.tools.request import setup_user_in_request

from httpauth import CONFIG

_log = logging.getLogger(__name__)


class HttpAuthMeddleware(BaseMeddleware):

    def process_request(self, request, controller):
        """Log the user in if the HTTP Authentication header is found."""
        username = six.text_type(
            request.headers.get(CONFIG['header'], '')
        )
        if not username:
            if 'user_id' in request.session:
                request.session.delete()
                request.user = None
            return

        # Check the current user session
        if request.user:
            if request.user.username != username:
                request.session.delete()
                request.user = None
            else:
                return

        user = User.query.filter(User.username==username).first()
        if not user:
            # Create the user
            user = User()
            user.username = username
            if CONFIG['header_email']:
                user.email = six.text_type(
                    request.headers.get(CONFIG['header_email'], '')
                )

            # give the user the default privileges
            default_privileges = get_default_privileges(user)
            default_privileges.append(
                Privilege.query.filter(
                    Privilege.privilege_name==u'active').one()
            )
            if username == CONFIG['admin']:
                _log.info('admin user')
                default_privileges.append(
                    Privilege.query.filter(
                        Privilege.privilege_name==u'admin').one()
                )
            user.all_privileges = default_privileges
            user.save()

        # log the user in
        request.session['user_id'] = six.text_type(user.id)
        request.session.save()
        request.user = user
