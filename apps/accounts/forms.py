# apps/accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from apps.boutiques.models import Boutique

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_vendor = forms.BooleanField(required=False, label="Je veux être vendeur")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2', 'is_vendor']

class BoutiqueRegisterForm(forms.ModelForm):
    class Meta:
        model = Boutique
        fields = ['name', 'city', 'neighborhood', 'shop_type', 'categories', 'website']
        widgets = {
            'categories': forms.CheckboxSelectMultiple,
        }