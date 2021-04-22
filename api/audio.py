# flask packages
from flask import Response, request
from flask_restful import Resource

# local packages
from database.models import Song, Podcast, Audiobook
from tools.manipulate_data import remove_metadata

# external packages
from json import dumps


def create_audio_obj(audio_file_type):
    audio_file_type = audio_file_type.strip().lower()
    if audio_file_type == 'song':
        return Song
    if audio_file_type == 'podcast':
        return Podcast
    if audio_file_type == 'audiobook':
        return Audiobook
    return None


class CreateAudioApi(Resource):
    def post(self):
        body = request.get_json()
        audio_file_type = body['audioFileType']
        audio_file_metadata = body['audioFileMetadata']
        Audio = create_audio_obj(audio_file_type)
        audio = Audio(**audio_file_metadata).save()

        resp = {
            'id': audio.ID,
            'message': 'Successfully created!',
        }
        return Response(dumps(resp), mimetype="application/json", status=200)


class AudiosApi(Resource):
    def get(self, audio_file_type):
        Audio = create_audio_obj(audio_file_type)
        audio_files = Audio.objects().to_json()
        resp = remove_metadata(audio_files)

        return Response(resp, mimetype="application/json", status=200)


class AudioApi(Resource):
    def get(self, audio_file_type, audio_file_id):
        Audio = create_audio_obj(audio_file_type)
        audio = Audio.objects.get(ID=audio_file_id).to_json()
        resp = remove_metadata(audio)

        return Response(resp, mimetype="application/json", status=200)

    def put(self, audio_file_type, audio_file_id):
        body = request.get_json()
        Audio = create_audio_obj(audio_file_type)
        Audio.objects.get(ID=audio_file_id).update(**body)

        resp = {
            'id': audio_file_id,
            'message': 'Successfully updated!',
        }
        return Response(dumps(resp), mimetype="application/json", status=200)

    def delete(self, audio_file_type, audio_file_id):
        Audio = create_audio_obj(audio_file_type)
        Audio.objects.get(ID=audio_file_id).delete()

        resp = {
            'id': audio_file_id,
            'message': 'Successfully deleted!',
        }
        return Response(dumps(resp), mimetype="application/json", status=200)