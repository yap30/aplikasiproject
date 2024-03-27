from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Testimoni(models.Model):
    Nama = models.CharField(max_length=200)
    Profesi = models.CharField(max_length=200)
    Deskripsi = models.TextField(max_length=200)

