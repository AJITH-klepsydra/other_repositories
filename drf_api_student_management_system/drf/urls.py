from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/',include('apps.users.urls')),
    path('api/v1/certificates/',include('apps.certificate.urls')),
    path('api/v1/lectures/', include('apps.lectures.urls')),
]
