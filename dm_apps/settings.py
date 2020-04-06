"""
Django settings for dm_apps project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

import requests
from django.utils.translation import gettext_lazy as _
from decouple import config, UndefinedValueError
from msrestazure.azure_active_directory import MSIAuthentication
from . import utils

# Custom variables

WEB_APP_NAME = "DMApps"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# some simple settings that we import from the .env file or the environmental variables
####################################################
# Django security keye
SECRET_KEY = config('SECRET_KEY', cast=str, default="fdsgfsdf3erdewf232343242fw#ERD$#F#$F$#DD")
# should debug mode be turned on or off? default = False
DEBUG = config("DEBUG", cast=bool, default=False)
# this is used in email templates to link the recipient back to the site
SITE_FULL_URL = config("SITE_FULL_URL", cast=str, default="http://dmapps")
# the default 'from' email address used for system emails
SITE_FROM_EMAIL = config("SITE_FROM_EMAIL", cast=str, default="DoNotReply.DMApps@Azure.Cloud.dfo-mpo.gc.ca")
# google maps API key
GOOGLE_API_KEY = config("GOOGLE_API_KEY", cast=str, default="")
# github api key
GITHUB_API_KEY = config("GITHUB_API_KEY", cast=str, default="")
# Should the ticketing app be displayed on the main index page?
SHOW_TICKETING_APP = config("SHOW_TICKETING_APP", cast=bool, default=True)
# Should the ticketing app be displayed on the main index page?
DEVOPS_BUILD_NUMBER = config("DEVOPS_BUILD_NUMBER", cast=str, default="")

# Slightly more complicated settings
####################################
#
# Azure AD
azure_connection_dict = utils.get_azure_connection_dict()
if utils.azure_ad_values_exist(azure_connection_dict):
    # check to see if a manual override is provided in env
    AZURE_AD = config("AZURE_AD", cast=bool, default=True)
    # if AZURE_AD is set to false, it is because of a manual override
    if not AZURE_AD:
        print("Azure Active Directory oauth credentials available but settings present to manually overriding usage")
    else:
        print("Azure Active Directory oauth credentials provided. User authentication will be handled by AAD.")
else:
    # there is not a complete set of connection values in the env
    AZURE_AD = False

#
# Email settings
SENDGRID_API_KEY = config('SENDGRID_API_KEY', cast=str, default="")
EMAIL_HOST = config('EMAIL_HOST', cast=str, default="")
EMAIL_HOST_USER = config('EMAIL_HOST_USER', cast=str, default="")
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', cast=str, default="")
EMAIL_PORT = config('EMAIL_PORT', cast=str, default="")
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=str, default="")

# first check to see if a sendgrid api key is available
if SENDGRID_API_KEY == "":
    USE_SENDGRID = False
    # if there is nothing there, let's check for SMTP EMAIL configuration
    if EMAIL_HOST == "":
        print("No email service credentials found in system config.")
        USE_SMTP_EMAIL = False
    else:
        USE_SMTP_EMAIL = True
else:
    USE_SENDGRID = True

#
# Allowed Hosts
# the user can provide a one-off host to allow (i.e., if they do not wish to add it to the settings file)
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'dmapps',
    'dmapps.ent.dfo-mpo.ca',
    'dmapps-dev.azurewebsites.net',
    'dmapps-test-web.azurewebsites.net',
    'dmapps-prod-web.azurewebsites.net',
    'dmapps-prod-web-staging.azurewebsites.net',
]
ALLOWED_HOST_TO_ADD = config("ALLOWED_HOST_TO_ADD", cast=str, default="")
if ALLOWED_HOST_TO_ADD != "":
    ALLOWED_HOSTS.append(ALLOWED_HOST_TO_ADD)
    print("The following hostname is being added to the ALLOWED_HOSTS variable", ALLOWED_HOST_TO_ADD)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

#################################################
# APPS -- will look to local configuration file #
#################################################
# check to see if there is a user-defined local configuration file
# if there is, we use this as our local configuration, otherwise we use the default
try:
    from . import my_conf as local_conf
except ModuleNotFoundError and ImportError:
    from . import default_conf as local_conf

# Application definition
INSTALLED_APPS = [
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.gis',
                     'storages',
                     'django.contrib.humanize',
                     'bootstrap4',
                     'el_pagination',
                     'easy_pdf',
                     'tracking',
                     'accounts',
                     'lib',
                     'shared_models',
                     'tickets',
                 ] + local_conf.MY_INSTALLED_APPS


# If the GEODJANGO setting is set to False, turn off any apps that require it
GEODJANGO = config("GEODJANGO", cast=bool, default=False)
if not GEODJANGO:
    INSTALLED_APPS.remove('django.contrib.gis')
    try:
        INSTALLED_APPS.remove('spring_cleanup')
        print("turning off spring cleanup app because geodjango is not enabled")
    except ValueError:
        pass


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dm_apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dm_apps.context_processor.my_envr'
            ],
        },
    },
]

WSGI_APPLICATION = 'dm_apps.wsgi.application'

######################################################
# DATABASES -- will look to local configuration file #
######################################################
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# DATABASE_ROUTERS = ['dm_apps.routers.WhaleDatabaseRouter', ]
DATABASES = local_conf.DATABASES

# This variable will describe the type of database we are connecting to (e.g PROD, DEV, TEST...)
try:
    DB_MODE = local_conf.DB_MODE
    DB_HOST = local_conf.DB_HOST
    DB_NAME = local_conf.DB_NAME
    USE_LOCAL_DB = local_conf.USE_LOCAL_DB
except AttributeError:
    DB_MODE = "n/a"
    DB_HOST = "n/a"
    DB_NAME = "n/a"
    USE_LOCAL_DB = True

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Halifax'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AZURE_STORAGE_ACCOUNT_NAME = config("AZURE_STORAGE_ACCOUNT_NAME", cast=str, default="")
AZURE_STORAGE_ACCESS_KEY = config("AZURE_STORAGE_ACCESS_KEY", cast=str, default="")
# if no account name was provided, serve static and media files with whitenoise
if AZURE_STORAGE_ACCOUNT_NAME == "" or AZURE_STORAGE_ACCESS_KEY == "":
    print('Serving static and media files from local staticfiles directory using Whitenoise.')
    MEDIA_ROOT = MEDIA_DIR
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
else:
    # serve from azure
    print('Azure storage blob connection information found. Serving static and mediafile from azure storage blob.')
    DEFAULT_FILE_STORAGE = 'backend.custom_azure.AzureMediaStorage'
    STATICFILES_STORAGE = 'backend.custom_azure.AzureStaticStorage'
    STATIC_CONTAINER_NAME = "static"
    MEDIA_CONTAINER_NAME = "media"
    AZURE_CUSTOM_DOMAIN = f'{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net'
    STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_CONTAINER_NAME}/'
    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_CONTAINER_NAME}/'

# This setting should allow for submitting forms with lots of fields. This is especially relevent when using formsets as in ihub > settings > orgs...
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# Setting for django-tracking2
TRACK_PAGEVIEWS = True
TRACK_QUERY_STRING = True
TRACK_REFERER = True
TRACK_SUPERUSERS = False

if "win" in sys.platform.lower() and GEODJANGO:
    GDAL_LIBRARY_PATH = config("GDAL_LIBRARY_PATH", cast=str, default="")
