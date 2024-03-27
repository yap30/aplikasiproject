from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class tabelbuku(models.Model):
    ID_Buku = models.IntegerField()
    Kategori = models.TextField()
    Nama_Buku = models.TextField()
    Harga = models.IntegerField()
    Stok = models.TextField()
    Penerbit = models.TextField()
    Penulis = models.TextField()
    Deskripsi_Buku = models.TextField()
    Foto = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.Kategori
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Foto.url))
    image_tag.short_description = 'Image'

class tabelpenerbit(models.Model):
    ID_Penerbit = models.IntegerField()
    Nama = models.TextField()
    Alamat = models.TextField()
    Kota = models.IntegerField()
    Telepon = models.TextField()
    Deskripsi_Penerbit = models.TextField()
    Foto = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.Nama

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Foto.url))
    image_tag.short_description = 'Image'