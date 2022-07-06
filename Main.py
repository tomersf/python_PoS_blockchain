from BlockchainUtils import BlockchainUtils
from TransactionPool import TransactionPool
from Wallet import Wallet
from Block import Block
from Blockchain import Blockchain
from AccountModel import AccountModel
from constants import LAST_INDEX, TRANSFER_OPERATIONS
import pprint

SENDER = 'sender'
RECIEVER = 'reciever'
AMOUNT = 2
TYPE = 'TRANSFER'

if __name__ == '__main__':
    blockchain = Blockchain()
    pool = TransactionPool()
    
    alice = Wallet()
    bob = Wallet()
    
    transaction = alice.create_transaction(bob.get_public_key_string(),5,
                                           TRANSFER_OPERATIONS.TRANSFER)
    if not pool.is_transaction_exists(transaction):
        pool.add_transaction(transaction)
    
    covered_transaction = blockchain.get_covered_transaction_set(pool.transactions)
    print(covered_transaction)
    
