
class AccountModel():
    
    def __init__(self) -> None:
        self.accounts = []
        self.balances = {}
        
    def add_account(self, public_key_string:str) -> None:
        if not public_key_string in self.accounts:
            self.accounts.append(public_key_string)
            self.balances[public_key_string] = 0
    
    def get_balance(self, public_key_string:str) -> int:
        if public_key_string not in self.accounts:
            self.add_account(public_key_string)
        return self.balances[public_key_string]
    
    def update_balance(self, public_key_string:str, amount:int) -> None:
        if public_key_string not in self.accounts:
            self.add_account(public_key_string)
        self.balances[public_key_string] += amount