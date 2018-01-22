# run commented code if you want to test id your application is live
#def application(environ, start_response):
#    start_response('200 OK', [('Content-type', 'text/plain')])
#    return ["Problem Solver Central"]
import sys
import os

cwd = os.getcwd()
env_dir = os.path.join(cwd, 'venv')
project_dir = os.path.join(cwd, 'API_Project')

INTERP = os.path.join(env_dir, 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.insert(0, os.path.join(env_dir, 'bin'))
sys.path.insert(0, os.path.join(env_dir, 'lib', 'python2.7', 'site-packages'))
sys.path.insert(0, os.path.join(env_dir, 'lib', 'python2.7', 'site-packages', 'django'))

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'API_Project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
