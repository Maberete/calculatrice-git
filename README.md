# Calculatrice Git

## Authentification

Le module 'auth.py' gere la connexion des utilisateurs.
- 'login(username, password)' -> verifie les identifiants
- 'logout(username)' -> retourne un message de deconnexion

## Gestion des donnees

Le module 'data.py' permet de charger et sauvegarder des donnees CSV.
- 'load_csv(filepath)' -> charge un fichier CSV en liste de dicts
- 'save_csv(filepath, data)' -> sauvegarde une liste de dicts en CSV