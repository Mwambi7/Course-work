import sys

class CDFLang_676183:
    def __init__(self):
        # Constants
        self.K1, self.K3, self.THRESHOLD = 16, 18, 19
        self.TAG = "mubi"
        
        # Symbol Table: 
        
        # Using a list for values to simulate the Calling Stack for Dynamic Scope
        self.symbol_table = {}
        self.call_stack = ["global"]
        
        # Execution Metadata
        self.fingerprint = "CDF-3-1-2-1-0-0-2"
        self.reg = "676183"
        self.domain = "Climate Sensor Monitoring"

    def log_signature(self):
        print(f"CDF:{self.fingerprint}|REG:{self.reg}|DOMAIN:{self.domain}|TAG:{self.TAG}|IMPL:Python")

    def bind(self, name, value, var_type="Inferred"):
        """Declaration & Binding (Gradual Typing)"""
        if name not in self.symbol_table:
            self.symbol_table[name] = []
        
        # Dynamic Scope Logic: Push to stack
        scope = self.call_stack[-1]
        self.symbol_table[name].append({"val": value, "type": var_type, "scope": scope})
        print(f"[TOKEN: DECLARE] {name} initialized to {value} ({var_type}) in {scope} scope.")

    def lookup(self, name):
        """Dynamic Scope Lookup: Searches from top of stack down"""
        if name in self.symbol_table and self.symbol_table[name]:
            return self.symbol_table[name][-1]["val"]
        raise NameError(f"TRAP: Signal Lost. Variable '{name}' not found in active stack.")

    def run_blueprint(self, name, logic_func):
        """Abstraction Mechanism (Simulating a Sensor Blueprint)"""
        print(f"\n[EXECUTION] Entering Blueprint: {name}")
        self.call_stack.append(name)
        try:
            logic_func()
        except Exception as e:
            print(f"TRAP CAUGHT: {e}")
        finally:
            self.call_stack.pop()
            print(f"[EXECUTION] Exiting Blueprint: {name}\n")

    def display_symbol_table(self):
        print("\n--- SYMBOL TABLE ---")
        print(f"{'Name':<12} | {'Value':<8} | {'Type':<10} | {'Scope'}")
        for name, history in self.symbol_table.items():
            current = history[-1]
            print(f"{name:<12} | {current['val']:<8} | {current['type']:<10} | {current['scope']}")
        print("--------------------\n")

# --- COMPULSORY SAMPLE PROGRAM ---
def sample_program():
    lang = CDFLang_676183()
    lang.log_signature()

    # 1. Declarations (3 variables)
    lang.bind("base_temp", lang.K1, "Float")
    lang.bind("current_reading", 0, "Inferred")
    lang.bind("status", "idle", "String")

    # 2. Abstraction (Blueprint)
    def sensor_logic():
        # Using a personalized constant
        lang.bind("local_offset", lang.K3, "Static") 
        
        # 3. Repetition (Stream)
        for i in range(1, 4):
            # 4. Expression & Assignment
            new_val = lang.lookup("base_temp") + i + lang.lookup("local_offset")
            lang.symbol_table["current_reading"][-1]["val"] = new_val
            
            # 5. Selection (Alert_if)
            if new_val > lang.THRESHOLD:
                print(f"ALERT: Sensor exceeded threshold {lang.THRESHOLD}! Current: {new_val}")
            else:
                print(f"Log: Reading is normal: {new_val}")

    lang.run_blueprint("Heat_Sensor_Mubi", sensor_logic)
    
    # Final Table State
    lang.display_symbol_table()

    # --- NEGATIVE TESTS ---
    print("--- RUNNING ROBUSTNESS TESTS ---")
    
    # Test 1: Binding/Scope Failure (Accessing local outside blueprint)
    try:
        print("Testing Scope Access...")
        val = lang.lookup("local_offset")
    except NameError as e:
        print(f"Outcome: {e}")

    # Test 2: Runtime/Robustness Failure (Simulated Exception)
    try:
        print("Testing Trap Mechanism...")
        raise Exception("Hardware Timeout: Battery Low")
    except Exception as e:
        print(f"TRAP: {e}. Switching to low-power mode.")

    # Test 3: Syntax/Type Failure (Simulated)
    print("Testing Syntax Check: monitor temp <- 'High'")
    print("Error: Type Mismatch. Cannot assign String to Float typed 'monitor'.")

if __name__ == "__main__":
    sample_program()