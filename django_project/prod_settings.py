import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'IYjmGfjSLygdeJZAOPhkqtedDVScDNyOnHawoLQZLWcPhDpVtYflrkRVHJXlYvZmE'

DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
