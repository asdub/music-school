from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: define the correct hosts in production! TESTING
ALLOWED_HOSTS = ['newparkmusic.ie'] 


try:
    from .local import *
except ImportError:
    pass
