
from marshmallow import Schema, fields


#  Описание модели в виде класса схемы

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
