import base64

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


# Generating Signatures with Crypto
def sign(privateKey, message):
    private_key = RSA.importKey(base64.b64decode(privateKey.encode('utf-8')))
    cipher = PKCS1_v1_5.new(private_key)
    h = SHA256.new(message.encode('utf-8'))
    signature = cipher.sign(h)
    return base64.b64encode(signature).decode('utf-8')
