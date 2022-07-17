from typing import List
from Blockchain import Blockchain
import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI

class Node():
    """Implementation of the node class
    """ 
       
    def __init__(self, ip: str, port: int) -> None:
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        self.api : NodeAPI = None
        
    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket_communication()
        
    def startAPI(self, port:int) -> None:
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(port)
        
    def transactions_in_txs_pool(self) -> List[Transaction.Transaction]:
        return self.transaction_pool.transactions