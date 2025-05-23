# apps/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from .forms import BoutiqueRegisterForm
from .models import User
from apps.boutiques.models import Boutique

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['is_vendor']:
                # Stocke l'ID utilisateur en session pour l'étape 2
                request.session['pending_vendor_id'] = user.id
                return redirect('register_boutique')
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def register_boutique(request):
    user_id = request.session.get('pending_vendor_id')
    if not user_id:
        return redirect('register')
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = BoutiqueRegisterForm(request.POST)
        if form.is_valid():
            boutique = form.save(commit=False)
            boutique.user = user
            boutique.save()
            form.save_m2m()
            user.is_vendor = True
            user.save()
            login(request, user)
            del request.session['pending_vendor_id']
            return redirect('home')
    else:
        form = BoutiqueRegisterForm()
    return render(request, 'register_boutique.html', {'form': form})