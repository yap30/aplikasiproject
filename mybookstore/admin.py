from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class tabelbukuAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("ID_Buku", "Kategori", "Nama_Buku", "Harga", "Stok", "Penerbit", "Penulis", "Deskripsi_Buku", "image_tag")
    search_fields = ("ID_Buku__startswith", )
    list_filter = ("ID_Buku", )

class tabelpenerbitAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("ID_Penerbit", "Nama", "Alamat", "Kota", "Telepon", "Deskripsi_Penerbit", "image_tag")
    search_fields = ("ID_Penerbit__startswith", )
    list_filter = ("ID_Penerbit", )

admin.site.register(tabelbuku, tabelbukuAdmin)
admin.site.register(tabelpenerbit, tabelpenerbitAdmin)

admin.site.site_header = "Admin Toko Saya"
admin.site.site_title = "Toko Saya"
admin.site.index_title = "Admin Toko Saya"


