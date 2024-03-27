from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class TestimoniAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("Nama", "Profesi", "Deskripsi")
    search_fields = ("Nama__startswith", )
    list_filter = ("Nama", )

admin.site.register(Testimoni, TestimoniAdmin)

admin.site.site_header = "Admin Toko Saya"
admin.site.site_title = "Toko Saya"
admin.site.index_title = "Admin Toko Saya"
