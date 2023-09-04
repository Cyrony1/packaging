from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*7!^g_l08+lqt*!nael!gadyjd1v+kj86$u=mggib($2ksuz#s'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
