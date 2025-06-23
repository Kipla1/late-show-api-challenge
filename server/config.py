import os
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@localhost:5432/late_show_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '1234' # Change this in production
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()