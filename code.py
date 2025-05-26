import random
import string
import base64
import time
import hmac
import hashlib
from datetime import datetime, timedelta

def random_string(length):
    """Generate a random string of digits and letters with specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encode_base64(s):
    """Encode string to base64."""
    return base64.b64encode(s.encode()).decode().strip()

def generate_hmac(secret_key):
    """Generate a random HMAC with SHA256."""
    message = random_string(16)
    return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

def create_token():
    """Generate a single token following a custom format."""
    random_str = random_string(18)
    base64_str = encode_base64(random_str)

    rand_date = datetime.utcnow() + timedelta(days=random.randint(-365, 365))
    timestamp = int(rand_date.timestamp())
    timestamp_plus_epoch = timestamp + 129384000
    timestamp_str = str(timestamp_plus_epoch)

    secret_key = random_string(32)
    hmac_str = generate_hmac(secret_key)

    token = f"{base64_str}.{timestamp_str}.{hmac_str}."
    return token

def save_tokens_to_file(tokens, filename):
    """Save tokens to a text file."""
    with open(filename, 'w') as file:
        for token in tokens:
            file.write(token + '\n')

def main():
    num_tokens = 1000
    tokens = []

    for _ in range(num_tokens):
        token = create_token()
        tokens.append(token)

    # Save tokens to a file
    save_tokens_to_file(tokens, 'tokens.txt')
    print("Tokens have been saved to 'tokens.txt'.")

if __name__ == "__main__":
    main()
