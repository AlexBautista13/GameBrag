from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

CORS(app)
db = SQLAlchemy(app)


class Images(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    url = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(50))

    def __init__(self, url, description, title):
        self.title = title
        self.url = url
        self.description = description


class ProfileImage(db.Model):
    __tablename__ = "profileImages"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=False)

    def __init__(self, url):
        self.url = url


class Bio(db.Model):
    __tablename__ = "bios"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))

    def __init__(self, description):
        self.description = description


class UserName(db.Model):
    __tablename__ = "usernames"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)

    def __init__(self, username):
        self.username = username


class Like(db.Model):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.int(), nullable=False, unique=False)

    def __init__(self, amount):
        self.amount = amount


class GameTitles(db.Model):
    __tablename__ = "gametitles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(20), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title


class GameCategory(db.Model):
    __tablename__ = "gamecategory"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.string(20), nullable=False, unique=True)

    def __init__(self, category):
        self.category = category

# Post image
# Save image
# View album
# Profile Edit
# Delete image
# Delete profile
# Admin page with privaleges



if __name__ == "__main__":
    app.debug = True
    app.run()