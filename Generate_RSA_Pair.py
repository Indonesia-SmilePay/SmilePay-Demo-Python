import Crypto.Util.number
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Cipher import AES
import base64
import os
import sys

encoding_utf8 = 'utf-8'
PRIVATE_KEY_BEGIN = '-----BEGIN PRIVATE KEY-----'
PRIVATE_KEY_END = '-----END PRIVATE KEY-----'
PUBLIC_KEY_BEGIN = '-----BEGIN PUBLIC KEY-----'
PUBLIC_KEY_END = '-----END PUBLIC KEY-----'


def rsa_create_key(bits):
    random_generator = Random.new().read
    rsa = RSA.generate(bits, random_generator)

    pkcs8_private_key = rsa.exportKey(format='PEM', passphrase=None, pkcs=8, protection=None)
    private_key_with_title_and_bottom = pkcs8_private_key.decode("utf-8")
    private_key_string = private_key_with_title_and_bottom.removeprefix(PRIVATE_KEY_BEGIN) \
        .removesuffix(PRIVATE_KEY_END).replace('\n', "")

    public_pem = rsa.publickey().exportKey()
    public_key_with_begin_and_end = public_pem.decode(encoding_utf8)
    public_key_string = public_key_with_begin_and_end.removeprefix(PUBLIC_KEY_BEGIN) \
        .removesuffix(PUBLIC_KEY_END).replace("\n", "")

    print("private_key_string=", private_key_string)
    print("public_key_string=", public_key_string)
    return public_key_string, private_key_string


rsa_create_key(2048)