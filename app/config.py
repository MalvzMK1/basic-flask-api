from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
  ENVIRONMENT = environ.get('ENVIRONMENT')
  HOST = environ.get('HOST')
  PORT = environ.get('PORT')
  SQLALCHEMY_TRACK_MODIFICATIONS = True if environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') == '1' else False
  SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')