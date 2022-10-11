from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla import filters
from flask_admin.actions import action
from delivery.ext import db
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash, Markup


def format_user(self, request, user, *args):
    return Markup (f'<b>{user.email.split("@")[0]}</b>')#negrito


class UserAdmin(ModelView):
    """Interface admin de user"""

    column_formatters = {"email": format_user}
    column_list = {"email", "admin"}
    column_searchable_list = ["email"]
    column_filters = [
        "email", 
        "admin",
        filters.FilterLike(
            User.email,
            "Dominio",
            options=(("gmail", "Gmail"), ("uol", "Uol"))
        )
    ]


    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toggle_admin',
        'Togle admin status',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} usuarios alterados com sucesso!")

    @action(
        'send_email',
        'Send email to all users',
        'Are you sure?'
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a msg do email
        # 2) enviar o email
        flash(f" {len(users)} emails enviados!", "success")
