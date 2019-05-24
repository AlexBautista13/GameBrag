from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

CORS(app)
db = SQLAlchemy(app)


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


class Like(db.Model):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer(), nullable=False, unique=False)

    def __init__(self, amount):
        self.amount = amount


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


@app.route('/post', methods=["POST"])
def image_post():
    if request.content_type == "application/json":
        post_data = request.get_json()
        title = post_data.get('title')
        description = post_data.get('description')
        url = post_data.get('url')
        adding = Images(title, description, url)
        db.session.add(adding)
        db.session.commit()
        return jsonify("success")
    return jsonify("error")

@app.route("/userfeed/<id>", methods=["GET"])
def get_images(id):
    all_images = db.session.query(Images.id, Images.title, Images.url, Images.description).all()
    return jsonify(all_images)
    

    # image_post = Guide(title, description, url)

    # db.session.add(image_post)
    # db.session.commit()

    # guide = Guide.query.get(image_post.id)

    # return guide_schema.jsonify(guide)



if __name__ == "__main__":
    app.debug = True
    app.run()