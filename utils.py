from setup_db import db
from models.movie_model import MovieModel
from models.director_model import Director


def get_all_movies():
    result = []
    for row in MovieModel.query.all():
        result.append(row.to_json())

    return result


def get_all_directors():
    result = []
    for row in Director.query.all():
        result.append(row.to_json())

    return result


def get_all_genre():
    result = []
    for row in Director.query.all():
        result.append(row.to_json())

    return result