# encoder.py

import base64

def encode_string(s):
    encoded = base64.b64encode(s.encode()).decode()
    print("Encoded string:", encoded)

if __name__ == "__main__":
    user_input = input("Enter string to encode in Base64: ")
    encode_string(user_input)
