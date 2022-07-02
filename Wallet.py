from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils

MODULO = 2048

class Wallet():
    """Wallet class
    """
    def __init__(self) -> None:
        self.key_pair = RSA.generate(MODULO)
        
    def sign(self, data) -> str:
        data_hash = BlockchainUtils.hash(data)
        signature_scheme = PKCS1_v1_5.new(self.key_pair)
        signature = signature_scheme.sign(data_hash)
        return signature.hex()
    
    @staticmethod
    def validate_signature(data, signature, public_key_string) -> bool:
        signature = bytes.fromhex(signature)
        data_hash = BlockchainUtils.hash(data)
        public_key = RSA.import_key(public_key_string)
        signature_scheme_object = PKCS1_v1_5.new(public_key)
        signature_validity = signature_scheme_object.verify(data_hash,signature)
        return signature_validity
    
    def get_public_key_string(self) -> str:
        public_key_str = self.key_pair.publickey().export_key('PEM').decode('utf-8')
        return public_key_str