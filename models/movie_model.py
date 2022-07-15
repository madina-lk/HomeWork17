from setup_db import db


class MovieModel(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")

    def __init__(
        self,
        id,
        title,
        description,
        trailer,
        year,
        rating,
        genre_id,
        genre,
        director_id,
        director,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.trailer = trailer
        self.year = year
        self.rating = rating
        self.genre_id = genre_id
        self.genre = genre
        self.director_id = director_id
        self.director = director
