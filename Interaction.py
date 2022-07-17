from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests

from constants import POST_TRANSACTION_URL, TRANSFER_OPERATIONS

if __name__ == '__main__':
    bob = Wallet()
    alice = Wallet()
    exchange = Wallet()

    transaction = exchange.create_transaction(
        alice.get_public_key_string(), 10, TRANSFER_OPERATIONS.EXCHANGE)

    url = POST_TRANSACTION_URL
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)
    print(request.text)
