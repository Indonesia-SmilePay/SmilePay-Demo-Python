import base64
import json
import uuid

import pytz
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime


# Generating Signatures with Crypto
def sign(privateKey, message):
    private_key = RSA.importKey(base64.b64decode(privateKey.encode('utf-8')))
    cipher = PKCS1_v1_5.new(private_key)
    h = SHA256.new(message.encode('utf-8'))
    signature = cipher.sign(h)
    return base64.b64encode(signature).decode('utf-8')

def checkSha256RsaSignature(content, signature, publicKeyStr):
    try:
        public_key = serialization.load_pem_public_key(publicKeyStr.encode('utf-8'))

        data_to_verify = content.encode('utf-8')
        signature_bytes = base64.b64decode(signature)
        public_key.verify(
            signature_bytes,
            data_to_verify,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print("error:" + str(e))  # Convert the exception object to a string and print it
        return False


def generate_32bit_uuid():
    # Generate a UUID
    unique_id = uuid.uuid4()
    # Convert the UUID to a 32-character string (remove dashes)
    uuid_str = str(unique_id).replace('-', '')
    return uuid_str


# Generating Signatures with Crypto
def sha256RsaSignature(privateKey, message):
    private_key = RSA.importKey(base64.b64decode(privateKey.encode('utf-8')))
    cipher = PKCS1_v1_5.new(private_key)
    h = SHA256.new(message.encode('utf-8'))
    signature = cipher.sign(h)
    return base64.b64encode(signature).decode('utf-8')


def minify(pay_in_req):
    return json.dumps(pay_in_req, default=lambda o: o.__dict__, separators=(',', ':'))


def get_formatted_datetime(timezone_str: object) -> object:
    # Creating a time zone object
    timezone = pytz.timezone(timezone_str)
    # Get the current time and set it to the specified time zone
    now = datetime.now(timezone)
    # Returns a formatted date and time string
    return now.isoformat(timespec='seconds')
