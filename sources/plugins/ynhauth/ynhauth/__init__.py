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

import logging

from mediagoblin.meddleware import ENABLED_MEDDLEWARE
from mediagoblin.tools import pluginapi
from mediagoblin.tools.response import redirect

_log = logging.getLogger(__name__)

CONFIG = {
    'header': 'REMOTE_USER',
    'header_email': 'EMAIL',
    'admin': '',
    'logout_redirect': None,
}


def setup_plugin():
    _log.info('Setting up YunoHost SSO Auth...')

    CONFIG.update(pluginapi.get_config('ynhauth'))
    ENABLED_MEDDLEWARE.append('ynhauth.meddleware:YnhAuthMeddleware')

def logout_response(request):
    if not CONFIG['logout_redirect']:
        return
    return redirect(request, location=CONFIG['logout_redirect'])


hooks = {
    'setup': setup_plugin,
    'auth_logout_response': logout_response,
}
