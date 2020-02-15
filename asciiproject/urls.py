from django.contrib import admin
from django.urls import path

import asciiapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asciiapp.views.home, name='home'),
    path('encryption/', asciiapp.views.encryption, name='encryption'),
]
