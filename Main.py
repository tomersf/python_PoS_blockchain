from BlockchainUtils import BlockchainUtils
from TransactionPool import TransactionPool
from Wallet import Wallet
from Block import Block
from Blockchain import Blockchain
from AccountModel import AccountModel
from constants import LAST_INDEX
import pprint

SENDER = 'sender'
RECIEVER = 'reciever'
AMOUNT = 2
TYPE = 'TRANSFER'

if __name__ == '__main__':
    wallet = Wallet()
    accountModel = AccountModel()
    accountModel.update_balance(wallet.get_public_key_string(),10)
    accountModel.update_balance(wallet.get_public_key_string(),-5)
    print(accountModel.balances)
    pool = TransactionPool()

    transaction = wallet.create_transaction(RECIEVER, AMOUNT, TYPE)

    if pool.is_transaction_exists(transaction) is False:
        pool.add_transaction(transaction)

    blockchain = Blockchain()
    last_hash = BlockchainUtils.hash(blockchain.blocks[LAST_INDEX].payload()).hexdigest()
    block_count = blockchain.blocks[LAST_INDEX].block_count + 1
    block = wallet.create_block(pool.transactions, last_hash, block_count)
    
    if not blockchain.last_block_hash_validity(block):
        print('last block hash is not valid!')
    
    if not blockchain.block_count_validity(block):
        print('Block count is not valid!')
    
    if blockchain.last_block_hash_validity(block) and blockchain.block_count_validity(block):
        blockchain.add_block(block)
        
    pprint.pprint(blockchain.to_json())
