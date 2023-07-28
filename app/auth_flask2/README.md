#Comment ajouter l’authentification à votre application avec Flask-Login

Étape 1 — Installation des paquets
Il y a trois packages principaux dont vous avez besoin pour votre projet :
    . Flask
    . Flask-login : pour gérer les sessions utilisateur après authentification
    . Flask-SQLAlchemy: pour gérer les sessions utilisateur après authentification

Vous utiliserez SQLite pour éviter d’avoir à installer des dépendances supplémentaires pour la base de données.

installer: auth, SQLite
>>> sqlite3 db.sqlite3
>>> .tables

Cette application utilisera le modèle d’usine de l’application Flask avec des plans. 
Un Blueprint gère les itinéraires réguliers, qui incluent l’index et la page de profil protégée.
Un autre plan gère tout ce qui concerne l’authentification. 
Dans une application réelle, vous pouvez décomposer les fonctionnalités comme vous le souhaitez, mais la solution abordée ici fonctionnera bien pour ce tutoriel.

Ce fichier aura la fonction de créer l’application, qui initialisera la base de données et enregistrera les plans. 
Pour le moment, cela ne fera pas grand-chose, mais ce sera nécessaire pour le reste de l’application.

https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

Étape 2 — Création du fichier d’application principal
Étape 3 — Ajout d’itinéraires
Pour les itinéraires, vous utiliserez deux plans.

Pour le, vous aurez une page d’accueil () et une page de profil ().main_blueprint//profile

Tout d’abord, créez :main.py

.
└── flask_auth_app
    └── project
        ├── __init__.py       # setup the app
        ├── auth.py           # the auth routes for the app
        ├── db.sqlite         # the database
        ├── main.py           # the non-auth routes for the app
        ├── models.py         # the user model
        └── templates
            ├── base.html     # contains common layout and links
            ├── index.html    # show the home page
            ├── login.html    # show the login form
            ├── profile.html  # show the profile page
            └── signup.html   # show the signup form

<!-- =========== important link ============ -->
https://stackoverflow.com/questions/31093558/get-content-from-parent-block-in-jinja2


python 3.10
pip 
pip install flask

python -m pip install flask


.flaskenv
FLASK_APP = "__init__"
FLASK_ENV = "development"
FLASK_DEBUG = True
SERVER_NAME='azert'
FLASK_RUN_HOST ='192.168.88.158'
FLASK_RUN_PORT=8000

flask run