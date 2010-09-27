# -*- coding: utf-8 -*-
# Django settings for djangocmstest project.

from os.path import abspath, dirname, join

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = abspath(dirname(__file__)) 

ADMINS = (
    ('Manuel Schmidt', 'ms@creative-cubes.de'),
    ('Christian Schweinhardt', 'cs@creative-cubes.de'),
)

MANAGERS = ADMINS

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heicmo',
        'USER': 'root', 
        'PASSWORD': 'hjk90ma',
        'HOST': '80.246.57.155',
        'PORT': '3306',
    }
        
    
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': join(PROJECT_ROOT, 'db.sqlite'),
#        'USER': '', 
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
    
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de-de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = join(PROJECT_ROOT, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3*)7zkh9-quwb$ubq$ipdu&!8t#it#pw%(nwzrpj#%d(45#a3q'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'cms.middleware.media.PlaceholderMediaMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'hcmo.urls'

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

    # base django-cms

    'cms',
    'menus',
    'publisher',
    'mptt',
    # django-cms plugins
    'cms.plugins.text',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.picture',
    'cms.plugins.video',
    
    
    # zinnia and deps
    #'tagging',
    
    # Other
    'lib',
    'sorl.thumbnail',
    'imggal',
    'news',
    'cmsplugin_contact',
)

#------------------------------------------------------------------------
# django cms settings 
# 

CMS_LANGUAGES = (
    ('de', 'Deutsch'),
)

CMS_TEMPLATES = (
    ('cms/pages/default.html', 'Default'),
    ('cms/pages/home.html', 'Home'),
    ('cms/pages/showroom.html', 'Showroom'),
    ('cms/pages/impressum.html', 'Impressum'),
)

CMS_MODERATOR = False
CMS_SEO_FIELDS = True
CMS_REDIRECTS = True

THUMBNAIL_EXTENSION = 'png'
THUMBNAIL_DEBUG = True
