from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad


class Crypto:
    block_size = AES.block_size

    def encrypt(self, key, iv, data):
        if isinstance(data, str):
            data = str.encode(data)
        obj = AES.new(key, AES.MODE_CBC, iv)
        return obj.encrypt(pad(data, self.block_size))

    def decrypt(self, key, iv, data):
        obj = AES.new(key, AES.MODE_CBC, iv)
        return unpad(obj.decrypt(data), self.block_size).decode()

    def generate_key(self):
        key = os.urandom(16)
        return key

    def generate_iv(self):
        iv = os.urandom(16)
        return iv
