import threading, time
from BlockchainUtils import BlockchainUtils

from constants import MESSAGE_TYPES
from Message import Message
import SocketCommunication

class PeerDiscoveryHandler():
    """Class implemenation for discovering nodes
    """
    
    def __init__(self, node: SocketCommunication) -> None:
        self.socket_communication : SocketCommunication.SocketCommunication = node
        
    def start(self) -> None:
        status_thread = threading.Thread(target=self.status, args=())
        status_thread.start()
        discovery_thread = threading.Thread(target=self.discovery, args=())
        discovery_thread.start()
        
    def status(self) -> None:
        while True:
            print('Current Connections:')
            for peer in self.socket_communication.peers:
                print(str(peer.ip) + ':' + str(peer.port))
            time.sleep(10)
        
    def discovery(self) -> None:
        while True:
            handshake_msg = self.handshake_message()
            self.socket_communication.broadcast(handshake_msg)
            time.sleep(10)
            
    def handshake(self, connect_node) -> None:
        handshake_message = self.handshake_message()
        self.socket_communication.send(connect_node, handshake_message)
        
    def handshake_message(self) -> None:
        connector = self.socket_communication.socket_connector
        peers = self.socket_communication.peers
        data = peers
        message_type = MESSAGE_TYPES.DISCOVERY
        message = Message(connector, message_type, data)
        encoded_message = BlockchainUtils.encode(message)
        return encoded_message
    
    def handle_meesage(self, message: Message) -> None:
        peer_socket_connector = message.sender_connector
        peers_peer_list = message.data
        new_peer = True
        for peer in self.socket_communication.peers:
            if peer.equals(peer_socket_connector):
                new_peer = False
        if new_peer:
            self.socket_communication.peers.append(peer_socket_connector)
        
        for peers_peer in peers_peer_list:
            peer_known = False
            
            for peer in self.socket_communication.peers:
                if peer.equals(peers_peer):
                    peer_known = True
            if not peer_known and not peers_peer.equals(self.socket_communication.socket_connector):
                self.socket_communication.connect_with_node(peers_peer.ip, peers_peer.port)