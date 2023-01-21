import random
import string

def create_secure_password(password_length):
    errors = 0
    while True:
        try:
            password_length = int(password_length)
            if password_length < 8:
                errors += 1
                if errors > 1:
                    return "Too many errors, exiting"
                print("Password length should be at least 8 characters.")
                continue
            break
        except ValueError:
            errors += 1
            if errors > 1:
                return "Too many errors, exiting"
            print("Invalid input. Please enter a number.")

    # Create a list of allowed characters
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    # Create a password of the specified length
    password = "".join(random.choices(allowed_chars, k=password_length))

    # Verify that the password does not contain any dictionary words
    # (this step is omitted for brevity and can be added as additional functionality)

    return password

print(create_secure_password(int(input("How long should be your password ?"))))