from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('landingpage/', views.landing, name='landing'),
    path('<id>/landingpageproductdetail/', views.product, name='product'),
    path('landingpageabout/', views.contact, name='contact'),
    path('landingpagelogin/', views.user_login, name='user_login'),
    path('landingpageregister/', views.register, name='register'),
    path('landingpagelogout/', views.user_logout, name='user_logout'),
    path('landingpageproductdetail/', views.create_review, name='create_review'),
    path('landingpagecart/', views.cart, name='cart'),
    path('<id>/', views.product, name='detail_review'),
]