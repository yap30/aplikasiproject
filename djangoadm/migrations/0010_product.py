# Generated by Django 5.0.3 on 2024-03-21 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoadm', '0009_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField()),
                ('ProductName', models.TextField()),
                ('SupplierID', models.IntegerField()),
                ('CategoryID', models.IntegerField()),
                ('Unit', models.TextField()),
                ('Price', models.IntegerField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('ProductDescription', models.TextField()),
            ],
        ),
    ]