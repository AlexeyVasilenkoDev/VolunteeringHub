from config.settings.base import *  # NOQA

DEBUG = True

CURRENT_ENV = "DEV"

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
