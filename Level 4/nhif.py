# 1. The Data Model
class Patient:
    def __init__(self, name, policy_number):
        self.name = name
        self.policy_number = policy_number

# 2. The Logic & Display (Abstraction)
class NHIFSystem:
    def __init__(self):
        self.co_pay_rate = 0.10

    def process_claim(self, patient, total_bill):
        # Calculation logic
        payout = total_bill * (1 - self.co_pay_rate)
        patient_owes = total_bill - payout

        # Simple Display using a Multi-line f-string
        print(f"""
        === NHIF CLAIM SUMMARY ===
        Patient Name:  {patient.name}
        Policy Number: {patient.policy_number}
        --------------------------
        Total Hospital Bill: Ksh {total_bill}
        NHIF Payout (90%):   Ksh {payout}
        Patient Co-pay (10%): Ksh {patient_owes}
        ==========================
        """)

# 3. Execution (The Main Entry Point)
if __name__ == "__main__":
    # objects
    my_patient = Patient("Terry Sharon", "NHIF-778899")
    nhif = NHIFSystem()

    
    nhif.process_claim(my_patient, 10000)

    """ THE PROCEDURAL ROUTE
    we use simple variables and a standalone function.
    
def calculate_nhif_claim(amount):
    co_pay = amount * 0.10
    payout = amount - co_pay
    return payout, co_pay

# Data: Just variables (not tied to an object)
patient_name = "Alice Wanjiku"
policy_number = "NHIF-778899"
hospital_bill = 10000.0

 Calling the function directly
nhif_payout, member_owes = calculate_nhif_claim(hospital_bill)

# Display
print(f"Patient: {patient_name}")
print(f"NHIF Payout: {nhif_payout}")
print(f"Member Owes: {member_owes}")"""