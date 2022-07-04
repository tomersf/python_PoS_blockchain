from typing import List
from Block import Block
from BlockchainUtils import BlockchainUtils
from constants import LAST_INDEX


class Blockchain():
    """Blockchain class implementation
    """
    
    def __init__(self) -> None:
        self.blocks : List[Block] = [Block.genesis()]
        
    def add_block(self, block: Block) -> None:
        self.blocks.append(block)
        
    def to_json(self):
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
    
    def last_block_hash_validity(self, block:Block):
        latest_blockchain_block_hash = BlockchainUtils.hash(self.blocks[LAST_INDEX].payload()).hexdigest()
        if latest_blockchain_block_hash == block.last_hash:
            return True
        return False
            