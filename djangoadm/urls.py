from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('landingpage/', views.landing, name='landing'),
    path('<id>/landingpageproductdetail/', views.product, name='product'),
    path('landingpageabout/', views.contact, name='contact'),
    path('landingpagesignup/', views.user_signup, name='user_signup'),
    path('landingpagelogin/', views.user_login, name='user_login'),
    path('landingpagelogout/', views.user_logout, name='user_logout'),
    path('landingpageproductdetail/', views.create_review, name='create_review'),
    path('<id>/', views.product, name='detail_review'),
]