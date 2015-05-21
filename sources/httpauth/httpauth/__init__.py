from mediagoblin.meddleware import ENABLED_MEDDLEWARE
from mediagoblin.tools import pluginapi
from mediagoblin.tools.response import redirect

CONFIG = {
    'header': 'REMOTE_USER',
    'header_email': 'HTTP_EMAIL',
    'admin': '',
    'logout_response': None,
}


def setup_plugin():
    global CONFIG
    CONFIG.update(pluginapi.get_config('httpauth'))
    ENABLED_MEDDLEWARE.append('httpauth.meddleware:HttpAuthMeddleware')

def logout_response(request):
    if not CONFIG['logout_redirect']:
        return
    return redirect(request, location=CONFIG['logout_redirect'])

def auth():
    return True


hooks = {
    'setup': setup_plugin,
    'authentication': auth,
    'auth_logout_response': logout_response,
    }
