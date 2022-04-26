"""
Django settings for app_main project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import logging
from datetime import timedelta
from pathlib import Path
import pymysql
from peewee import *

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p2sztu3d8)%)552^lthu(+-:(%+nededa2a-*^hwb8y0^b*arm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'True'

ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'app_common.User'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # 放在新建应用之前
    'rest_framework',
    'drf_yasg',
    'django_filters',
    'django_q',
    'rest_framework_simplejwt',
    'app_common',
    'app_files'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 注意顺序，放在此处
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.jwt_user.JWTAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.current_user.CurrentUserMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True  # 允许所有的请求，或者设置
CORS_ALLOW_HEADERS = ('*')  # 允许所有的请求头
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie，前端需要携带cookies访问

ROOT_URLCONF = 'app_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'utils.renderer.JSONResponseRenderer',
        'drf_excel.renderers.XLSXRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'EXCEPTION_HANDLER': 'utils.exception_handler.antd_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.StandardResultsSetPagination',
}

# JWT 认证配置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1200),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=2400),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        },
        'jwt': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'LOGIN_URL': '/api-auth/login/',
    'LOGOUT_URL': '/api-auth/logout/',
}

REDOC_SETTINGS = {
    'LOGIN_URL': '/api-auth/login/',
    'LOGOUT_URL': '/api-auth/logout/',
}

WSGI_APPLICATION = 'app_main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# 139.224.192.64
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mfs',  # 数据库名
        'USER': 'root',  # 用户名
        'PASSWORD': 'nihao@123',  # 密码
        'HOST': '139.224.192.64',
        'PORT': '3310',
    }
}

SUPER_X = {
    "host": '139.224.192.64',
    "port": 3310,
    "user": 'root',
    "password": 'nihao@123',
    "cursorclass": pymysql.cursors.DictCursor,
    "database": 'mfs',
}

FMS = {
    'database': 'mfs',
    'charset': 'utf8',
    'sql_mode': 'PIPES_AS_CONCAT',
    'use_unicode': True,
    'host': '139.224.192.64',
    'port': 3310,
    'user': 'root',
    'password': 'nihao@123'
}
database = MySQLDatabase(read_timeout=3600,
                         init_command='SET LOCAL wait_timeout = 3600',
                         write_timeout=3600, **FMS)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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

# Logging Config
LOGGING = {
    'version': 1,  # the dictConfig format version
    'disable_existing_loggers': False,  # retain the default loggers
    'formatters': {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            'format': '%(name)s %(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'verbose': {
            'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'level_debug_filter': {
            '()': 'utils.logging_utils.LevelEqFilter',
            'level': logging.DEBUG,
        },
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true', 'level_debug_filter'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true', ],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'production': {
            'level': 'INFO',
            'filters': ['require_debug_false', ],
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        }
    },
    # 'loggers': {
    #     'app_exporter.views': {
    #         'handlers': ['debug'],
    #         'level': 'DEBUG',
    #     },
    # },
    'root': {
        'handlers': ['debug', 'console', 'production'],
        'level': 'DEBUG',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# 用户上传文件
MEDIA_URL = '/api/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# APP settings
# app_exporter
RESULT_FILE_ROOT = BASE_DIR / 'result_file'
