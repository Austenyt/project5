from django.urls import path

from materials.apps import MaterialsConfig
app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', MaterialsCreateView.as_view(), name='create'),
    path('', MaterialsCreateView.as_view(), name='list'),
    path('view/<int:pk>/', MaterialsCreateView.as_view(), name='view'),
    path('edit/<int:pk>/', MaterialsCreateView.as_view(), name='edit'),
    path('delete/<int:pk>/', MaterialsCreateView.as_view(), name='delete'),
]
