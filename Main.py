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
    transaction.sign(signature)
    signature_validity = Wallet.validate_signature(transaction.payload(),
                                                   signature,wallet.get_public_key_string())
    print(signature_validity)

    