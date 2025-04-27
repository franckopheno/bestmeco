from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView

def home(request):
    """Vue pour la page d'accueil"""
    return render(request, 'index.html')
# route pour voir le contenus du panier
def cartuser(request):
    """Vue pour la page du panier"""
    return render(request, 'cart.html')

def contact(request):
    """Vue pour la page de contact"""
    if request.method == 'POST':
        # Traitement du formulaire de contact
        pass
    return render(request, 'templates/contact.html')

def contact_success(request):
    """Vue pour la page de succès du contact"""
    return render(request, 'templates/contact_success.html')

def about(request):
    """Vue pour la page à propos"""
    return render(request, 'templates/about.html')

def team(request):
    """Vue pour la page équipe"""
    return render(request, 'templates/team.html')

def services(request):
    """Vue pour la liste des services"""
    return render(request, 'templates/services.html')

def service_detail(request, service_slug):
    """Vue pour le détail d'un service"""
    return render(request, 'templates/service_detail.html', {'service_slug': service_slug})

def blog_list(request):
    """Vue pour la liste des articles de blog"""
    return render(request, 'templates/blog_list.html')

def blog_detail(request, post_slug):
    """Vue pour le détail d'un article de blog"""
    return render(request, 'templates/blog_detail.html', {'post_slug': post_slug})

def faq(request):
    """Vue pour la page FAQ"""
    return render(request, 'templates/faq.html')

def privacy_policy(request):
    """Vue pour la page de politique de confidentialité"""
    return render(request, 'templates/privacy_policy.html')

def terms_of_service(request):
    """Vue pour la page des conditions d'utilisation"""
    return render(request, 'templates/terms_of_service.html')

def error_404(request, exception):
    """Vue pour la page d'erreur 404"""
    return render(request, 'templates/404.html', status=404)

def error_500(request):
    """Vue pour la page d'erreur 500"""
    return render(request, 'templates/500.html', status=500)