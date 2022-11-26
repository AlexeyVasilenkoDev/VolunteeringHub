from config.settings.base import *  # NOQA

DEBUG = False

CURRENT_ENV = "PROD"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

ALLOWED_HOSTS = ["localhost", "ec2-54-224-225-111.compute-1.amazonaws.com"]
