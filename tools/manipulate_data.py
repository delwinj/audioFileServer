# internal packages
from api.errors import DateInvalidError

# external packages
from json import loads, dumps
from datetime import datetime, timezone, timedelta


def del_metadata(json_data):
    if '_cls' in json_data:
        del json_data['_cls']
    if '_id' in json_data:
        del json_data['_id']


def remove_metadata(json_str):
    json_data = loads(json_str)

    if isinstance(json_data, dict):
        del_metadata(json_data)
    elif isinstance(json_data, list):
        for data in json_data:
            del_metadata(data)

    return dumps(json_data)


def parse_date(dt_str):
    formats = (
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S%z",
    )
    for fmt in formats:
        try:
            d1 = datetime.strptime(dt_str, fmt)
            d2 = datetime.utcnow()
            if d2.astimezone(tz=timezone.utc) - d1.astimezone(tz=timezone.utc) > timedelta(seconds=60):
                raise DateInvalidError
            return d1.astimezone(tz=timezone.utc)
        except ValueError:
            pass
    raise DateInvalidError
