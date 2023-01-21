import base64

def encrypt_base64(string: str) -> str:
    encoded_string = base64.b64encode(string.encode())
    return encoded_string.decode()

def decrypt_base64(encoded_string: str) -> str:
    decoded_string = base64.b64decode(encoded_string.encode()).decode()
    return decoded_string

string_to_encode = input("Enter the string you want to encode: ")
encoded_string = encrypt_base64(string_to_encode)
print(encoded_string)
decoded_string = decrypt_base64(encoded_string)
print(decoded_string)