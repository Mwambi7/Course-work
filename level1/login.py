# Predefined credentials
USERNAME = "adminKE"
PASSWORD = "254Secure"

max_attempts = 3
attempts = 0
logged_in = False

while attempts < max_attempts:
    # Prompt user for username and password
    user_name = input("Enter username: ")
    input_password = input("Enter password: ")

    # Validate credentials
    if user_name == USERNAME and input_password == PASSWORD:#if you use or a logical error is encountered 
        print("Login successful!")
        logged_in = True
        break  # Exit the loop if login is successful
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Invalid Credentials! {remaining} Remaining attempts")

# End of while loop
if not logged_in:
    print("Your account has been blocked!")