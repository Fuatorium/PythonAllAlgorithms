from Crypto.Cipher import AES # type: ignore
from Crypto.Util.Padding import pad, unpad # type: ignore
from Crypto.Random import get_random_bytes # type: ignore

def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ct_bytes

def aes_decrypt(key, data):
    iv = data[:16]
    ct = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt

if __name__ == "__main__":
    key = get_random_bytes(16)
    data = b"Hello, AES!"
    encrypted = aes_encrypt(key, data)
    print(f"Encrypted: {encrypted}")
    decrypted = aes_decrypt(key, encrypted)
    print(f"Decrypted: {decrypted}")
