import os

from config.settings.base import *  # NOQA

DEBUG = True

CURRENT_ENV = "DEV"

DATABASES = {
    "default_sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "default_postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Vasylenko",
        "HOST": "localhost",
        "USER": "postgres",
        "PASSWORD": "admin",
        "PORT": "5432",
    },
}
