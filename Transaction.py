from __future__ import annotations
import uuid
import time
import copy

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
    
    def to_json(self):
        return self.__dict__
    
    def sign(self, signature):
        self.signature = signature
        
    def payload(self):
        json_representation = copy.deepcopy(self.to_json())
        json_representation['signature'] = ''
        return json_representation
        
    def equals(self, transaction: Transaction) -> bool:
        if self.id == transaction.id:
            return True
        return False
        
        