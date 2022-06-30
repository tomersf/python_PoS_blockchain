import uuid
import time

class Transaction():
    """Implementation of the transaction class
    """    

    def __init__(self,sender_pub_key,reciever_pub_key, amount,transaction_type) -> None:
        self.sender_pub_key = sender_pub_key
        self.reciever_pub_key = reciever_pub_key
        self.amount = amount
        self.transaction_type = transaction_type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''
    
    def toJson(self):
        return self.__dict__
    
    def sign(self, signature):
        self.signature = signature
        