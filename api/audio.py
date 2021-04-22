# flask packages
from flask import Response, request
from flask_restful import Resource

# local packages
from database.models import Song

# external packages
from json import dumps


class CreateAudioApi(Resource):
    def post(self):
        body = request.get_json()
        audio_file_type = body['audioFileType']
        audio_file_type = audio_file_type.strip().lower()
        audio_file_metadata = body['audioFileMetadata']

        if audio_file_type == 'song':
            audio = Song(**audio_file_metadata).save()

        resp = {
            'id': audio.ID,
            'message': 'Successfully created!',
        }
        return Response(dumps(resp), mimetype="application/json", status=200)


class AudiosApi(Resource):
    def get(self, audio_file_type):
        audio_file_type = audio_file_type.strip().lower()
        if audio_file_type == 'song':
            audio_files = Song.objects().to_json()

        return Response(audio_files, mimetype="application/json", status=200)


class AudioApi(Resource):
    def get(self, audio_file_type, audio_file_id):
        audio_file_type = audio_file_type.strip().lower()
        if audio_file_type == 'song':
            audio = Song.objects.get(ID=audio_file_id).to_json()

        return Response(audio, mimetype="application/json", status=200)
