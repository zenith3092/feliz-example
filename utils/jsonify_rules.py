import datetime
import json
from enum import Enum

from bson import ObjectId

TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

def customized_jsonify(obj, default_jsonify):
    if isinstance(obj, datetime.datetime):
        return obj.strftime(TIME_FORMAT)
    elif isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, Enum):
        return obj.value
    else:
        return default_jsonify(obj)

def _customized_json_default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime(TIME_FORMAT)
    elif isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, Enum):
        return obj.value
    else:
        return None

def _customized_object_hook(d, datetime_keys=[], object_id_keys=[]):
    if isinstance(d, dict):
        for key, value in d.items():
            if key in datetime_keys:
                d[key] = datetime.datetime.strptime(value, TIME_FORMAT)
            elif key in object_id_keys:
                d[key] = ObjectId(value)
    elif isinstance(d, list):
        for i in range(len(d)):
            d[i] = _customized_object_hook(d[i], datetime_keys, object_id_keys)
    return d

def json_stringify(obj):
    """
    This function converts the object to a JSON string, supporting to handle datetime.datetime, bson.ObjectId, and Enum objects.

    Args:
        - obj (object): Object to convert.
    
    Returns:
        - str: JSON string.
    """
    return json.dumps(obj, default=_customized_json_default)

def json_parse(s, datetime_keys=[], object_id_keys=[]):
    """
    This function converts the JSON string to an object, supporting to handle datetime.datetime, bson.ObjectId.

    Args:
        - s (str): JSON string.
        - datetime_keys (list): List of keys that need to convert to datetime.datetime.
        - object_id_keys (list): List of keys that need to convert to bson.ObjectId.
    
    Returns:
        - dict: Parsed object.
    """
    return json.loads(s, object_hook=lambda d: _customized_object_hook(d, datetime_keys, object_id_keys))