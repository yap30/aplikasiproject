# Generated by Django 5.0.3 on 2024-03-20 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoadm', '0007_alter_employee_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
