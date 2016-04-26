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

import os
import json
import logging

from mediagoblin.meddleware import ENABLED_MEDDLEWARE
from mediagoblin.tools import pluginapi
from mediagoblin.tools.response import redirect

_log = logging.getLogger(__name__)

ADMIN_USERNAME = None


def setup_plugin():
    _log.info('Setting up YunoHost SSO Auth...')

    config = pluginapi.get_config('ynhauth')
    if 'admin' in config:
        global ADMIN_USERNAME
        ADMIN_USERNAME = config['admin']

    ENABLED_MEDDLEWARE.append('ynhauth.meddleware:YnhAuthMeddleware')


def logout_response(request):
    try:
        with open('/etc/ssowat/conf.json') as f:
            ssowat = json.load(f)
        logout_url = 'https://{0}{1}?action=logout'.format(
            ssowat['portal_domain'], ssowat['portal_path'],
        )
    except (IOError, KeyError):
        return
    else:
        return redirect(request, location=logout_url)


def auth():
    return True


hooks = {
    'setup': setup_plugin,
    'authentication': auth,
    'auth_logout_response': logout_response,
}
