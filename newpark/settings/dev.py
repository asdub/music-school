from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w$wjc6mzt-x#@t%5hhxxph8vltkso)42s8n5sss2@dwjhbd$@$'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 


try:
    from .local import *
except ImportError:
    pass
