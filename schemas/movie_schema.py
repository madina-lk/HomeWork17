
from marshmallow import Schema, fields
from schemas.genre_schema import GenreSchema
from schemas.director_schema import DirectorSchema


#  Описание модели в виде класса схемы

class MovieSchema(Schema):

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    genre = fields.Nested(GenreSchema)
    director_id = fields.Int()
    director = fields.Nested(DirectorSchema)

