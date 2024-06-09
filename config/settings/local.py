from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ls&1oied3t*np!^y6664m!j2-l%ie=8g$w-bjk_pjryzd#3y6b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
