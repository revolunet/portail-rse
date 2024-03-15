"""
Django settings for Portail RSE project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "0.0.0.0,127.0.0.1").split(",")

# Application definition
INSTALLED_APPS = [
    "api",
    "entreprises",
    "habilitations",
    "metabase",
    "public",
    "reglementations",
    "users",
    "utils",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django_vite",
    "anymail",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "impact.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "entreprises.context_processors.current_entreprise",
            ],
        },
    },
]
WSGI_APPLICATION = "impact.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
METABASE = os.getenv("METABASE_DATABASE_URL")
METABASE_DATABASE_NAME = "metabase"

DATABASES = {
    "default": dj_database_url.config("DATABASE_URL"),
    METABASE_DATABASE_NAME: dj_database_url.config(
        "METABASE_DATABASE_URL" if METABASE else "DATABASE_URL"
    ),
}

DATABASE_ROUTERS = ["impact.db_routers.MetabaseRouter"]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 12,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "impact.password_validation.CompositionPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "fr-FR"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Django-vite configuration for static files build with vite
# https://github.com/MrBin99/django-vite
DJANGO_VITE_ASSETS_PATH = Path(BASE_DIR, "static", "svelte")
DJANGO_VITE_DEV_MODE = DEBUG
DJANGO_VITE_MANIFEST_PATH = Path(DJANGO_VITE_ASSETS_PATH, "manifest.json")
DJANGO_VITE_DEV_SERVER_PORT = 5173
DJANGO_VITE_STATIC_URL_PREFIX = "svelte"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = Path(BASE_DIR, "static_collected")
STATIC_URL = "/static/"
STATICFILES_DIRS = (Path(BASE_DIR, "static"),)

# Compression and caching whitenoise configuration to serve static files
# https://whitenoise.readthedocs.io/en/stable/django.html
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email
SENDINBLUE_API_KEY = os.getenv("SENDINBLUE_API_KEY")
EMAIL_BACKEND = (
    "anymail.backends.sendinblue.EmailBackend"
    if SENDINBLUE_API_KEY
    else "django.core.mail.backends.console.EmailBackend"
)
ANYMAIL = {"SENDINBLUE_API_KEY": SENDINBLUE_API_KEY}
DEFAULT_FROM_EMAIL = "ne-pas-repondre@portail-rse.beta.gouv.fr"
CONTACT_EMAIL = os.getenv("CONTACT_EMAIL")
SENDINBLUE_CONFIRM_EMAIL_TEMPLATE = 1

# Users
AUTH_USER_MODEL = "users.User"
LOGIN_URL = "/connexion"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Sentry
SENTRY_DSN = os.getenv("SENTRY_DSN")

if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        environment=os.getenv("SENTRY_ENV", "production"),
    )
