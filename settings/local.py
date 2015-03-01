from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

INSTALLED_APPS += ('django_extensions', 'debug_toolbar',)

INTERNAL_IPS = ("127.0.0.1",)

MIDDLEWARE_CLASSES += \
("debug_toolbar.middleware.DebugToolbarMiddleware", )
