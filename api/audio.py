# flask packages
from flask_restful import Resource
from flask import Response, request
from mongoengine import NotUniqueError, FieldDoesNotExist, DoesNotExist, ValidationError

# local packages
from database.models import Song, Podcast, Audiobook
from tools.manipulate_data import remove_metadata, parse_date
from api.errors import AudioExistsError, SchemaValidationError, InternalServerError, DateFormatInvalidError, \
    AudioTypeInvalidError, AudioDoesNotExistError, DeletingAudioError, UpdatingAudioError

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
    raise AudioTypeInvalidError


class CreateAudioApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            audio_file_type = body['audioFileType']
            audio_file_metadata = body['audioFileMetadata']
            audio_file_metadata['uploaded_time'] = parse_date(audio_file_metadata['uploaded_time'])

            Audio = create_audio_obj(audio_file_type)
            audio = Audio(**audio_file_metadata).save()

            resp = {
                'id': audio.ID,
                'message': 'Successfully created!',
            }
            return Response(dumps(resp), mimetype="application/json", status=200)
        except FieldDoesNotExist:
            raise SchemaValidationError
        except ValidationError:
            raise ValidationError
        except NotUniqueError:
            raise AudioExistsError
        except AudioTypeInvalidError:
            raise AudioTypeInvalidError
        except DateFormatInvalidError:
            raise DateFormatInvalidError
        except Exception as e:
            raise InternalServerError


class AudiosApi(Resource):
    def get(self, audio_file_type):
        try:
            Audio = create_audio_obj(audio_file_type)
            audio_files = Audio.objects().to_json()
            resp = remove_metadata(audio_files)

            return Response(resp, mimetype="application/json", status=200)
        except AudioTypeInvalidError:
            raise AudioTypeInvalidError
        except Exception as e:
            raise InternalServerError


class AudioApi(Resource):
    def get(self, audio_file_type, audio_file_id):
        try:
            Audio = create_audio_obj(audio_file_type)
            audio = Audio.objects.get(ID=audio_file_id).to_json()
            resp = remove_metadata(audio)

            return Response(resp, mimetype="application/json", status=200)
        except ValidationError:
            raise ValidationError
        except DoesNotExist:
            raise AudioDoesNotExistError
        except AudioTypeInvalidError:
            raise AudioTypeInvalidError
        except Exception as e:
            raise InternalServerError

    def put(self, audio_file_type, audio_file_id):
        try:
            body = request.get_json()
            body['uploaded_time'] = parse_date(body['uploaded_time'])
            Audio = create_audio_obj(audio_file_type)
            Audio.objects.get(ID=audio_file_id).update(**body)

            resp = {
                'id': audio_file_id,
                'message': 'Successfully updated!',
            }
            return Response(dumps(resp), mimetype="application/json", status=200)
        except FieldDoesNotExist:
            raise SchemaValidationError
        except ValidationError:
            raise ValidationError
        except DoesNotExist:
            raise UpdatingAudioError
        except AudioTypeInvalidError:
            raise AudioTypeInvalidError
        except DateFormatInvalidError:
            raise DateFormatInvalidError
        except Exception as e:
            print(e)
            raise InternalServerError

    def delete(self, audio_file_type, audio_file_id):
        try:
            Audio = create_audio_obj(audio_file_type)
            Audio.objects.get(ID=audio_file_id).delete()

            resp = {
                'id': audio_file_id,
                'message': 'Successfully deleted!',
            }
            return Response(dumps(resp), mimetype="application/json", status=200)
        except ValidationError:
            raise ValidationError
        except DoesNotExist:
            raise DeletingAudioError
        except AudioTypeInvalidError:
            raise AudioTypeInvalidError
        except Exception as e:
            raise InternalServerError
