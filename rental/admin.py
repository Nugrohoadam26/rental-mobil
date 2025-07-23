from django.contrib import admin
from .models import Mobil, RiwayatPenyewaan, ContactMessage

@admin.register(Mobil)
class MobilAdmin(admin.ModelAdmin):
    list_display = ('id', 'merk', 'nama', 'tahun', 'harga_per_hari', 'tersedia')
    list_filter = ('merk', 'tahun', 'tersedia')
    actions = ['tandai_tersedia', 'tandai_tidak_tersedia']  # aksi tambahan

    @admin.action(description='Tandai mobil sebagai tersedia')
    def tandai_tersedia(self, request, queryset):
        queryset.update(tersedia=True)

    @admin.action(description='Tandai mobil sebagai tidak tersedia')
    def tandai_tidak_tersedia(self, request, queryset):
        queryset.update(tersedia=False)


@admin.register(RiwayatPenyewaan)
class RiwayatPenyewaanAdmin(admin.ModelAdmin):
    list_display = ('nama_penyewa', 'mobil', 'tanggal_mulai', 'tanggal_selesai')
    list_filter = ('tanggal_mulai', 'tanggal_selesai')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)