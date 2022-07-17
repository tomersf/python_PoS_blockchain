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

if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    api_port = int(sys.argv[3])

    node = Node(ip, port)
    node.start_p2p()
    node.startAPI(api_port)
    
