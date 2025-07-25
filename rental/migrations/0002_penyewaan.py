# Generated by Django 5.0.2 on 2025-07-03 15:57

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penyewaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_penyewa', models.CharField(max_length=100)),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('tanggal_dipesan', models.DateTimeField(default=django.utils.timezone.now)),
                ('mobil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.mobil')),
            ],
        ),
    ]
