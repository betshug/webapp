from unicodedata import category
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate=Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    category = db.Column(db.String(30))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    availability = db.Column(db.Boolean)


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),unique=True,nullable=False)
    name=db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    # position = db.Column(db.String(50), nullable=False)
    # phone = db.Column(db.String(50), nullable=False)
    # dateofbirthday = db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
        return "<User %r>"% self.name