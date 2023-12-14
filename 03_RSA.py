#pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)
pubKey = keyPair.publickey()

pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = 'Ismile Academy'
msg_bytes = msg.encode('utf-8')

encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg_bytes)
print("Encrypted:", binascii.hexlify(encrypted))
