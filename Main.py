from Transaction import Transaction
from Wallet import Wallet

def generate_transaction() -> Transaction:
    SENDER = 'sender'
    RECIEVER = 'reciever'
    AMOUNT = 2
    TYPE = 'TRANSFER'
    generated_transaction = Transaction(SENDER,RECIEVER,AMOUNT,TYPE)
    return generated_transaction

if __name__ == '__main__':
    transaction = generate_transaction()
    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    print(signature)

    