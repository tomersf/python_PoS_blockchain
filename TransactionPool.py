
from typing import List
from Transaction import Transaction

class TransactionPool():
    def __init__(self) -> None:
        self.transactions : List[Transaction] = []
        
    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        
    def is_transaction_exists(self, transaction: Transaction) -> bool:
        for pool_transaction in self.transactions:
            if pool_transaction.equals(transaction):
                return True
        return False
            
        