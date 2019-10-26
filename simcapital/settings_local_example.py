import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault('POSTGRES_NAME', 'simcapital'),
        'USER': os.environ.setdefault('POSTGRES_USER', 'simcapital'),
        'PASSWORD': os.environ.setdefault('POSTGRES_PASSWORD', 'string'),
        'HOST': os.environ.setdefault('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.setdefault('POSTGRES_PORT', '35432'),
    }
}
