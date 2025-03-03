import json

import requests

from Constant import BASE_URL, ACCESS_TOKEN, MERCHANT_ID, \
    INQUIRY_BALANCE_API
from Tool import getTimestamp
from Tool_Sign import hmacSHA512
from req.InquiryBalanceReq import InquiryBalanceReq


def inquiry_Balance():
    print("=====> inquiry Balance")

    # url
    end_point_ulr = INQUIRY_BALANCE_API
    url = BASE_URL + end_point_ulr

    # access_token
    access_token = ACCESS_TOKEN

    # transaction time
    timestamp = getTimestamp()

    # partner_id
    partner_id = MERCHANT_ID
    account_no = "1024042914280502562"
    balanceTypes = ["BALANCE"]
    additionalInfo = "1024042914280502562"

    inquiry_balance_req = InquiryBalanceReq(account_no, balanceTypes, additionalInfo)

    json_data_minify = json.dumps(inquiry_balance_req, default=lambda o: o.__dict__, separators=(',', ':'))
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
