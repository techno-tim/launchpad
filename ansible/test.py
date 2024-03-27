from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class AsymmetricEncryption:
    def __init__(self, key_size=2048):
        self.key = RSA.generate(key_size)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

    def encrypt(self, plaintext):
        cipher_rsa = PKCS1_OAEP.new(self.key.publickey())
        ciphertext = cipher_rsa.encrypt(plaintext.encode())
        return ciphertext

    def decrypt(self, ciphertext):
        cipher_rsa = PKCS1_OAEP.new(self.key)
        plaintext = cipher_rsa.decrypt(ciphertext)
        return plaintext.decode()