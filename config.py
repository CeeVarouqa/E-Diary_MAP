"""Flask configuration."""
from os import path

basedir = path.abspath(path.dirname(__file__))

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = 'GDtfDCFYjD'
