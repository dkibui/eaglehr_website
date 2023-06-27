from django.contrib.messages import constants as messages
from pathlib import Path
import os
import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["127.0.0.1", "localhost", env("ALLOWED_HOST")]


INSTALLED_APPS = [
    "blogs.apps.BlogsConfig",
    # "news.apps.NewsConfig",
    "jobs.apps.JobsConfig",
    "User.apps.UserConfig",
    "webapp.apps.WebappConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # pip installed apps
    "ckeditor",
    "tailwind",
    "theme",
    "django_browser_reload",
    # All auth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Local middleware
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# MESSAGE_TAGS
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# AUTH_USER_MODEL = 'User.User'

ROOT_URLCONF = "CORE.urls"

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
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "CORE.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Nairobi"
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    BASE_DIR / "theme/static",
]


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

FORMS_LABEL_SUFFIX = ""
ACCOUNT_FORMS_LABEL_SUFFIX = ""


SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {"client_id": "123", "secret": "456", "key": ""}
    }
}

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
LOGIN_REDIRECT_URL = "webapp:index"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar_Basic": [["-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            "/",
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Subscript",
                    "Superscript",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "Blockquote",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink"]},
            # '/',
            {"name": "styles", "items": ["Format"]},
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {
                "name": "insert",
                "items": ["Table", "HorizontalRule", "Smiley", "SpecialChar"],
            },
        ],
        "toolbar": "YourCustomToolbarConfig",  # put selected toolbar config here
        "width": "100%",
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "autolink",
                "autogrow",
                # 'devtools',
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ]
        ),
    }
}
