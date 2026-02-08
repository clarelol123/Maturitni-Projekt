from flask import Blueprint
import requests

api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets')

# API klíč – pokud by API vyžadovalo autentifikaci (tady aktuálně není využit)
API_KEY = "your_api_key"

# Hlavičky požadavku (zde prázdné, ale můžeš přidat např. autentifikaci)
headers = {
    # "x-api-key": API_KEY  # pokud by bylo potřeba
}

# Funkce pro získání náhodného obrázku kočky z thecatapi.com
def GetRandomCatImage():
    # Odeslání GET požadavku na API pro náhodný obrázek
    response = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
    
    # Pokud je odpověď v pořádku (HTTP 200), vrať JSON odpověď
    if response.status_code == 200:
        return response.json()
    else:
        # Pokud došlo k chybě, vrať None
        return None