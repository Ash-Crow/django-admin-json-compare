# django-admin-json-compare

POC for a function that allows to compare between two JSONFields in a Django project.

## Prérequis
- poetry
- postgresql

## Installer le projet
### Cloner le projet
- `git clone` ce répertoire quelque part et `cd` dedans.

### Régler les paramètres locaux
- `cp config/local_sample.py config/local.py`
- Remplir le fichier `local.py`

### Créer et activer l'environnement virtuel et installer les dépendances
- `poetry install`
- `poetry shell`
 
### Installer la structure de base de données et récupérer les fichiers statiques
- `python3 manage.py migrate`
- `python3 manage.py collectstatic`

### Créer le super-utilisateur
- ` python manage.py createsuperuser`

### Lancer le projet
 - `python3 manage.py runserver`
