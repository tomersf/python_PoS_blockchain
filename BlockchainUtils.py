import json
import jsonpickle
from typing import Any
from Crypto.Hash import SHA256


class BlockchainUtils():
    """Implement utils for the project
    """

    @staticmethod
    def hash(data: Any):
        data_string = json.dumps(data)
        data_bytes = data_string.encode('utf-8')
        data_hash = SHA256.new(data_bytes)
        return data_hash

    @staticmethod
    def encode(object_to_encode) -> dict:
        return jsonpickle.encode(object_to_encode, unpicklable=True)

    @staticmethod
    def decode(encoded_object):
        return jsonpickle.decode(encoded_object)
