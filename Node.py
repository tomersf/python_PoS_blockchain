from Blockchain import Blockchain
from TransactionPool import TransactionPool
from Wallet import Wallet
from SocketCommunication import SocketCommunication

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
        
    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket_communication()