🛍️ MECO – Plateforme de commerce électronique
MECO est une application web développée avec Django, conçue pour faciliter la gestion de boutiques en ligne. Elle permet aux vendeurs de créer et gérer leurs boutiques, produits, variantes, stocks, et bien plus encore.

📋 Sommaire
Fonctionnalités

Prérequis

Installation

Utilisation

Structure du projet

Contribuer

Licence

✨ Fonctionnalités
Gestion des utilisateurs avec rôles (vendeur, client, administrateur)

Création et gestion de boutiques avec informations détaillées (nom, localisation, type, catégories, lien du site)

Gestion des produits avec variantes (couleur, taille, etc.) et suivi des stocks

Organisation des produits en catégories et sous-catégories

Interface d'administration personnalisée pour une meilleure expérience utilisateur

Téléversement et affichage des images des produits

⚙️ Prérequis
Python 3.8 ou supérieur

Django 4.2 ou supérieur

PostgreSQL ou SQLite

Pillow pour la gestion des images

django-jazzmin pour personnaliser l'interface d'administration

🚀 Installation
Cloner le dépôt

bash
Copier
Modifier
git clone https://github.com/votre-utilisateur/meco.git
cd meco
Créer et activer un environnement virtuel

bash
Copier
Modifier
python -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate
Installer les dépendances

bash
Copier
Modifier
pip install -r requirements.txt
Configurer la base de données

Modifier les paramètres de la base de données dans meco/settings.py si nécessaire.

Appliquer les migrations :

bash
Copier
Modifier
python manage.py migrate
Créer un superutilisateur

bash
Copier
Modifier
python manage.py createsuperuser
Lancer le serveur de développement

bash
Copier
Modifier
python manage.py runserver
Accéder à l'application via http://127.0.0.1:8000/
