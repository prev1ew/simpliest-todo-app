from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.index, name='index'),
    path('', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('change/<str:pk>', views.change_todo_item, name='change'),
    path('delete/<str:pk>', views.delete_todo_item, name='delete'),
]
