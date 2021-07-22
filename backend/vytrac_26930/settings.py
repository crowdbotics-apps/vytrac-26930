import os
import environ
import logging

from django.core.checks import templates

from modules.manifest import get_modules
import datetime

env = environ.Env()
is_deployed = env.str("DATABASE_URL", default=None)
GOOGLE_API_KEY = 'AIzaSyD--your-google-maps-key-SjQBE'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool("DEBUG", default=False)
DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'mystupidsecretkey'
if is_deployed:
    SECRET_KEY = env.str("SECRET_KEY")

# ALLOWED_HOSTS = env.list("HOST", default=["*"])
ALLOWED_HOSTS = ['*', '0.0.0.0', '127.0.0.1']
SITE_ID = 1

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_REDIRECT", default=False)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]
LOCAL_APPS = [
    'home',
    # 'users.apps.UsersConfig',
    "users",
    'timesheets',
    'archive',
    # 'chat',
    'Alerts',
    'calendars',
    'patients',
    'automations',
    'permissions',
    "tasks",
    'Functions.MyAppsConfig.YourAppConfig',
]
THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_auth',
    'rest_auth.registration',
    'bootstrap4',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_extensions',
    'drf_yasg',
    'storages',
    'corsheaders',

    # start fcm_django push notifications
    'fcm_django',
    # end fcm_django push notifications
    'channels',
    'safedelete',
    'rest_framework_simplejwt.token_blacklist',
    'django_celery_beat',
    'django_celery_results',

]
MODULES_APPS = get_modules()

INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS + MODULES_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Functions.TimezoneMiddleware.TimezoneMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'drf_renderer_xlsx.renderers.XLSXRenderer',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # "USER_DETIALS_SERLIZER": 'users.serlizer.UserSerializer',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(weeks=9999),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(weeks=9999),
    # 'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    # 'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}

ROOT_URLCONF = 'vytrac_26930.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['web_build', 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# CORS
CORS_ALLOW_ALL_ORIGINS = True

WSGI_APPLICATION = 'vytrac_26930.wsgi.application'
ASGI_APPLICATION = "vytrac_26930.asgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
is_deployed = False

if is_deployed:
    print('========================== docker mode ==========================')
    DATABASES = {
        'default': env.db()
    }
else:
    print('========================== classic mode ==========================')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'OPTIONS': {
                'timeout': 20,  # in seconds
                # see also
                # https://docs.python.org/3.7/library/sqlite3.html#sqlite3.connect
            },
            'TEST': {
                'NAME': os.path.join(BASE_DIR, "db_test.sqlite3"),
                'OPTIONS': {
                    'timeout': 100,  # in seconds
                    # see also
                    # https://docs.python.org/3.7/library/sqlite3.html#sqlite3.connect
                },
            },

        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'web_build/static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# allauth / users
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_UNIQUE_EMAIL = True
LOGIN_REDIRECT_URL = "users:redirect"

ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"
ACCOUNT_ALLOW_REGISTRATION = env.bool("ACCOUNT_ALLOW_REGISTRATION", True)
SOCIALACCOUNT_ALLOW_REGISTRATION = env.bool("SOCIALACCOUNT_ALLOW_REGISTRATION", True)

REST_AUTH_SERIALIZERS = {
    # Replace password reset serializer to fix 500 error
    "PASSWORD_RESET_SERIALIZER": "home.api.v1.serializers.PasswordSerializer",
}
REST_AUTH_REGISTER_SERIALIZERS = {
    # Use custom serializer that has no username and matches web signup
    "REGISTER_SERIALIZER": "home.api.v1.serializers.SignupSerializer",
}

# Custom user model
AUTH_USER_MODEL = "users.User"

EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'  # TODO env.str("EMAIL_HOST", "smtp.sendgrid.net")
EMAIL_PORT = 587
EMAIL_HOST_USER = 'crowboticstest@gmail.com'  # TODO env.str("SENDGRID_USERNAME", "")
EMAIL_HOST_PASSWORD = 'my@NewPassword'  # TODO env.str("SENDGRID_PASSWORD", "")

# Sendgrid
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# todo -> add this key in .env
SENDGRID_API_KEY = "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"
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

# AWS S3 config
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", "")
AWS_STORAGE_REGION = env.str("AWS_STORAGE_REGION", "")

USE_S3 = (
        AWS_ACCESS_KEY_ID and
        AWS_SECRET_ACCESS_KEY and
        AWS_STORAGE_BUCKET_NAME and
        AWS_STORAGE_REGION
)

if USE_S3:
    AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", "")
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL", "public-read")
    AWS_MEDIA_LOCATION = env.str("AWS_MEDIA_LOCATION", "media")
    AWS_AUTO_CREATE_BUCKET = env.bool("AWS_AUTO_CREATE_BUCKET", True)
    DEFAULT_FILE_STORAGE = env.str(
        "DEFAULT_FILE_STORAGE", "home.storage_backends.MediaStorage"
    )
    MEDIA_URL = '/mediafiles/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# start fcm_django push notifications
FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": env.str("FCM_SERVER_KEY", "")
}
# end fcm_django push notifications


# Swagger settings for api docs
SWAGGER_SETTINGS = {
    "DEFAULT_INFO": f"{ROOT_URLCONF}.api_info",
}

# if DEBUG or not (EMAIL_HOST_USER and EMAIL_HOST_PASSWORD):
# output email to console instead of sending
#     if not DEBUG:
#         logging.warning("You should setup `SENDGRID_USERNAME` and `SENDGRID_PASSWORD` env vars to send emails.")
#     EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
host = os.environ.get('REDIS_URL', 'redis://localhost:6379') if is_deployed else ('0.0.0.0', 6379)
CHANNEL_LAYERS = {
    'default': {
        # "BACKEND": "channels.layers.InMemoryChannelLayer",
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [host],
        },
    },
}

REDIS_URL = [host]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SAFE_DELETE_INTERPRET_UNDELETED_OBJECTS_AS_CREATED = True

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
