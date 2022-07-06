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
    exchange = Wallet()
    forger = Wallet()
    
    exchange_transaction = exchange.create_transaction(alice.get_public_key_string(), 10,
                                                       TRANSFER_OPERATIONS.EXCHANGE)
    
    if not pool.is_transaction_exists(exchange_transaction):
        pool.add_transaction(exchange_transaction)
    
    covered_transactions = blockchain.get_covered_transaction_set(pool.transactions)
    block_one = forger.create_block(covered_transactions,
                                    BlockchainUtils.hash(blockchain.blocks[LAST_INDEX].payload()).hexdigest(),
                                    blockchain.blocks[LAST_INDEX].block_count + 1)
    blockchain.add_block(block_one)
    pool.remove_from_pool(block_one.transactions)
    
    transaction = alice.create_transaction(bob.get_public_key_string(),5,
                                           TRANSFER_OPERATIONS.TRANSFER)
    if not pool.is_transaction_exists(transaction):
        pool.add_transaction(transaction)

    covered_transactions = blockchain.get_covered_transaction_set(pool.transactions)
    block_two = forger.create_block(covered_transactions,
                                    BlockchainUtils.hash(blockchain.blocks[LAST_INDEX].payload()).hexdigest(),
                                    blockchain.blocks[LAST_INDEX].block_count + 1)
    blockchain.add_block(block_two)
    pool.remove_from_pool(block_two.transactions)
    
    pprint.pprint(blockchain.to_json())
    
