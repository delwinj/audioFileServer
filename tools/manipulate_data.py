# external packages
from json import loads, dumps


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
