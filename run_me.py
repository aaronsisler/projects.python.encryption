from encryption_service import Crypto

crypto = Crypto()

key = crypto.generate_key()
# key = 'This is a key123'
iv = crypto.generate_iv()
# iv = 'This is an IV456'
# data = b'Taco'
data = "Taco"

encrypted = crypto.encrypt(key, iv, data)
print(encrypted)
decrypted = crypto.decrypt(key, iv, encrypted)
print(decrypted)