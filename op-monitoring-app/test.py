import requests
from requests.auth import HTTPBasicAuth

# Tes identifiants
username = "sjaziri@itops.group"
password = "Saif12345++!"  

# URL d’un exemple d’endpoint API BoondManager
url = "https://support.boondmanager.com/hc/fr"

# Requête avec Basic Auth
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Résultat
if response.status_code == 200:
    print("Connexion réussie ✅")
    print(response.json())  # Affiche les données reçues
else:
    print(f"Erreur {response.status_code} ❌")
    print(response.text)
