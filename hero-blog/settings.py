import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
CSRF_ENABLED = True
SECRET_KEY = 'sadjquwyehsjdccahskhdwuiqw23213^2sdahj$sakj'

SQLALCHEMY_TRACK_MODIFICATIONS = True

try:
    from .local_settings import *
except ImportError:
    pass