from http.client import HTTPException


class InternalServerError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class ValidationError(HTTPException):
    pass


class AudioExistsError(HTTPException):
    pass


class AudioDoesNotExistError(HTTPException):
    status_code = 400


class AudioTypeInvalidError(HTTPException):
    pass


class DateInvalidError(HTTPException):
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
    "AudioDoesNotExistError": {
        "message": "Audio with given id doesn't exists",
        "status": 400
    },
    "AudioTypeInvalidError": {
        "message": "Audio type provided is invalid",
        "status": 400
    },
    "DateInvalidError": {
        "message": "Updated time provided in invalid or in an invalid format",
        "status": 400
    },
}
