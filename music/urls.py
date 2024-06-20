from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('musician/add/', views.musician_create, name='musician_create'),
    path('musician/<int:pk>/edit/', views.musician_edit, name='musician_edit'),
    path('musician/<int:pk>/delete/', views.musician_delete, name='musician_delete'),
    path('album/add/', views.album_create, name='album_create'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
]
