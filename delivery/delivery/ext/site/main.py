from flask import render_template
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("index.html")#retorna um objto que contem uma string e criada apartir de um template


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")
