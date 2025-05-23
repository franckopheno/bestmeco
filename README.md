
---

# 🛍️ MECO – Plateforme de commerce électronique

MECO est une application web développée avec Django, conçue pour faciliter la gestion de boutiques en ligne. Elle permet aux vendeurs de créer et gérer leurs boutiques, produits, variantes, stocks, et bien plus encore.

---

## 📋 Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## ✨ Fonctionnalités

- Gestion des utilisateurs avec rôles (vendeur, client, administrateur)
- Création et gestion de boutiques avec informations détaillées (nom, localisation, type, catégories, lien du site)
- Gestion des produits avec variantes (couleur, taille, etc.) et suivi des stocks
- Organisation des produits en catégories et sous-catégories
- Interface d'administration personnalisée pour une meilleure expérience utilisateur
- Téléversement et affichage des images des produits

---

## ⚙️ Prérequis

- Python 3.8 ou supérieur
- Django 4.2 ou supérieur
- PostgreSQL ou SQLite
- [Pillow](https://pypi.org/project/Pillow/) pour la gestion des images
- [django-jazzmin](https://github.com/farridav/django-jazzmin) pour personnaliser l'interface d'administration

---

## 🚀 Installation

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/votre-utilisateur/bestmeco.git
   cd meco
   ```

2. **Créer et activer un environnement virtuel**

   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données**

   - Modifier les paramètres de la base de données dans `meco/settings.py` si nécessaire.

   - Appliquer les migrations :

     ```bash
     python manage.py migrate
     ```

5. **Créer un superutilisateur**

   ```bash
   python manage.py createsuperuser
   ```

6. **Lancer le serveur de développement**

   ```bash
   python manage.py runserver
   ```

   Accéder à l'application via [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Utilisation

- Accéder à l'interface d'administration via [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Ajouter des catégories, sous-catégories, produits et variantes
- Gérer les informations des boutiques et des vendeurs
- Visualiser et gérer les stocks en temps réel

---

## 🗂️ Structure du projet

```
meco/
├── apps/
│   ├── accounts/      # Gestion des utilisateurs et des vendeurs
│   ├── catalog/       # Gestion des produits, catégories et variantes
│   ├── core/          # Pages statiques, layouts et configurations globales
│   └── orders/        # Gestion des commandes (à venir)
├── media/             # Fichiers médias téléversés (images des produits)
├── static/            # Fichiers statiques (CSS, JS, images)
├── templates/         # Templates HTML
├── meco/              # Configuration principale du projet
├── manage.py
└── requirements.txt
```

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour contribuer :

1. Forker le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`)
3. Commiter vos modifications (`git commit -am 'Ajout de ma fonctionnalité'`)
4. Pusher la branche (`git push origin feature/ma-fonctionnalité`)
5. Ouvrir une Pull Request

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

---

N'hésitez pas à personnaliser ce `README.md` en fonction des spécificités de votre projet MECO. 
