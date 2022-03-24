import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'AbnEuCaCqV2L570Ph3PTAnkEg3JFHAhFYfz4yRz6E2ENVuNuayJ0hTsVTyfasB5y'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '37.140.197.191', '2a00:f940:2:4:2::2619', '37-140-197-191.cloudvps.regruhosting.ru',
                 'multimer.ru']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kr',
        'USER': 'postgres',
        'PASSWORD': 'FjhfNB693>M',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
