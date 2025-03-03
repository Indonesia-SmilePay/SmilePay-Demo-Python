import json
import time

import requests

import Tool_Sign
from Constant import MERCHANT_ID, MERCHANT_SECRET, PAY_OUT_API, BASE_URL, ACCESS_TOKEN
from Tool import getTimestamp
from req.AddressReq import AddressReq
from req.ItemDetailReq import ItemDetailReq
from req.MerchantReq import MerchantReq
from req.MoneyReq import MoneyReq
from req.PayerReq import PayerReq
from req.ReceiverReq import ReceiverReq
from req.TradePayoutReq import TradePayoutReq


def disbursement_pay_out():
    print("=====> step6 : Payout Disbursement")
    # transaction time
    timestamp = getTimestamp()
    access_token = ACCESS_TOKEN
    # partner_id
    partner_id = MERCHANT_ID
    # url
    end_point_ulr = PAY_OUT_API
    url = BASE_URL + end_point_ulr

    # transaction time
    # partner_id
    merchant_order_no = "D_" + str(time.time())
    purpose = "Purpose For Disbursement from python Demo"
    payment_method = "BCA"
    product_detail = "Product details"
    additional_param = "other descriptions"
    cashAccount = "36473282333"

    # moneyReq
    money_req = MoneyReq("IDR", 10000)

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

    # payoutReq
    pay_out_req = TradePayoutReq(payment_method, payer_req, receiver_req, cashAccount, merchant_order_no, purpose,
                                 product_detail,
                                 additional_param,
                                 item_detail_req_list, billing_address, shipping_address, money_req, merchant_req, None,
                                 None)

    # jsonStr by json then minify
    json_data_minify = json.dumps(pay_out_req, default=lambda o: o.__dict__, separators=(',', ':'))
    print("json_data_minify=", json_data_minify)

    # signature
    signature = Tool_Sign.hmacSHA512("POST",
                                     end_point_ulr,
                                     access_token,
                                     json_data_minify,
                                     timestamp)

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
