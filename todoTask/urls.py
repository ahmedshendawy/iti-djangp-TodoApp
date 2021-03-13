from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path('add', views.create, name="addNew"),
    path('update/<int:id>', views.update, name="updateTask"),
    path('delete/<int:id>', views.delete, name="deleteTask"),
]
