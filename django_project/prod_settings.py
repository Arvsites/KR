import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'IYjmGfjSLygdeJZAOPhkqtedDVScDNyOnHawoLQZLWcPhDpVtYflrkRVHJXlYvZmE'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '194.67.121.74', '2a00:f940:2:4:2::2619', '37-140-197-191.cloudvps.regruhosting.ru',
                 'multimer.ru']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
