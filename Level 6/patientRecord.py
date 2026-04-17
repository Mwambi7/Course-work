def checkAccess(role):
    
    if role.strip().capitalize() != "Doctor":
        raise PermissionError("Access Denied: Unauthorized Role")
    print("Access Granted.")


user_role = input("Enter your role: ")

try:
    checkAccess(user_role)
except PermissionError as e:
    print(f"Caught an error: {e}")
    
    """ def scope_test():
    local_variable = "I am hidden inside the function"
    print(local_variable)

scope_test()

# Attempting to access outside
print(local_variable)"""