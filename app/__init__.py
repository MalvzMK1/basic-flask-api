import json
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from app.config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app() -> Flask:
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  migrate.init_app(app=app, db=db)

  return app