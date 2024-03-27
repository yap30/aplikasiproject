from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('mycv/', views.testimoni, name='mycv'),
    # path('postmycv/', views.testimoni_post, name='testimoni_post'),
]