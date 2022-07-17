from typing import List
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from Message import Message
import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from constants import MESSAGE_TYPES


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
        self.api: NodeAPI = None

    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket_communication(self)

    def startAPI(self, port: int) -> None:
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(port)

    def transactions_in_txs_pool(self) -> List[Transaction.Transaction]:
        return self.transaction_pool.transactions

    def handle_transaction(self, transaction: Transaction.Transaction):
        data = transaction.payload()
        signature = transaction.signature
        signer_public_key = transaction.sender_pub_key
        signature_validity = Wallet.validate_signature(
            data, signature, signer_public_key)
        transaction_exists = self.transaction_pool.is_transaction_exists(
            transaction)
        if not transaction_exists and signature_validity:
            self.transaction_pool.add_transaction(transaction)
            message = Message(self.p2p.socket_connector,
                              MESSAGE_TYPES.TRANSACTION, transaction)
            encoded_message = BlockchainUtils.encode(message)
            self.p2p.broadcast(encoded_message)
