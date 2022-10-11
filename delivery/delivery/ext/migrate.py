from flask_migrate import Migrate
from delivery.ext.db import db
from delivery.ext.db import models
from delivery.ext.auth import models


migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
