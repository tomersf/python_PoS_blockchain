import pprint
import sys
from BlockchainUtils import BlockchainUtils
from Node import Node
from TransactionPool import TransactionPool
from Wallet import Wallet
from Block import Block
from Blockchain import Blockchain
from AccountModel import AccountModel
from constants import LAST_INDEX, TRANSFER_OPERATIONS


SENDER = 'sender'
RECIEVER = 'reciever'
AMOUNT = 2
TYPE = 'TRANSFER'

if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    node = Node(ip, port)
    node.start_p2p()
    
