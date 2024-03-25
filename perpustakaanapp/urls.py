from django.urls import path
from . import views

urlpatterns = [
    path('beranda/', views.beranda, name='beranda'),
    path('profile/', views.profile, name='profile'),
    path('rekomendasi/', views.rekomendasi, name='rekomendasi'),
    path('reservasi_kunjungan/', views.reservasi_kunjungan, name='reservasi_kunjungan'),
]

