from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, PenyewaanForm
from .models import Mobil, Penyewaan, RiwayatPenyewaan, Profile


# ------------------------
# AUTH
# ------------------------
class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('daftar_mobil')
        form = UserCreationForm()
        return render(request, 'rental/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('daftar_mobil')
        return render(request, 'rental/register.html', {'form': form})


class CustomLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('daftar_mobil')
        return render(request, 'rental/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('daftar_mobil')
        messages.error(request, 'Username atau password salah')
        return render(request, 'rental/login.html')


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'rental/change_password.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password berhasil diubah!')
        return super().form_valid(form)


# ------------------------
# STATIC PAGES
# ------------------------
class AboutView(TemplateView):
    template_name = 'rental/about.html'


class TermsView(TemplateView):
    template_name = 'rental/terms.html'


class ContactView(View):
    template_name = 'rental/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pesan Anda berhasil dikirim!')
            return redirect('contact')
        return render(request, self.template_name, {'form': form})


# ------------------------
# PROFILE
# ------------------------
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        return render(request, 'profil.html', {'profile': profile})


@method_decorator(login_required(login_url='login'), name='dispatch')
class EditProfileView(View):
    def get(self, request):
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)
        return render(request, 'edit_profil.html', {'user': user, 'profile': profile})

    def post(self, request):
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)

        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.username = request.POST.get('username', '')
        user.save()

        if 'foto' in request.FILES:
            profile.foto = request.FILES['foto']
            profile.save()

        messages.success(request, 'Profil berhasil diperbarui!')
        return redirect('profile')


# ------------------------
# MOBIL
# ------------------------
class DaftarMobilView(ListView):
    model = Mobil
    template_name = 'rental/daftar_mobil.html'
    context_object_name = 'daftar_mobil'

    def get_queryset(self):
        return Mobil.objects.filter(tersedia=True)


class DetailMobilView(DetailView):
    model = Mobil
    template_name = 'rental/detail_mobil.html'
    context_object_name = 'mobil'
    pk_url_kwarg = 'mobil_id'


@method_decorator(login_required(login_url='login'), name='dispatch')
class SewaMobilView(View):
    def get(self, request, mobil_id):
        mobil = get_object_or_404(Mobil, id=mobil_id)
        form = PenyewaanForm()
        return render(request, 'rental/sewa_mobil.html', {'form': form, 'mobil': mobil})

    def post(self, request, mobil_id):
        mobil = get_object_or_404(Mobil, id=mobil_id)
        form = PenyewaanForm(request.POST)

        if form.is_valid():
            penyewaan = form.save(commit=False)
            penyewaan.mobil = mobil
            penyewaan.nama_penyewa = request.user.username  # otomatis ambil nama user
            lama_sewa = (penyewaan.tanggal_selesai - penyewaan.tanggal_mulai).days
            lama_sewa = max(lama_sewa, 1)
            penyewaan.total_harga = lama_sewa * mobil.harga_per_hari
            penyewaan.save()

            mobil.tersedia = False
            mobil.save()

            RiwayatPenyewaan.objects.create(
                nama_penyewa=penyewaan.nama_penyewa,
                mobil=mobil,
                tanggal_mulai=penyewaan.tanggal_mulai,
                tanggal_selesai=penyewaan.tanggal_selesai,
                total_harga=penyewaan.total_harga
            )
            messages.success(request, f"Mobil {mobil.nama} berhasil disewa!")
            return redirect('riwayat_penyewaan')

        return render(request, 'rental/sewa_mobil.html', {'form': form, 'mobil': mobil})


@method_decorator(login_required(login_url='login'), name='dispatch')
class RiwayatPenyewaanView(ListView):
    model = RiwayatPenyewaan
    template_name = 'rental/riwayat_penyewaan.html'
    context_object_name = 'riwayat'

    def get_queryset(self):
        return RiwayatPenyewaan.objects.filter(nama_penyewa=self.request.user.username).order_by('-tanggal_mulai')
