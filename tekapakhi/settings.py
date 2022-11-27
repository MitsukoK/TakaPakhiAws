from pathlib import Path
import os, subprocess
import django_on_heroku
import environ
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)


# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
# SECRET_KEY = "django-insecure-8c1%w48pbtbb($fz^c+a16_ds$v-1ud@zl63cfn-qd((=pkl)m"
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ because of casting above
DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["tiyapakhi2.herokuapp.com", "127.0.0.1"]
# ALLOWED_HOSTS = env('ALLOWED_HOST')


# Application definition

INSTALLED_APPS = [
    #! django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #! flowbite compressor (for static files)
    "compressor",
    #! rest framework
    "rest_framework",
    "rest_framework.authtoken",
    #! my apps
    "banking",
    "landing",
    "userapp",
    "extras",
    "useraccount",
    "user_request",
    #! third party apps
    "phonenumber_field",
    "multiselectfield",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "tekapakhi.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # new
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "tekapakhi.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600, default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    #     # 'ENGINE': 'django.db.backends.mysql',
    #     # 'NAME':'romjan_db',
    #     # 'USER':'romjan',
    #     # 'PASSWORD':'fuck you',
    #     # 'HOST':'localhost',
    #     # 'PORT':'3306',
    # }
}

# DATABASES = {}
# DATABASES['default'] = dj_database_url.config(conn_max_age=600)
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CSRF_TRUSTED_ORIGINS = ["https://tiyapakhi2.herokuapp.com"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}


django_on_heroku.settings(locals())
options = DATABASES["default"].get("OPTIONS", {})
options.pop("sslmode", None)

AUTH_USER_MODEL = "userapp.NewUser"
# AUTH_USER_MODEL = "customauth.MyUser"

COMPRESS_ROOT = BASE_DIR / "static"
COMPRESS_ENABLED = True
STATICFILES_FINDERS = ("compressor.finders.CompressorFinder",)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_DIRS = [
    BASE_DIR / "static",
    # '/var/www/static/',
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
# try:
#     from .local_settings import *
# except ImportError:
#     pass
