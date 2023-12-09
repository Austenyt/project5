from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import index, contact

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact')
]
