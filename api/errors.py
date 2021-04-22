class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class ValidationError(Exception):
    pass


class AudioExistsError(Exception):
    pass


class UpdatingAudioError(Exception):
    pass


class DeletingAudioError(Exception):
    pass


class AudioDoesNotExistError(Exception):
    pass


class AudioTypeInvalidError(Exception):
    pass


class DateFormatInvalidError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "ValidationError": {
        "message": "Required field fails validation",
        "status": 400
    },
    "AudioExistsError": {
        "message": "Audio file with given id already exists",
        "status": 400
    },
    "UpdatingAudioError": {
        "message": "Updating movie added by other is forbidden",
        "status": 400
    },
    "DeletingAudioError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 400
    },
    "AudioDoesNotExistError": {
        "message": "Movie with given id doesn't exists",
        "status": 400
    },
    "AudioTypeInvalidError": {
        "message": "Audio type provided is invalid",
        "status": 400
    },
    "DateFormatInvalidError": {
        "message": "Updated time provided in an invalid format",
        "status": 400
    },
}
