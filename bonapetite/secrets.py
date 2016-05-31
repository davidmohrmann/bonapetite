
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r+2eetsy46jia8sz*4eqth070-ojggb9h+jwjdj*^142w8ea7-'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mister',
        'USER': 'davidmohrmann',
        'PASSWORD': 'admin123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
