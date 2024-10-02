<<<<<<< HEAD

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
=======
from pathlib import Path
import os

>>>>>>> parte2/main
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/pdfs/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'pdfs')
<<<<<<< HEAD
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!)fu#80qj4$%vv!dcoy(rdob9yo*(+k)q_67=bc+r@hg@5)o^p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

=======

SECRET_KEY = 'django-insecure-!)fu#80qj4$%vv!dcoy(rdob9yo*(+k)q_67=bc+r@hg@5)o^p'
DEBUG = True
ALLOWED_HOSTS = []

>>>>>>> parte2/main
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_project',
<<<<<<< HEAD

    
    'rest_framework',
    'corsheaders',
    'api', 
    'rest_framework.authtoken',  # Autenticação via token

=======
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'drf_yasg',
>>>>>>> parte2/main
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
<<<<<<< HEAD
    'corsheaders.middleware.CorsMiddleware',
]

=======
]


>>>>>>> parte2/main
ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

<<<<<<< HEAD


WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': str(BASE_DIR / 'db.sqlite3'),
        'NAME': 'djangoprojeto',
        'USER': 'artigos',
        'PASSWORD': 'django',
=======
WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangoprojeto',
        'USER': 'artigos',
        'PASSWORD': 'sistemas',
>>>>>>> parte2/main
        'HOST': 'localhost',
        'PORT': '',
    }
}

<<<<<<< HEAD

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

=======
>>>>>>> parte2/main
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

<<<<<<< HEAD

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_ORIGINS = [
    'http://localhost:8080',
]


=======
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.template': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
>>>>>>> parte2/main
