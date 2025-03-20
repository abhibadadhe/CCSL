import hashlib

def compute_hashes(text):
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    return sha256_hash

user_input = input("Enter a string: ")
sha256_result = compute_hashes(user_input)

print(f"SHA256 Hash: {sha256_result}")