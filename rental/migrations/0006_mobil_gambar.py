# Generated by Django 5.0.2 on 2025-07-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0005_remove_mobil_harga_sewa_mobil_harga_per_hari_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='mobil/'),
        ),
    ]
