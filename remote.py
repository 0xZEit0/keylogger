import requests
import time

file_path = "log.txt" # Chemin absolu vers le fichier à surveiller

# Récupération de la taille du fichier initial
with open(file_path, "rb") as f:
    initial_size = len(f.read())

while True:
    # Récupération de la taille du fichier actuelle
    with open(file_path, "r", encoding='utf-8') as f:
        current_size = len(f.read())
    
    # Si la taille du fichier a changé, envoie une requête GET avec les paramètres de requête
    if current_size != initial_size:
        with open(file_path, "r") as f:
            content = f.read()
        
        # Construction de l'URL avec les paramètres de requête
        url = "http://localhost:3000/"
        params = {"data": content}
        
        # Envoi de la requête GET avec les paramètres de requête
        response = requests.get(url, params=params)
        
        # Mise à jour de la taille du fichier initial
        initial_size = current_size
    
    # Attente de 1 seconde avant la prochaine vérification
    time.sleep(1)
