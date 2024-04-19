DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mony',
        'USER': 'ayhan',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}