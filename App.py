from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

CORS(app)
db = SQLAlchemy(app)

# Post image
# Like image
# Save image
# View album
# Profile Desc
# Profile Edit
# Delete image
# Delete profile
# Admin page with privaleges
# Categories
# Game Titles



if __name__ == "__main__":
    app.debug = True
    app.run()