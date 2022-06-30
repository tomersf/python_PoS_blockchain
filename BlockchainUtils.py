from typing import Any
from Crypto.Hash import SHA256
import json

class BlockchainUtils():
    """Implement utils for the project
    """
    
    @staticmethod
    def hash(data: Any):
        data_string = json.dumps(data)
        data_bytes = data_string.encode('utf-8')
        data_hash = SHA256.new(data_bytes)
        return data_hash
        