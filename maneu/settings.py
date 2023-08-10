"""
Django settings for maneu project.

Generated by 'django-maneu startproject' using Django 3.0.

For more information on this file, see
https:#docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https:#docs.djangoproject.com/en/3.0/ref/settings/
"""
import os

"""
Build paths inside the project like this: os.path.join(BASE_DIR, ...)
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


"""
secret config
Quick-start development settings - unsuitable for production
See https:#docs.djangoproject.com/en/3.0/howto/deployment/checklist/
SECURITY WARNING: don't run with debug turned on in production!
SECURITY WARNING: keep the secret key used in production secret!
"""
DEBUG = True
SECRET_KEY = 'd&@vq_f^z79&w=nqqcm2vu#+gj8)_qdvy1t&agfxhmi74fwpr!'
ALLOWED_HOSTS = ['*']


"""
注册应用程序
"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'maneu',
    'maneu_admin',
    'maneu_guest',
    'maneu_index',
    'maneu_order',
    'maneu_service',
]


"""
注册中间件
"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.UserMiddleware.UserMiddleware',  # 用户登录校验中间件
]


"""
根路由
"""
ROOT_URLCONF = 'maneu.urls'


"""
注册模板
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates"],
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


"""
WSGI_应用程序
"""
WSGI_APPLICATION = 'maneu.wsgi.application'


"""
配置数据库
https:#docs.djangoproject.com/en/3.0/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'maneu',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '',
    }
}


"""
密码验证
Password validation
https:#docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
"""
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


"""
国际化配置
Internationalization
https:#docs.djangoproject.com/en/3.0/topics/i18n/
"""
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False


"""
Static files config
https:#docs.djangoproject.com/en/3.0/howto/static-files/
"""
STATIC_URL = '/static/'
STATIC_ROOT = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


"""
session config
"""
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Session的cookie保存在浏览器上时的key，即：session_id＝随机字符串（默认）
SESSION_COOKIE_NAME = "sessionid"
# Session的cookie保存的路径（默认）
SESSION_COOKIE_PATH = "/"
# Session的cookie保存的域名（默认）
SESSION_COOKIE_DOMAIN = None
# 是否Https传输cookie（默认）
SESSION_COOKIE_SECURE = False
# 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_HTTPONLY = True
# Session的cookie失效日期（2周）（默认）
SESSION_COOKIE_AGE = 3600
# 是否关闭浏览器使得Session过期（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# 是否每次请求都保存Session，默认修改之后才保存（默认）
SESSION_SAVE_EVERY_REQUEST = True
