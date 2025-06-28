from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('polling/', include('polling.urls')),
    path('admin/', admin.site.urls),
]
