from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Penyewaan, ContactMessage


class PenyewaanForm(forms.ModelForm):
    class Meta:
        model = Penyewaan
        fields = ['nama_penyewa', 'tanggal_mulai', 'tanggal_selesai']
        labels = {
            'nama_penyewa': 'Nama Penyewa',
            'tanggal_mulai': 'Tanggal Mulai Sewa',
            'tanggal_selesai': 'Tanggal Selesai Sewa',
        }
        widgets = {
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nama Pengguna',
            'email': 'Email',
            'password1': 'Kata Sandi',
            'password2': 'Konfirmasi Kata Sandi',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Anda'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Anda'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tulis pesan Anda...'}),
        }
