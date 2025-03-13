import hashlib

# The email address to be hashed
email = "kallilinux1234@gmail.com"

# Create a hash object using SHA-256
hash_object = hashlib.sha256(email.encode())

# Get the hexadecimal representation of the hash
email_hash = hash_object.hexdigest()

# Output the hashed email
print(f"SHA-256 Hash of the email '{email}' is: {email_hash}")
