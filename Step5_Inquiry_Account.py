import json

import requests

from Constant import BASE_URL, ACCESS_TOKEN, MERCHANT_ID, \
    PAY_OUT_INQUIRY_ACCOUNT_API
from Tool import getTimestamp
from Tool_Sign import hmacSHA512
from req.InquiryAccountReq import InquiryAccountReq
from req.MerchantReq import MerchantReq


# from step2

def inquiry_account():
    print("=====> step5 : Inquiry Account")

    # url
    end_point_ulr = PAY_OUT_INQUIRY_ACCOUNT_API
    url = BASE_URL + end_point_ulr

    # access_token
    access_token = ACCESS_TOKEN

    # transaction time
    timestamp = getTimestamp()

    # partner_id
    partner_id = MERCHANT_ID
    paymentMethod = "BRI"
    account_no = "1234567890"

    # merchantReq
    merchant_req = MerchantReq(partner_id, None, None)

    inquiry_payment_method_req = InquiryAccountReq(merchant_req, paymentMethod, account_no, None, None)

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
