class MobileMoneyDSL:
    def __init__(self, accounts):
       
        self.accounts = accounts

    def execute(self, command):
        print(f"Executing: '{command}'")
        try:
            # 1. PARSER: 
            tokens = command.split()
            
            #  TRANSFER [amount] FROM [sender] TO [receiver] IF BALANCE > [threshold]
            amount = float(tokens[1])
            sender = tokens[3]
            receiver = tokens[5]
            threshold = float(tokens[9])

            # Validation & Rules
            if sender not in self.accounts:
                return f"Error: Sender '{sender}' does not exist."
            
            if receiver not in self.accounts:
                return f"Error: Receiver '{receiver}' does not exist."

            current_balance = self.accounts[sender]

            # Rule Validation: IF BALANCE > threshold
            if current_balance > threshold:
                if current_balance >= amount:
                    # Perform the transaction
                    self.accounts[sender] -= amount
                    self.accounts[receiver] += amount
                    return f"Success: Transferred {amount} from {sender} to {receiver}. New Balance: {self.accounts[sender]}"
                else:
                    return f"Error: Insufficient funds for transfer."
            else:
                return f"Rule Denied: Balance must be greater than {threshold} to initiate."

        except (IndexError, ValueError):
            return "Syntax Error: Ensure command follows 'TRANSFER X FROM A TO B IF BALANCE > Y'"

# --- TEST DRIVE ---

# Initial State
database = {"ALICE": 5000, "BOB": 1000}
engine = MobileMoneyDSL(database)

# Scenario A: Valid Transaction
print(engine.execute("TRANSFER 2000 FROM ALICE TO BOB IF BALANCE > 1000"))

# Scenario B: Rule Violation (Balance not > 4000)
print(engine.execute("TRANSFER 500 FROM BOB TO ALICE IF BALANCE > 4000"))