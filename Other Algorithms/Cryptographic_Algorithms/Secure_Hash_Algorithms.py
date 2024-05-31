import hashlib

def sha256(data):
    return hashlib.sha256(data).hexdigest()

if __name__ == "__main__":
    data = b"Hello, SHA-256!"
    print(f"SHA-256: {sha256(data)}")
