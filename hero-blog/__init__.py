from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('hero-blog.settings')

db = SQLAlchemy(app)