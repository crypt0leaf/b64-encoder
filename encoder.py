# encoder.py

import base64

def encode_string(s):
    encoded = base64.b64encode(s.encode()).decode()
    print("Encoded string:", encoded)

if __name__ == "__main__":
    user_input = input("Enter string to encode in Base64: ")
    encode_string(user_input)

# Temporary debug output (I have to clean that after:
# XCkDs7ro/Luw4IGLo9NDPNK7mQ4azxel6ONqvaqH8VueWOmxu1QalqmUaond5Xm4/erGbkwyNnAEm+LoMQS3Wlci7zK7Znz/92oPLtJn5eA4aVJ4f27pdfwijTS6L9qUPTBJWCWmknbPM4wo/HMC0sV4NfW3W0AWyHygZ+bNtEoB9OdONY5Yf0If7vGwTr657CL0ddguA2dNnZFkaDyXwfucum2LFC+aGIH4oqA9DtBTEgKf9nemgNbv8+t+pmsznOxbU1y2tMcg87tWO8ZngbynrfqeqJI2DN0QLGYo3e250emz1Kmz36BNcxHfU2Bd9eKaDmkvRtmgEloLdjCCLQ==