import django


SECRET_KEY = 'qaz123'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqlite'
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'authrole',
    'tests',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

MIDDLEWARE_CLASSES = []

ROOT_URLCONF = 'tests.urls'

if django.VERSION[:2] <= (1, 6):
    INSTALLED_APPS += ['south']
