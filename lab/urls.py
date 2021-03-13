from django.urls import path
from . import views

urlpatterns = [
    path('addNew', views.addNew, name="addNew"),
    path('delete', views.delete, name='delete'),
    path('<str:name>', views.index, name="index"),
]


