import json
from typing import List
from p2pnetwork.node import Node
from BlockchainUtils import BlockchainUtils
from Message import Message

from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
from constants import FIRST_NODE_PORT, LOCAL_HOST, MESSAGE_TYPES


class SocketCommunication(Node):
    """Class for providing the P2P communication
    """

    def __init__(self, ip, port) -> None:
        super(SocketCommunication, self).__init__(ip, port, None)
        self.peers: List[SocketConnector] = []
        self.peer_discovery_handler = PeerDiscoveryHandler(self)
        self.socket_connector = SocketConnector(ip, port)

    def connect_to_first_node(self) -> None:
        if self.socket_connector.port != FIRST_NODE_PORT:
            self.connect_with_node(LOCAL_HOST, FIRST_NODE_PORT)

    def start_socket_communication(self, peer_node) -> None:
        self.node = peer_node
        self.start()
        self.peer_discovery_handler.start()
        self.connect_to_first_node()

    def inbound_node_connected(self, connected_node) -> None:
        self.peer_discovery_handler.handshake(connected_node)

    def outbound_node_connected(self, connected_node) -> None:
        self.peer_discovery_handler.handshake(connected_node)

    def node_message(self, connected_node, incoming_message) -> None:
        message: Message = BlockchainUtils.decode(json.dumps(incoming_message))
        if message.message_type == MESSAGE_TYPES.DISCOVERY:
            self.peer_discovery_handler.handle_meesage(message)
        elif message.message_type == MESSAGE_TYPES.TRANSACTION:
            transaction = message.data
            self.node.handle_transaction(transaction)

    def send(self, receiver, message) -> None:
        self.send_to_node(receiver, message)

    def broadcast(self, message) -> None:
        self.send_to_nodes(message)
