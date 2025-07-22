from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rental.views import (
    RegisterView, CustomLoginView, CustomLogoutView, CustomPasswordChangeView,
    AboutView, TermsView, ContactView,
    ProfileView, EditProfileView,
    DaftarMobilView, DetailMobilView, SewaMobilView, RiwayatPenyewaanView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Profil
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/password/', CustomPasswordChangeView.as_view(), name='change_password'),

    # Halaman Informasi
    path('about/', AboutView.as_view(), name='about'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('contact/', ContactView.as_view(), name='contact'),

    # Aplikasi rental
    path('', DaftarMobilView.as_view(), name='home'),
    path('mobil/', DaftarMobilView.as_view(), name='daftar_mobil'),
    path('mobil/<int:mobil_id>/', DetailMobilView.as_view(), name='detail_mobil'),
    path('sewa/<int:mobil_id>/', SewaMobilView.as_view(), name='sewa_mobil'),
    path('riwayat/', RiwayatPenyewaanView.as_view(), name='riwayat_penyewaan'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
