# Generated by Django 5.0.3 on 2024-03-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0002_bukumodel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bukumodel',
            name='author',
            field=models.CharField(default='author', max_length=200),
        ),
        migrations.AddField(
            model_name='bukumodel',
            name='file',
            field=models.FileField(default='mydocs/myfile.pdf', upload_to='mydocs'),
        ),
    ]
