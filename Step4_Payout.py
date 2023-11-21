import base64
import hashlib
import hmac
import json
import time

import requests

from Constant import BASE_URL, MERCHANT_ID, MERCHANT_SECRET, PAY_OUT_API
from req.AddressReq import AddressReq
from req.ItemDetailReq import ItemDetailReq
from req.MerchantReq import MerchantReq
from req.MoneyReq import MoneyReq
from req.PayerReq import PayerReq
from req.ReceiverReq import ReceiverReq
from req.TradePayoutReq import TradePayoutReq

# from step2
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE3MDA1NjQ4MjAsImV4cCI6MTcwMDU2NTcyMCwiaWF0IjoxNzAwNTY0ODIwLCJNRVJDSEFOVF9JRCI6InNhbmRib3gtMTAwMDQifQ.E-HZJ94eLmZYpykFGtLLBxlWJfSat9EAm4r36vZywxQ"


def disbursement_pay_out():
    print("=====> step4 : Payout Disbursement")

    # url
    end_point_ulr = PAY_OUT_API
    url = BASE_URL + end_point_ulr

    # transaction time
    timestamp = "2023-11-21T11:03:47+07:00"
    # partner_id
    partner_id = MERCHANT_ID
    merchant_order_no = "D_" + str(time.time())
    purpose = "Purpose For Disbursement from python SDK"
    payment_method = "BCA"
    product_detail = "Product details"
    additional_param = "other descriptions"
    cashAccount = "36473282333"

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

    # payoutReq
    pay_out_req = TradePayoutReq(payment_method, payer_req, receiver_req, cashAccount, merchant_order_no, purpose,
                                 product_detail,
                                 additional_param,
                                 item_detail_req_list, billing_address, shipping_address, money_req, merchant_req, None,
                                 None)

    # jsonStr by json then minify
    json_data_minify = json.dumps(pay_out_req, default=lambda o: o.__dict__, separators=(',', ':'))
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
disbursement_pay_out()
