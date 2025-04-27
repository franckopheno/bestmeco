from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),
    
    path('cartuser', views.cartuser, name='cartuser'),
    
    path('products', views.products_view, name='products'),
    # path pour les details d'un produit avec le slug dans l'url
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Pages de contact
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    
    # Pages à propos
    path('about/', views.about, name='about'),
    path('about/team/', views.team, name='team'),
    
    # Pages de services
    path('services/', views.services, name='services'),
    path('services/<slug:service_slug>/', views.service_detail, name='service_detail'),
    
    # Pages de blog
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:post_slug>/', views.blog_detail, name='blog_detail'),
    
    # Pages de FAQ
    path('faq/', views.faq, name='faq'),
    
    # Pages de politique
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    
    # Pages d'erreur
    path('404/', views.error_404, name='error_404'),
    path('500/', views.error_500, name='error_500'),
]
