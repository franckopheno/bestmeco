from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from apps.catalog.models import Product  # Assure-toi que le modèle Product est bien importé

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

def join_tuple_string(strings_tuple) -> str:
    return ' '.join([str(s) for s in strings_tuple if s is not None])

def get_feature_products():
    product_list = list(Product.objects.values_list('name', 'description'))
    result = list(map(join_tuple_string, product_list))
    return result

def get_products_with_id():
    feature_product = get_feature_products()
    all_products_id = list(Product.objects.values_list('id', flat=True))
    products_with_id = {}
    for index, id in enumerate(all_products_id):
        products_with_id[id] = feature_product[index]
    return products_with_id

def similar_products(product_id, no_similar_prod):
    all_products = get_feature_products()
    all_products_id = list(Product.objects.values_list('id', flat=True))
    cm = CountVectorizer().fit_transform(all_products)
    cs = cosine_similarity(cm)
    product_index = all_products_id.index(product_id)
    unsorted_similar_product = list(enumerate(cs[product_index]))
    sorted_similar_product = sorted(unsorted_similar_product, key=lambda x: x[1], reverse=True)
    similar_products_query_set = []
    temp = 0
    for product in sorted_similar_product:
        if all_products_id[product[0]] == product_id:
            continue  # skip itself
        similar_products_query_set.append(Product.objects.get(id=all_products_id[product[0]]))
        temp += 1
        if temp >= no_similar_prod:
            break
    return similar_products_query_set

def products_view(request):
    products = Product.objects.all()
    # Pour chaque produit, on peut ajouter les similaires si besoin
    # Exemple pour le premier produit :
    similar = []
    if products.exists():
        similar = similar_products(products.first().id, 4)
    return render(request, 'products.html', {'products': products, 'similar_products': similar})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # Tu peux aussi ajouter des produits similaires ici si tu veux
    similar = similar_products(product.id, 4)
    return render(request, 'product-infos.html', {'product': product, 'similar_products': similar})


