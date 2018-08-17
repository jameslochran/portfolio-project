SECRET_KEY = '#@w7*a)12_d-e1r%uo(=45p3l(x13zp2m#1t8a1$b6kurv^^'

ALLOWED_HOSTS = ['167.99.154.197', 'jlochran.com', 'www.jlochran.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfoliodb',
        'USER': 'djangodbuser',
        'PASSWORD': 'Organug07' ,
        'HOST': '127.0.0.1',
        'PORT' : '5432',

          }
}
DEBUG = False
