from typing import List
from Block import Block
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from constants import LAST_INDEX, TRANSFER_OPERATIONS
from AccountModel import AccountModel
from pprint import pprint


class Blockchain():
    """Blockchain class implementation
    """
    
    def __init__(self) -> None:
        self.blocks : List[Block] = [Block.genesis()]
        self.account_model = AccountModel()
        
    def add_block(self, block: Block) -> None:
        self.execute_transactions(block.transactions)
        self.blocks.append(block)
        
    def to_json(self) -> dict:
        data = {}
        json_blocks = []
        for block in self.blocks:
            json_blocks.append(block.to_json())
        data['blocks'] = json_blocks
        return data
    
    def block_count_validity(self, block:Block) -> bool:
        if self.blocks[LAST_INDEX].block_count == block.block_count - 1:
            return True
        return False
    
    def last_block_hash_validity(self, block:Block) -> bool:
        latest_blockchain_block_hash = BlockchainUtils.hash(self.blocks[LAST_INDEX].payload()).hexdigest()
        if latest_blockchain_block_hash == block.last_hash:
            return True
        return False
    
    def transaction_covered(self, transaction: Transaction) -> bool:
        if transaction.transaction_type == TRANSFER_OPERATIONS.EXCHANGE:
            return True
        sender_balance = self.account_model.get_balance(transaction.sender_pub_key)
        if sender_balance >= transaction.amount:
            return True
        return False
    
    def get_covered_transaction_set(self, transactions: List[Transaction]) -> List[Transaction]:
        covered_transactions = []
        for transaction in transactions:
            if self.transaction_covered(transaction):
                covered_transactions.append(transaction)
            else:
                print('The following transaction is not covered by the sender!')
                pprint(transaction.to_json())
                
        return covered_transactions
    
    def execute_transaction(self, transaction: Transaction) -> None:
        sender = transaction.sender_pub_key
        reciever = transaction.reciever_pub_key
        amount = transaction.amount
        
        self.account_model.update_balance(sender, -amount)
        self.account_model.update_balance(reciever, amount)
        
    def execute_transactions(self, transactions: List[Transaction]) -> None:
        for transaction in transactions:
            self.execute_transaction(transaction)
            
        
            