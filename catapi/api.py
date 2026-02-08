from flask import Blueprint
import requests

api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

API_KEY = "tvuj_api_klic"
headers = {
    "x-api-key": API_KEY
}

def GetRandomCatImage():
    response = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None
