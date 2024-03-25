from django.contrib import admin
from django.urls import path
from . import views 
from .views import create_view

urlpatterns = [
    path('create/', views.create_view, name='create view'),
    path('list/', views.list_view, name='list view'),
    path('<id>', views.detail_view, name='detail view'),
    path('<id>/update/', views.update_view, name='update view'),
    path('<id>/delete/', views.delete_view,name='delete view'),

]