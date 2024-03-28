from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Testimoni(models.Model):
    Nama = models.CharField(max_length=200)
    Profesi = models.CharField(max_length=200)
    Deskripsi = models.TextField(max_length=200)

class Berita(models.Model):
    Judul = models.CharField(max_length=200)
    Deskripsi = models.TextField(max_length=200)
    Foto = models.ImageField(upload_to='images', blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Foto.url))
    image_tag.short_description = 'Image'
