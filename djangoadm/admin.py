from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class CustomerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("CustomerID", "CustomerName", "ContactName", "Address", "City", "PostalCode", "Country", "image_tag")
    search_fields = ("CustomerID__startswith", )
    list_filter = ("CustomerID", )

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("CategoryID", "CategoryName", "Description")
    search_fields = ("CategoryID__startswith", )
    list_filter = ("CategoryID", )

class EmployeeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("EmployeeID", "LastName", "FirstName", "BirthDate", "image_tag", "Notes")
    search_fields = ("EmployeeID__startswith", )
    list_filter = ("EmployeeID", )

class OrderDetailAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("OrderDetailID", "OrderID", "ProductID", "Quantity")
    search_fields = ("OrderDetailID__startswith", )
    list_filter = ("OrderDetailID", )

class OrderAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("OrderID", "CustomerID", "EmployeeID", "OrderDate", "ShipperID")
    search_fields = ("OrderID__startswith", )
    list_filter = ("OrderID", )

class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("ProductID", "ProductName", "ProductDescription", "SupplierID", "CategoryID", "Unit", "Price", "image_tag")
    search_fields = ("ProductID__startswith", )
    list_filter = ("ProductID", )

class ShipperAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("ShipperID", "ShipperName", "Phone")
    search_fields = ("ShipperID__startswith", )
    list_filter = ("ShipperID", )

class SupplierAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("SupplierID", "SupplierName", "ContactName", "Address", "City", "PostalCode", "Country", "Phone")
    search_fields = ("SupplierID__startswith", )
    list_filter = ("SupplierID", )

class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("contact_name", "contact_email", "message")
    search_fields = ("contact_email__startswith", )
    list_filter = ("contact_email", )

class ReviewAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("product_id", "customer_name", "customer_email", "customer_review", "rate", "date")
    search_fields = ("customer_email__startswith", )
    list_filter = ("customer_email", )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Review, ReviewAdmin)

admin.site.site_header = "Admin Toko Saya"
admin.site.site_title = "Toko Saya"
admin.site.index_title = "Admin Toko Saya"



