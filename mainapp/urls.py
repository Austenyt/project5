from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import contact, StudentListView, StudentDetailView

app_name = MainappConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='view_student')
]
