# 1. Get Member Info
name = input("Enter Member Name: ")
member_id = input("Enter Member ID: ")
total_savings = 0.0

#Get 6 months of contributions
print("\nEnter contributions for 6 months:")
for i in range(1, 7):
    # Get input, convert to a number, and add to the total
    amount = float(input(f"Month {i}: "))
    total_savings += amount

# Result
print("\n--- Summary ---")
print("Member Name:", name)
print("Member ID:", member_id)
print("Total Savings: $", total_savings)