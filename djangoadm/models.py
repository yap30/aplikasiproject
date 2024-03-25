from django.db import models
from datetime import datetime
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Author(models.Model):
#     User = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField()

#     def __str__(self):
#         return self.user.username

# class Category(models.Model):
#     title = models.CharField(max_length=20)

#     def __str__(self):
#         return self.title
    

class Customer(models.Model):
    CustomerID = models.IntegerField()
    CustomerName = models.TextField()
    ContactName = models.TextField()
    Address = models.TextField()
    City = models.TextField()
    PostalCode = models.TextField()
    Country = models.TextField()
    Photo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.CustomerName

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Photo.url))
    image_tag.short_description = 'Image'

class Category(models.Model):
    CategoryID = models.IntegerField()
    CategoryName = models.TextField()
    Description = models.TextField()

    def __str__(self):
        return self.CategoryName

class Employee(models.Model):
    EmployeeID = models.IntegerField()
    LastName = models.TextField()
    FirstName = models.TextField()
    BirthDate = models.DateField(default=datetime.now)
    Photo = models.ImageField(upload_to='images', blank=True, null=True)
    Notes = models.TextField()

    def __str__(self):
        return self.FirstName

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Photo.url))
    image_tag.short_description = 'Image'

class OrderDetail(models.Model):
    OrderDetailID = models.IntegerField()
    OrderID = models.IntegerField()
    ProductID = models.IntegerField()
    Quantity = models.IntegerField()

    def __str__(self):
        return self.OrderID

class Order(models.Model):
    OrderID = models.IntegerField()
    CustomerID = models.IntegerField()
    EmployeeID = models.IntegerField()
    OrderDate = models.DateField()
    ShipperID = models.IntegerField()

    def __str__(self):
        return self.CustomerID

class Product(models.Model):
    ProductID = models.IntegerField()
    ProductName = models.TextField()
    SupplierID = models.IntegerField()
    CategoryID = models.IntegerField()
    Unit = models.TextField()
    Price = models.IntegerField()
    Photo = models.ImageField(upload_to='images', blank=True, null=True)
    ProductDescription = models.TextField()

    def __str__(self):
        return self.ProductName

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.Photo.url))
    image_tag.short_description = 'Image'

class Shipper(models.Model):
    ShipperID = models.IntegerField()
    ShipperName = models.TextField()
    Phone = models.TextField()

    def __str__(self):
        return self.ShipperName

class Supplier(models.Model):
    SupplierID = models.IntegerField()
    SupplierName = models.TextField()
    ContactName = models.TextField()
    Address = models.TextField()
    City = models.TextField()
    PostalCode = models.TextField()
    Country = models.TextField()
    Phone = models.TextField()

    def __str__(self):
        return self.SupplierName

class Contact(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    message = models.TextField()

class Review(models.Model):
    product_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    customer_review = models.TextField()
    rate = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
