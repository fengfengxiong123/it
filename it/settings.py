"""
Django settings for it project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xz^k@zl*no&gr=j7gr6_v698ugqdux#%#(p$h1-2syib+b564b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'share',
    'mdeditor',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'it.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'it.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import pymysql

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'NAME': 'it_db',
        'USER': 'root',
        'PASSWORD': 'Liangfeng0504@'

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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# 开发阶段放置项目自己的静态文件，不能包含STATIC_ROOT路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dev_static')
]

# 执行collectstatic命令后会将项目中的静态文件（包括STATICFILES_DIRS、自带admin的静态文件）
# 收集到该目录下面来
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# mdeditor文本编辑器配置
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'

MDEDITOR_CONFIGS = {
    'default':{
        'width': '90% ',  # Custom edit box width  宽度，整个页面的百分之多少
        'heigth': 1500,  # Custom edit box height   高度，单位为px
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime"
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # custom edit box toolbar   工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # image upload format type  允许上传的图片 的格式，不在这个里面的格式将不允许被上传
        'image_floder': 'editor',  # image save the folder name   上传图片后存放的目录，BASE_DIR/MEDIA_ROOT/editor
        'theme': 'default',  # edit box theme, dark / default  mdeditor主题，dark/default两种
        'preview_theme': 'default',  # Preview area theme, dark / default  内容显示区主题 dark/default
        'editor_theme': 'default',  # edit area theme, pastel-on-dark / default   文本编辑区主题  pastel-on-dark / default
        'toolbar_autofixed': True,  # Whether the toolbar capitals
        'search_replace': True,  # Whether to open the search for replacement  是否打开搜索替换
        'emoji': True,  # whether to open the expression function  是否允许使用emoji表情
        'tex': True,  # whether to open the tex chart function   是否打开tex图表功能
        'flow_chart': True,  # whether to open the flow chart function   是否打开流程图功能
        'sequence': True  # Whether to open the sequence diagram function   是否打开序列图函数
    }
}
LOGIN_URL = '/users/login/'