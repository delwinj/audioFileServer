# local packages
from api.audio import CreateAudioApi, AudiosApi, AudioApi


def initialize_routes(api):
    api.add_resource(CreateAudioApi, '/api/audios/')
    api.add_resource(AudiosApi, '/api/audios/<audio_file_type>/')
    api.add_resource(AudioApi, '/api/audios/<audio_file_type>/<audio_file_id>/')
