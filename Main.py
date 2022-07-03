from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet

SENDER = 'sender'
RECIEVER = 'reciever'
AMOUNT = 2
TYPE = 'TRANSFER'

if __name__ == '__main__':
    wallet = Wallet()
    pool = TransactionPool()
    
    transaction = wallet.create_transaction(RECIEVER,AMOUNT,TYPE)
    
    if pool.is_transaction_exists(transaction) == False:
        pool.add_transaction(transaction)
        
    if pool.is_transaction_exists(transaction) == False:
        pool.add_transaction(transaction)
        
    print(pool.transactions)
    