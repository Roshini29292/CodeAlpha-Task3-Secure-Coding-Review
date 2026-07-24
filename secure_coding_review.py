import re

def check_password(password):
    if len(password) < 8:
        return "Weak Password: Minimum 8 characters required."

    if not re.search(r"[A-Z]", password):
        return "Weak Password: Add at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "Weak Password: Add at least one lowercase letter."

    if not re.search(r"\d", password):
        return "Weak Password: Add at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak Password: Add at least one special character."

    return "Strong Password"

password = input("Enter Password: ")
print(check_password(password))