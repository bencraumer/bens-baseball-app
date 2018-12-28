from baseball_site.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
]

STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'assets'),
 )
