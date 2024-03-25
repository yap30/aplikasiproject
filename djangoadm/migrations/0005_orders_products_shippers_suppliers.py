# Generated by Django 5.0.3 on 2024-03-20 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoadm', '0004_employees_orderdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderID', models.IntegerField()),
                ('CustomerID', models.IntegerField()),
                ('EmployeeID', models.IntegerField()),
                ('OrderDate', models.DateField()),
                ('ShipperID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField()),
                ('ProductName', models.TextField()),
                ('SupplierID', models.IntegerField()),
                ('CategoryID', models.IntegerField()),
                ('Unit', models.TextField()),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShipperID', models.IntegerField()),
                ('ShipperName', models.TextField()),
                ('Phone', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupplierID', models.IntegerField()),
                ('SupplierName', models.TextField()),
                ('ContactName', models.TextField()),
                ('Address', models.TextField()),
                ('City', models.TextField()),
                ('PostalCode', models.TextField()),
                ('Country', models.TextField()),
                ('Phone', models.TextField()),
            ],
        ),
    ]
