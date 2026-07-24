import re

password = "Hello@123"

if len(password) < 8:
    print("Weak Password: Minimum 8 characters required.")
elif not re.search(r"[A-Z]", password):
    print("Weak Password: Add at least one uppercase letter.")
elif not re.search(r"[a-z]", password):
    print("Weak Password: Add at least one lowercase letter.")
elif not re.search(r"\d", password):
    print("Weak Password: Add at least one number.")
elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Weak Password: Add at least one special character.")
else:
    print("Strong Password")