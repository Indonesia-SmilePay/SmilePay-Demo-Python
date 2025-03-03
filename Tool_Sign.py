import base64
import hashlib
import hmac
from datetime import datetime

import pytz
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from Constant import MERCHANT_SECRET


# Generating Signatures with Crypto
def sign(privateKey, message):
    private_key = RSA.importKey(base64.b64decode(privateKey.encode('utf-8')))
    cipher = PKCS1_v1_5.new(private_key)
    h = SHA256.new(message.encode('utf-8'))
    signature = cipher.sign(h)
    return base64.b64encode(signature).decode('utf-8')


def hmacSHA512(method, endPointUlr, accessToken, json_data_minify, timestamp):
    print("json_data_minify=", json_data_minify)

    # calculate_sha256
    byte2Hex = calculate_sha256(json_data_minify)
    print("sha256 then byte2Hex=", byte2Hex)

    # lowercase_string
    lower_case = byte2Hex.lower()
    print("lower_case=", lower_case)

    # build
    string_to_sign = method + ":" + endPointUlr + ":" + accessToken + ":" + lower_case + ":" + timestamp
    print("string_to_sign=", string_to_sign)

    # signature
    signature = calculate_hmac_sha512_base64(MERCHANT_SECRET, string_to_sign)
    print("signature=", signature)
    return signature


def get_formatted_datetime(timezone_str: object) -> object:
    # Creating a time zone object
    timezone = pytz.timezone(timezone_str)
    # Get the current time and set it to the specified time zone
    now = datetime.now(timezone)
    # Returns a formatted date and time string
    return now.isoformat(timespec='seconds')


def calculate_sha256(text):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode('utf-8'))
    hash_value = sha256_hash.hexdigest()
    return hash_value


def calculate_hmac_sha512_base64(key, message):
    hmac_sha512 = hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha512)
    hash_value = hmac_sha512.digest()
    base64_value = base64.b64encode(hash_value).decode('utf-8')
    return base64_value
