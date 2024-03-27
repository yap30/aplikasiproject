from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('mybookstore/', views.book_catalog, name='book_catalog'),
]