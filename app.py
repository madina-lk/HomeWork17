# app.py

from flask import Flask
from flask_restx import Api
from setup_db import db

from ns_views.movie_view import movie_ns
from ns_views.director_view import director_ns
from ns_views.genre_view import genre_ns


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    create_api(app)

    return app


def create_api(app):
    db.init_app(app)
    api = Api(app)
    app.app_context().push()

    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)

    create_table(app, db)


def create_table(app, db):
    with app.app_context():
        db.create_all()


app = create_app()
app.debug = True

if __name__ == "__main__":
    app.run(debug=True)
