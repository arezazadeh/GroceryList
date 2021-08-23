

from pathlib import Path
import os
from django.urls import get_script_prefix
from django.utils.functional import lazy
from django.shortcuts import resolve_url
from django.conf import settings



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=uan#hv&^14ldwbw3m7=l1i!t)^ssx9guxy+h(k!4@j8(0^4&#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.1.153', '127.0.0.1', 'localhost', 'my-grocery-cart.herokuapp.com', '10.243.0.249']

# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grocery.apps.GroceryConfig',
    'user_account.apps.UserAccountConfig',
    'fontawesomefree',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GroceryList.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

try:
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
    }
except Exception as e:
    pass

WSGI_APPLICATION = 'GroceryList.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd7pv1ucrreqn29',
        'HOST': 'ec2-44-194-112-166.compute-1.amazonaws.com',
        'POST': 5432,
        'USER': 'vowybgcskedxat',
        'PASSWORD': 'dcbdadafbfa7c22cd5db46a46db3a946e2df369946c8100684f68215321c68f9'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


resolve_url = lazy(resolve_url, str)
_PWA_SCRIPT_PREFIX = get_script_prefix()

PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static',
                                               'serviceworker.js'))


PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'GroceryList')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'Grocery List App')
PWA_APP_ROOT_URL = resolve_url(getattr(settings, 'PWA_APP_ROOT_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', '#000')
PWA_APP_BACKGROUND_COLOR = getattr(settings, 'PWA_APP_BACKGROUND_COLOR', '#fff')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_SCOPE = resolve_url(getattr(settings, 'PWA_APP_SCOPE', _PWA_SCRIPT_PREFIX))
PWA_APP_DEBUG_MODE = getattr(settings, 'PWA_APP_DEBUG_MODE', True)
PWA_APP_ORIENTATION = getattr(settings, 'PWA_APP_ORIENTATION', 'any')
PWA_APP_START_URL = resolve_url(getattr(settings, 'PWA_APP_START_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_FETCH_URL = resolve_url(getattr(settings, 'PWA_APP_FETCH_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_STATUS_BAR_COLOR = getattr(settings, 'PWA_APP_STATUS_BAR_COLOR', 'default')

PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS', [
    {
        'src': '/static/img/food3.png',
        'size': '72x72'
    },
    {
        'src': '/static/img/food3.png',
        'size': '96x96'
    },
    {
        'src': '/static/img/food3.png',
        'size': '128x128'
    },
    {
        'src': '/static/img/food3.png',
        'size': '144x144'
    },
    {
        'src': '/static/img/food3.png',
        'size': '152x152'
    },
    {
        'src': '/static/img/food3.png',
        'size': '192x192'
    },
    {
        'src': '/static/img/food3.png',
        'size': '384x384'
    },
    {
        'src': '/static/img/food3.png',
        'size': '512x512'
    }
])
PWA_APP_SPLASH_SCREEN = getattr(settings, 'PWA_APP_SPLASH_SCREEN', [
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/food3.png',
        'media': '(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)'
    }

])

PWA_APP_DIR = getattr(settings, 'PWA_APP_DIR', 'auto')
PWA_APP_LANG = getattr(settings, 'PWA_APP_LANG', 'en-US')