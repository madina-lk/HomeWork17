
from marshmallow import Schema, fields


#  Описание модели в виде класса схемы

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()