from flask_classful import FlaskView, route
from flask import Flask, jsonify

import Node

NODE : Node = None

class NodeAPI(FlaskView):
    """Class for implemenating API for the blockchain
    """

    def __init__(self):
        self.app = Flask(__name__, static_url_path='')

    def start(self, api_port:int):
        NodeAPI.register(self.app, route_base='/')
        self.app.run(host='localhost', port=api_port)
        
    def inject_node(self, injected_node: Node) -> None:
        global NODE
        NODE = injected_node

    @route('/info', methods=['GET'])
    def info(self):
        return 'This is a communiction interface to the blockchain', 200
    
    @route('blockchain', methods=['GET'])
    def blockchain(self) -> dict:
        return NODE.blockchain.to_json(), 200
    
    @route('transaction_pool', methods=['GET'])
    def transaction_pool(self):
        transactions = {}
        for counter, transaction in enumerate(NODE.transactions_in_txs_pool()):
            transactions[counter] = transaction.to_json()
        return jsonify(transactions), 200