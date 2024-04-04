from cryptography.fernet import Fernet

# Generate a Fernet key
key = Fernet.generate_key()

# Encode the key to URL-safe base64 format
url_safe_key = key.decode('utf-8')

print("Generated 32-byte URL-safe base64-encoded key:", url_safe_key)
