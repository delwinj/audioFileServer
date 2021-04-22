# local packages
from .db import db


class AudioFile(db.Document):
    ID = db.IntField(required=True, unique=True)
    duration = db.IntField(required=True, min_value=0)
    uploaded_time = db.DateTimeField(required=True)

    meta = {'allow_inheritance': True}


class Song(AudioFile):
    name = db.StringField(required=True, max_length=100)


class Podcast(AudioFile):
    name = db.StringField(required=True, max_length=100)
    host = db.StringField(required=True, max_length=100)
    participants = db.ListField(db.StringField(max_length=100), max_length=10)


class Audiobook(AudioFile):
    title = db.StringField(required=True, max_length=100)
    author = db.StringField(required=True, max_length=100)
    narrator = db.StringField(required=True, max_length=100)
