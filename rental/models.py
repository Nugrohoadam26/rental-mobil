from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Pengguna")
    foto = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="Foto Profil")

    class Meta:
        verbose_name = "Profil Pengguna"
        verbose_name_plural = "Daftar Profil Pengguna"

    def __str__(self):
        return self.user.username


class Mobil(models.Model):
    nama = models.CharField(max_length=100, verbose_name="Nama Mobil")
    merk = models.CharField(max_length=100, verbose_name="Merk")
    tahun = models.IntegerField(verbose_name="Tahun Produksi")
    jumlah_kursi = models.IntegerField(verbose_name="Jumlah Kursi")
    transmisi = models.CharField(max_length=50, verbose_name="Jenis Transmisi")
    plat_nomor = models.CharField(max_length=20, verbose_name="Plat Nomor")
    tersedia = models.BooleanField(default=True, verbose_name="Tersedia")
    harga_per_hari = models.IntegerField(default=100000, verbose_name="Harga per Hari")
    gambar = models.ImageField(upload_to='mobil/', blank=True, null=True, verbose_name="Gambar Mobil")

    class Meta:
        verbose_name = "Mobil"
        verbose_name_plural = "Daftar Mobil"

    def __str__(self):
        return f"{self.nama} ({self.plat_nomor})"


class Penyewaan(models.Model):
    nama_penyewa = models.CharField(max_length=100, verbose_name="Nama Penyewa")
    mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE, verbose_name="Mobil")
    tanggal_mulai = models.DateField(verbose_name="Tanggal Mulai")
    tanggal_selesai = models.DateField(verbose_name="Tanggal Selesai")
    total_harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Harga")

    class Meta:
        verbose_name = "Penyewaan"
        verbose_name_plural = "Daftar Penyewaan"

    def __str__(self):
        return f"{self.nama_penyewa} - {self.mobil.nama}"


class RiwayatPenyewaan(models.Model):
    nama_penyewa = models.CharField(max_length=100, verbose_name="Nama Penyewa")
    mobil = models.ForeignKey(Mobil, on_delete=models.CASCADE, verbose_name="Mobil")
    tanggal_mulai = models.DateField(verbose_name="Tanggal Mulai")
    tanggal_selesai = models.DateField(verbose_name="Tanggal Selesai")
    total_harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Harga")

    class Meta:
        verbose_name = "Riwayat Penyewaan"
        verbose_name_plural = "Daftar Riwayat Penyewaan"

    def __str__(self):
        return f"{self.nama_penyewa} - {self.mobil.nama}"
