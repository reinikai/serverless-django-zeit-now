from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ('*',)

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

INTERNAL_IPS = ('127.0.0.1',)


# Email settings for Mailhog.
# These need to match the settings in docker-compose.yml.
#
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
