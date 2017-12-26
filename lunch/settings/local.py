from .base import *

SECRET_KEY = '&+tigon=iph0o15@*ngx%-cgwt8&#jwtkc3et2qpperkbz0=eq'
DEBUG = True
TEMPLATE_DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}