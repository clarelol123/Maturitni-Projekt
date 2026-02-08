from flask import Blueprint, render_template
from catapi.api import GetRandomCatImage

products_bp = Blueprint('catapi_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

@products_bp.route("/")
def home():
    random_cat = GetRandomCatImage()
    return render_template("index.html", cat=random_cat)