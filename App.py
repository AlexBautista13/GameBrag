from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
CORS(app)
db = SQLAlchemy(app)


class Bio(db.Model):
    __tablename__ = "bios"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))

    def __init__(self, description):
        self.description = description

class GameTitles(db.Model):
    __tablename__ = "gametitles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title

class GameCategory(db.Model):
    __tablename__ = "gamecategory"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False, unique=True)

    def __init__(self, category):
        self.category = category


@app.route('/create-bio', methods=["POST"])
def bio_create():
    if request.content_type == "application/json":
        post_data = request.get_json()
        description = post_data.get('description')
        adding = Bio(description)
        db.session.add(adding)
        db.session.commit()
        return jsonify("success")
    return jsonify("error")
@app.route("/bio/<id>", methods=["GET"])
def get_bio(id):
    all_bio = db.session.query(Bio.id, Bio.description).all()
    return jsonify(all_bio)


@app.route('/create-gametitle', methods=["POST"])
def gametitle_create():
    if request.content_type == "application/json":
        post_data = request.get_json()
        title = post_data.get('title')
        adding = GameTitles(title)
        db.session.add(adding)
        db.session.commit()
        return jsonify("success")
    return jsonify("error")
@app.route("/game-title/<id>", methods=["GET"])
def get_gametitle(id):
    all_gametitle = db.session.query(GameTitles.id, GameTitles.title).all()
    return jsonify(all_gametitle)


@app.route('/create-gamecategory', methods=["POST"])
def gamecategory_create():
    if request.content_type == "application/json":
        post_data = request.get_json()
        category = post_data.get('category')
        adding = GameCategory(category)
        db.session.add(adding)
        db.session.commit()
        return jsonify("success")
    return jsonify("error")
@app.route("/gamecategory/<id>", methods=["GET"])
def get_gamecategory(id):
    all_gamecategory = db.session.query(GameCategory.id, GameCategory.category).all()
    return jsonify(all_gamecategory)





if __name__ == "__main__":
    app.debug = True
    app.run()