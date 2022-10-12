import click
from delivery.ext.db import db
from delivery.ext.db import models

#criar esses COMANDOS usando os decorators
def init_app(app):
    
    @app.cli.command()
    def create_db():
        """Este comando inicialisa o db"""
        db.create_all()


    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate
        click.echo("Lista de pedidos")
