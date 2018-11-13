
  # Dependencies

  ## Django
    
   #### Third Party App
    
   - Django Rest Framework (pip install djangorestframework)
   - django-cors-headers (pip install django-cors-headers)
     
    
   #### Middleware
    
    MIDDLEWARE = [
       ...................................,
      'corsheaders.middleware.CorsMiddleware',
      'django.middleware.common.CommonMiddleware',
      ......................................,
    ]

     
   #### RestFrameWork Permission
     
    REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES': (
      'rest_framework.permissions.AllowAny',
      )
    }
    
    
    
   ## React
   
   #### Packages
   - axios (npm install axios)
    
