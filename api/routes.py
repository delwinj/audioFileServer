# local packages
from .audio import CreateAudioApi


def initialize_routes(api):
    api.add_resource(CreateAudioApi, '/api/audios/')
