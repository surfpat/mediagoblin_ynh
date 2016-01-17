# GNU MediaGoblin -- federated, autonomous media hosting
# - YunoHost SSO Authentication plugin
# Copyright (C) 2015-2016 Jerome Lebleu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import six
import logging

from mediagoblin.auth.tools import get_default_privileges, check_auth_enabled
from mediagoblin.db.models import User, Privilege
from mediagoblin.meddleware import BaseMeddleware
from mediagoblin.tools.request import setup_user_in_request

from ynhauth import CONFIG

_log = logging.getLogger(__name__)


class YnhAuthMeddleware(BaseMeddleware):

    def process_request(self, request, controller):
        """Log the user in if the HTTP Authentication header is found."""
        _log.debug('Trying to authorize the user via YunoHost SSO Auth')

        username = six.text_type(
            request.headers.get(CONFIG['header'], '')
        )
        if not username:
            # log current user out if auth is disabled
            if not check_auth_enabled() and (
                    request.user or 'user_id' in request.session):
                _log.debug('Cleaning invalid user session')
                request.session.delete()
                request.user = None
            return

        # check the current user session
        if request.user:
            if request.user.username != username:
                request.session.delete()
                request.user = None
            else:
                return

        # create the user as needed
        user = User.query.filter(User.username==username).first()
        if not user:
            _log.debug('Creating new user {0}'.format(username))

            user = User()
            user.username = username
            if CONFIG['header_email']:
                user.email = six.text_type(
                    request.headers.get(CONFIG['header_email'], '')
                )
                _log.debug('Found email address {0}'.format(user.email))

            # give the user the default privileges
            default_privileges = get_default_privileges(user)
            default_privileges.append(
                Privilege.query.filter(
                    Privilege.privilege_name==u'active').one()
            )
            if username == CONFIG['admin']:
                _log.debug('Giving admin privileges to user')
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
