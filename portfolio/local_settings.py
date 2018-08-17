SECRET_KEY = '#@w7*a)12_d-e1r%uo(=45p3l(x13zp2m#1t8a1$b6kurv^^hotdoge5'

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


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jimlochran@gmail.com'
EMAIL_HOST_PASSWORD = 'OmlGml01'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEBUG = False
