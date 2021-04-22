# local packages
from .db import db


class AudioFile(db.Document):
    ID = db.IntField(required=True, unique=True)
    duration = db.IntField(required=True, min_value=0)

    meta = {'allow_inheritance': True}


class Song(AudioFile):
    name = db.StringField(required=True, max_length=100)
