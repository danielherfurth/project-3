"""Flask config."""
from os import environ, path
# from dotenv import load_dotenv
#
# BASE_DIR = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(BASE_DIR, '.env'))


class Config:
    """Flask configuration variables."""

    # General Config
    FLASK_APP = 'app'
    FLASK_ENV = "development"
    # SECRET_KEY = environ.get('SECRET_KEY')
    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')