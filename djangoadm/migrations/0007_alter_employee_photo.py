# Generated by Django 5.0.3 on 2024-03-20 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoadm', '0006_rename_employees_employee_rename_orders_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
