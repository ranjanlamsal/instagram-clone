
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photo/', include('photo_app.urls')),
    path('user/', include('user_app.urls'))
]
