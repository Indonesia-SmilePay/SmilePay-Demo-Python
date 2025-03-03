import json
import time

import requests

from Constant import PAY_IN_API, BASE_URL, MERCHANT_ID, ACCESS_TOKEN
from Tool import getTimestamp
from Tool_Sign import hmacSHA512
from req.AddressReq import AddressReq
from req.ItemDetailReq import ItemDetailReq
from req.MerchantReq import MerchantReq
from req.MoneyReq import MoneyReq
from req.PayerReq import PayerReq
from req.ReceiverReq import ReceiverReq
from req.TradePayInReq import TradePayInReq


# from step2

def transaction_pay_in():
    print("=====> step3 : PayIn transaction")

    # url
    end_point_ulr = PAY_IN_API
    url = BASE_URL + end_point_ulr

    # access_token
    access_token = ACCESS_TOKEN

    # transaction time
    timestamp = getTimestamp()

    # partner_id
    partner_id = MERCHANT_ID
    merchant_order_no = "T_" + str(time.time())
    purpose = "Purpose For Transaction from python Demo"
    payment_method = "BRI"
    product_detail = "Product details"
    additional_param = "other descriptions"

    # moneyReq
    money_req = MoneyReq("IDR", 30000)

    # merchantReq
    merchant_req = MerchantReq(partner_id, None, None)

    # payerReq
    payer_req = PayerReq("paulo", "paulo@gmail.com", "82-018922990",
                         "Jalan Pantai Mutiara TG6, Pluit, Jakarta", None)

    # receiverReq
    receiver_req = ReceiverReq("smilepay", "smilepay@gmail.com", "82-018922990",
                               "Jl. Pluit Karang Ayu 1 No.B1 Pluit", None)

    # itemDetailReq
    item_detail_req = ItemDetailReq("mac A1", 1, 10000)
    item_detail_req_list = [item_detail_req]

    # billingAddress
    billing_address = AddressReq("Jl. Pluit Karang Ayu 1 No.B1 Pluit", "jakarta",
                                 "14450", "82-018922990", "Indonesia")
    # shippingAddress
    shipping_address = AddressReq("Jl. Pluit Karang Ayu 1 No.B1 Pluit", "jakarta",
                                  "14450", "82-018922990", "Indonesia")

    # payInReq
    pay_in_req = TradePayInReq(payment_method, payer_req, receiver_req, None, merchant_order_no, purpose,
                               product_detail,
                               additional_param,
                               item_detail_req_list, billing_address, shipping_address, money_req, merchant_req, None,
                               None)

    json_data_minify = json.dumps(pay_in_req, default=lambda o: o.__dict__, separators=(',', ':'))
    signature = hmacSHA512("POST", end_point_ulr, access_token, json_data_minify, timestamp)

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

