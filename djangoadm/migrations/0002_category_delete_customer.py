# Generated by Django 5.0.3 on 2024-03-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoadm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryID', models.IntegerField()),
                ('CategoryName', models.TextField()),
                ('Description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
