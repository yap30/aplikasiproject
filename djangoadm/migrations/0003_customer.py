# Generated by Django 5.0.3 on 2024-03-20 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoadm', '0002_category_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerID', models.IntegerField()),
                ('CustomerName', models.TextField()),
                ('ContactName', models.TextField()),
                ('Address', models.TextField()),
                ('City', models.TextField()),
                ('PostalCode', models.TextField()),
                ('Country', models.TextField()),
            ],
        ),
    ]
