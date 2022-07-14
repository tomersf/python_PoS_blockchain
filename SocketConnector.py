from __future__ import annotations

class SocketConnector():
    
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
        
    def equals(self, connector: SocketConnector) -> bool:
        if connector.ip == self.ip and connector.port == self.port:
            return True
        return False