# Generated by Django 5.0.3 on 2024-03-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0003_remove_testimoni_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=200)),
                ('Deskripsi', models.TextField(max_length=200)),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
