import json

import requests

from Constant import BASE_URL, ACCESS_TOKEN, PAY_OUT_INQUIRY_PAYMENT_METHOD_API, MERCHANT_ID
from Tool import getTimestamp
from Tool_Sign import hmacSHA512
from req.InquiryPaymentMethodReq import InquiryPaymentMethodReq
from req.MerchantReq import MerchantReq


# from step2

def inquiry_paymentMethod():
    print("=====> step4 : Inquiry PaymentMethod")

    # url
    end_point_ulr = PAY_OUT_INQUIRY_PAYMENT_METHOD_API
    url = BASE_URL + end_point_ulr

    # access_token
    access_token = ACCESS_TOKEN

    # transaction time
    timestamp = getTimestamp()

    # partner_id
    partner_id = MERCHANT_ID

    # merchantReq
    merchant_req = MerchantReq(partner_id, None, None)

    inquiry_payment_method_req = InquiryPaymentMethodReq(merchant_req, None)

    json_data_minify = json.dumps(inquiry_payment_method_req, default=lambda o: o.__dict__, separators=(',', ':'))
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
