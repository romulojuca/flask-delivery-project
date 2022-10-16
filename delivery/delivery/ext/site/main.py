from flask import Blueprint, current_app, render_template, redirect, request
from delivery.ext.auth.form import UserForm
from delivery.ext.auth.controller import create_user, save_user_foto


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")#retorna um objto que contem uma string e criada apartir de um template


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()

    if form.validate_on_submit():
        create_user(
            email=form.email.data,
            password=form.password.data
        )
        foto = request.files.get('foto')
        if foto:
            save_user_foto(
                foto.filename,
                foto
            )
        # forçar login
        return redirect("/")


    return render_template("userform.html", form=form)



@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")
