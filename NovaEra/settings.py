"""
Django settings for NovaEra project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from importlib.resources import Resource
from pathlib import Path
import os
import django_heroku
import psycopg2


from decouple import config

import banda_contratacion

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print ("base dir path", BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('production_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Eiqui a parte de ter o meu host local (127.0.0.1) engado tamén o host de heroku
ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Esto é para implementar os botóns de share no blog
    'django_social_share',
    'widget_tweaks',
    #my apps
    'artigos',
    'banda_contratacion',
    'newsletter',
    #Installing the Amazon Web Service Storage
    'storages',
    #Para implementar o rich text no cuadro do text field dos artículos
    #https://www.geeksforgeeks.org/richtextfield-django-models/
    'ckeditor',
    'entradas',
    #app para renderizar un pdf. Aunque estou vendo e senon inclúes a app eiqui tamén che funciona.
    'render_pdf'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Incluir eiqui o whitenoise para os archivos estáticos unha vez que estos se suban a heroku
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'NovaEra.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'NovaEra/templates'],
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

WSGI_APPLICATION = 'NovaEra.wsgi.application'
############Comproba se furruncha####################
#Esto é para que non me de error a hora de completar os formularios
CSRF_TRUSTED_ORIGINS = ['https://novaera.gal']

#-------------------start---------database local configuration---------------------
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# No caso de que as tablas non se che creen cando fas makemigrations e migrate utiliza este
# comando: python manage.py migrate --run-syncdb
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#-------------------end---------database local configuration---------------------

#------start-------Heroku database configuration------------------
#Estos atributos cóllelos de Heroku: https://data.heroku.com/datastores/6c90a2e4-c751-4984-a3b7-89ac7b9e5692#administration
#Esto é para conectar ca base de datos de heroku e todos os datos da app se garden nesta base de datos que facilita heroku
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('name_heroku_database'),
#         'USER': config('user_heroku_database'),
#         'PASSWORD': config('password_heroku_database'),
#         'HOST': config('host_heroku_database'),
#         'PORT': '5432',
#     }
# }


import dj_database_url

# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)
#Esto é para conectar tamén ca base de datos de Heroku
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
#------end-------Heroku database configuration------------------

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'gl-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

#Este código é para os arquivos estáticos como as imaxes... para cargalas tamén en Heroku
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = "/static/"
#django_heroku.settings(locals())

# Esto é para indicar a ruta onde temos as imaxes, pdf... Esto é válido tanto en local coma en Heroku
STATICFILES_DIRS=[
    BASE_DIR / "NovaEra/static/"
]

#ESto é para que as imaxes que a xente sube ao crear un blog se garden na seguinte ruta
MEDIA_URL='/mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, "NovaEra/mediafiles")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Configurarción para poder enviar emails desde local
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#Para ocultar a dirección de correo e o contrasinal utilicei este video: https://www.youtube.com/watch?v=NRf1LeQju2g
EMAIL_HOST_USER = config('email')
EMAIL_HOST_PASSWORD = config('contrasinal_email')

#VÍDEOQ QUE TE TES QUEVER PARA QUE OS ARQUIVOS ESTÁTICOS QUE SUBA A PEÑITA SE GARDEN EN S3 (Amazon web services):
# https://www.youtube.com/watch?v=inQyZ7zFMHM
#Configuración do AWS 

#IMPORTNATÍSIMO ESTO PARA QUE CHE CARGUE OS ARCHIVOS QUE TES EN AMAZON
AWS_S3_REGION_NAME = 'eu-west-3' #change to your region
AWS_S3_SIGNATURE_VERSION = 's3v4'
#--------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = config('aws_key_id')
AWS_SECRET_ACCESS_KEY = config('aws_secret_key')
AWS_STORAGE_BUCKET_NAME = config('aws_bucket_name')

AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None
#En AWS (S3) é onde se van a gardar os arquivos que os usuarios da web van a subir
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#Esto é para referirse os arquivos estáticos da páxina web. Pero eu como estos archivos gardoos na propia app, comento esta liña.
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



#PAra tema de GitHub, se tes problemas cas branches ou co historial colles e fas o que di esta páxina:
#https://docs.github.com/es/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/adding-an-existing-project-to-github-using-github-desktop

#Pasos para facer deploy dende o teu ordenador:
#Para facer esto tes que instalar o CLI de heroku
# heroku login
# git init
# git add .
# git commit -m "nome-do-commit"
# heroku git:remote -a novaera
# git push heroku main

#Para crear o requirements.txt file necesario para facer o deploy en Heroku:
#pip freeze > requirements.txt

#Cando fas un cambio no modelo e tes que replicalo na base de datos de Heroku

