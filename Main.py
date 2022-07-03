from TransactionPool import TransactionPool
from Wallet import Wallet
from Block import Block
import pprint

SENDER = 'sender'
RECIEVER = 'reciever'
AMOUNT = 2
TYPE = 'TRANSFER'

if __name__ == '__main__':
    wallet = Wallet()
    pool = TransactionPool()
    
    transaction = wallet.create_transaction(RECIEVER,AMOUNT,TYPE)
    
    if pool.is_transaction_exists(transaction) is False:
        pool.add_transaction(transaction)
        
    block = wallet.create_block(pool.transactions,'last_hash',1)
    signature_validity = Wallet.validate_signature(block.payload(),
                                                   block.signature, wallet.get_public_key_string())
    print(signature_validity)
    
    