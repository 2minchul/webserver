from .base import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["pybo.embition.ai"]
CSRF_TRUSTED_ORIGINS = ["http://pybo.embition.ai", "https://pybo.embition.ai"]
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
