from pathlib import Path
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

import dj_database_url
import os
import sys

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True") == "True"

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "True") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# Application definition

INSTALLED_APPS = [
    "modeltranslation",
    "unfold",
    "unfold.contrib.import_export",
    "unfold.contrib.filters", 
    "unfold.contrib.forms", 
    "unfold.contrib.inlines",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'distro.apps.panel',
    'distro.apps.users',
    'distro.apps.analytics',
    'distro.apps.artists',
    'distro.apps.albums',
    'distro.apps.dashboard',
    'distro.apps.labels',
    'distro.apps.notifications',
    'distro.apps.participants',
    'distro.apps.releases',
    'distro.apps.partners',
    'distro.apps.reviews',
    'distro.apps.royalties',
    'distro.apps.landing',
    'distro.apps.contact',
    'distro.apps.platforms',
    'distro.apps.genres',
    'distro.apps.tracks',
    'distro.apps.links',
    'distro.apps.lyrics',
    'distro.apps.demo',   
    'import_export',
    'guardian',
    'django_countries',
    'storages',
    'sendgrid',
    'tailwind',
    'django_extensions'
]

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'distro.apps.demo.middleware.ReadonlyExceptionHandlerMiddleware',
    'distro.apps.demo.middleware.ServiceMiddleware',
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
)

# SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

ROOT_URLCONF = 'distro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'distro.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if DEVELOPMENT_MODE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL") is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

USE_SPACES = os.getenv('USE_SPACES') == 'True'

if USE_SPACES:
    # settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = 'https://fra1.digitaloceanspaces.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UNFOLD = {
    "SITE_TITLE": "Brave Distro",
    "SITE_HEADER": "Brave Distro",
    "SITE_URL": "/",
    "SITE_SYMBOL": "music_note",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    # "THEME": "dark",
    "ENVIRONMENT": "distro.apps.demo.utils.environment_callback",
    "DASHBOARD_CALLBACK": "distro.apps.dashboard.views.dashboard_callback",
    "STYLES": [
        lambda request: static("css/admin.css"),
    ],
    "COLORS": {
        "primary": {
            "50": "198 242 34",
            "100": "187 228 32",
            "200": "176 215 30",
            "300": "165 201 28",
            "400": "154 188 26",
            "500": "143 174 24",
            "600": "132 160 22",
            "700": "121 147 20",
            "800": "110 133 18",
            "900": "99 120 16",
            "950": "88 106 14"
        }
    },

    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
             {
                "separator": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
             {
                "separator": True,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    # {
                    #     "title": _("_Analytics"),
                    #     "icon": "analytics",
                    #     "link": "#"#reverse_lazy("admin:albums_album_changelist"),
                    # },
                    {
                        "title": _("Notifications"),
                        "icon": "notifications",
                        "link": reverse_lazy("admin:notifications_notification_changelist")
                    },
                ],
            },
            {
                "title": _("Catalog"),
                "separator": True,
                "items": [
                    {
                        "title": _("Labels"),
                        "icon": "store",
                        "link": reverse_lazy("admin:labels_label_changelist")
                    },
                    {
                        "title": _("Artists"),
                        "icon": "artist",
                        "link": reverse_lazy("admin:artists_artist_changelist"),
                    },
                    {
                        "title": _("Participants"),
                        "icon": "group",
                        "link": reverse_lazy("admin:participants_participant_changelist"),
                    },
                    {
                        "title": _("Tracks"),
                        "icon": "audio_file",
                        "link": reverse_lazy("admin:tracks_track_changelist"),
                    },
                    {
                        "title": _("Lyrics"),
                        "icon": "lyrics",
                        "link": reverse_lazy("admin:lyrics_lyrics_changelist"),
                    },
                    {
                        "title": _("Albums"),
                        "icon": "album",
                        "link": reverse_lazy("admin:albums_album_changelist"),
                    },
                ],
            },
            {
                "title": _("Releases"),
                "separator": True,
                "items": [
                    {
                        "title": _("Releases"),
                        "icon": "new_releases",
                        "link": reverse_lazy("admin:releases_release_changelist"),
                    },
                     {
                        "title": _("Reviews"),
                        "icon": "reviews",
                         "link": reverse_lazy("admin:releases_releasereview_changelist"),
                    },
                    {
                        "title": _("History"),
                        "icon": "cycle",
                        "link": reverse_lazy("admin:releases_releasehistory_changelist"),
                    }
                ],
            },
            {
                "title": _("Royalties"),
                "separator": True,
                "items": [
                    {
                        "title": _("Royalties (n/a)"),
                        "icon": "attach_money",
                        "link": "#",
                    },
                    {
                        "title": _("Payments (n/a)"),
                        "icon": "payments",
                        "link": "#",
                    },
                ],
            },
            {
                "title": _("Configuration"),
                "separator": True,
                "items": [
                    {
                        "title": _("Partners"),
                        "icon": "handshake",
                        "link": reverse_lazy("admin:partners_partner_changelist"),
                    },
                    {
                        "title": _("Participants Role"),
                        "icon": "group",
                        "link": reverse_lazy("admin:participants_participantrole_changelist"),
                    },
                    {
                        "title": _("Platforms"),
                        "icon": "integration_instructions",
                        "link": reverse_lazy("admin:platforms_platform_changelist"),
                    },
                    {
                        "title": _("Genres"),
                        "icon": "group",
                        "link": reverse_lazy("admin:genres_genre_changelist"),
                    },
                    {
                        "title": _("Links"),
                        "icon": "link",
                        "link": reverse_lazy("admin:links_link_changelist"),
                    },
                ],
            },
        ],
    },
}

# Email settings
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "your_sendgrid_api_key")

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_ECHO_TO_STDOUT = False
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "office@bravelab.io")
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LOGIN_URL = "admin:login"

LOGIN_REDIRECT_URL = reverse_lazy("admin:index")

LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "admin")

LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "admin")
