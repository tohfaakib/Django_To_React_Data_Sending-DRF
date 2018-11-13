# Django_To_React_Data_Sending-(Django Rest Framework)

# Dependecncies:

# DJango:

# App

- Dgango Rest Framework (pip install djangorestframework)
- django-cors-headers (pip install django-cors-headers)

# Middleware

MIDDLEWARE = [
................................,
'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',
..................................,
]

# RestFrameWork_Permission

REST_FRAMEWORK = {
'DEFAULT_PERMISSION_CLASSES': (
'rest_framework.permissions.AllowAny',
)
}
