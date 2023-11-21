import base64
import hashlib
import hmac
import json
import time

import requests

from Constant import PAY_IN_API, BASE_URL, MERCHANT_ID, MERCHANT_SECRET
from req.AddressReq import AddressReq
from req.ItemDetailReq import ItemDetailReq
from req.MerchantReq import MerchantReq
from req.MoneyReq import MoneyReq
from req.PayerReq import PayerReq
from req.ReceiverReq import ReceiverReq
from req.TradePayInReq import TradePayInReq

# from step2
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE3MDA1NjM4NjUsImV4cCI6MTcwMDU2NDc2NSwiaWF0IjoxNzAwNTYzODY1LCJNRVJDSEFOVF9JRCI6InNhbmRib3gtMTAwMDQifQ.LBkcQ4EDA3SJDjsP-63zxVkybqf5BjV4Y4Xxgi2DHlw"


def transaction_pay_in():
    print("=====> step3 : PayIn transaction")

    # url
    end_point_ulr = PAY_IN_API
    url = BASE_URL + end_point_ulr

    # transaction time
    timestamp = "2023-11-21T11:03:47+07:00"
    # partner_id
    partner_id = MERCHANT_ID
    merchant_order_no = "T_" + str(time.time())
    purpose = "Purpose For Transaction from python SDK"
    payment_method = "BCA"
    product_detail = "Product details"
    additional_param = "other descriptions"

    # moneyReq
    money_req = MoneyReq("IDR", 10000)

    # merchantReq
    merchant_req = MerchantReq(partner_id, None, None)

    # payerReq
    payer_req = PayerReq("Jef-fer", "jef.gt@gmail.com", "82-3473829260",
                         "Jalan Pantai Mutiara TG6, Pluit, Jakarta", None)

    # receiverReq
    receiver_req = ReceiverReq("Viva in", "Viva@mir.com", "82-3473233732",
                               "Jl. Pluit Karang Ayu 1 No.B1 Pluit", None)

    # itemDetailReq
    item_detail_req = ItemDetailReq("mac A1", 1, 10000)
    item_detail_req_list = [item_detail_req]

    # billingAddress
    billing_address = AddressReq("Jl. Pluit Karang Ayu 1 No.B1 Pluit", "jakarta",
                                 "14450", "82-3473233732", "Indonesia")
    # shippingAddress
    shipping_address = AddressReq("Jl. Pluit Karang Ayu 1 No.B1 Pluit", "jakarta",
                                  "14450", "82-3473233732", "Indonesia")

    # payInReq
    pay_in_req = TradePayInReq(payment_method, payer_req, receiver_req, None, merchant_order_no, purpose,
                               product_detail,
                               additional_param,
                               item_detail_req_list, billing_address, shipping_address, money_req, merchant_req, None,
                               None)

    # jsonStr by json then minify
    json_data_minify = json.dumps(pay_in_req, default=lambda o: o.__dict__, separators=(',', ':'))
    print("json_data_minify=", json_data_minify)

    # calculate_sha256
    byte2Hex = calculate_sha256(json_data_minify)
    print("sha256 then byte2Hex=", byte2Hex)

    # lowercase_string
    lower_case = byte2Hex.lower()
    print("lower_case=", lower_case)

    # build
    string_to_sign = "POST" + ":" + end_point_ulr + ":" + access_token + ":" + lower_case + ":" + timestamp
    print("string_to_sign=", string_to_sign)

    # signature
    signature = calculate_hmac_sha512_base64(MERCHANT_SECRET, string_to_sign)
    print("merchant_secret=", MERCHANT_SECRET)
    print("signature=", signature)

    # post
    # header
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + access_token,
        'X-TIMESTAMP': timestamp,
        'X-SIGNATURE': signature,
        'ORIGIN': "www.yourDomain.com",
        'X-PARTNER-ID': partner_id,
        'X-EXTERNAL-ID': "123729342472347234236",
        'CHANNEL-ID': "95221"

    }
    # POST request
    response = requests.post(url, data=json_data_minify, headers=headers)
    # Get response result
    result = response.json()
    print(result)


def remove_nulls(d):
    if isinstance(d, dict):
        for k, v in list(d.items()):
            if v is None:
                del d[k]
            else:
                remove_nulls(v)
    if isinstance(d, list):
        for v in d:
            remove_nulls(v)
    return d


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


# run
transaction_pay_in()
