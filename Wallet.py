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