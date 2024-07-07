minimum_length = 8

def password_validator(password):

    if len(password) < minimum_length:
        print(f"Password is too short. Minimum length is {minimum_length} characters.")
        return False  

    missing_criteria = []
    if not any(char.isdigit() for char in password):
        missing_criteria.append("a digit")
    if not any(char.isupper() for char in password):
        missing_criteria.append("an uppercase letter")

    if missing_criteria:
        print(f"Password is missing: {', '.join(missing_criteria)}")
        return False

    return True  

password_attempt = input("Enter a password: ")

if password_validator(password_attempt):
    confirm_password = input("Confirm your password: ")
    if password_attempt == confirm_password:
        print("Your password is confirmed!")
    else:
        print("Passwords do not match. Please try again.")
else:
    print("Please try again with a stronger password.")
