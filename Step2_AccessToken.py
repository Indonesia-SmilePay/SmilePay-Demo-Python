import json

import Tool_Sign
from Constant import ACCESS_TOKEN_API, BASE_SANDBOX_URL, BASE_URL
from Tool_PostJson import postJson
from Tool_Sign import sign

# from step1
privateKeyStr = "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCjVahxDlZ8ETxPlEoNNmgVCMbS4AAZzHfOxjiUA7sDU1S5Qpd67Wtz6+n3ycBthVynFvwWU7ICAn48OsRhNLRvLEfx3eRQwjfy1B1tUJhGwwTxzTNX3f0+uif+8GwLbf4ApscWUpDJr3B+MJj8F6PtPAaPqa3ohnmOvcBXalCMeCb6C198JdRvYzW2wtfM719Xvp3VTwEqAzcTsVynauZxBP5fAsJGNn0foOnrSQY791UB6t2CqKv4qo0J4GKVyR8Ojphi/rY5sJ8bCmL7duSoYKlnEKTX2OZC1n2MO4Kjzs9PbC5yX8qCDFXxC8vbCcrQNYfStBUNZFV8/34Fhe19AgMBAAECggEACPZ3GQcYo1O9y78fJiT1ZqwV3vX4Q3InI+NYMPUYcskElerrzYzQL+sC6nw5cTkXebrG6AG9O6N/4lW2N4BRI2WaaBENSYoy0EIoADrjNETY1Vz1g42UqzfDYJe4UhM91DLSq2yp8ctNALuxdWnlrquzz3fX6XHRo03Ry2oz09VgfowxrjapTJz4IcWM/IMSOIxO298r8Z5/Pl/KKTTEBh4MLAbht8IevG/VhNq6Fr2Sw1uUgaottiS2ChtubeyPVujGtKVJ8935pUEErrTjB41hVChyVI9ExwiMCjVZ8nahMfq4U/yCRG3YpPboy5n0CVQNDU5cIgzkFWKP1RqbwQKBgQC5GzOVSALv3PVZfTdFY+WoJAyNeqo/urpOOoUgK+9QmV+iZsH9dx7+WRgB4O3nVSwcskvqGCrZoIbJ/iEsppQ7/9KNP2wH5WxrfCQr4FltqW8UmllgikcZgtBrbcMCu1ncOLlT8qqQ7rxSk2uTy6mZeHnblQnTplPYZaUO0uC8QQKBgQDh49kbvDNM1r906vYiu+S8cYAG+vx4Dr52yHo8KY3BvITue0QCElsIWtOVOIUWpXhFZW67hKOPBAWjNBNQP2XFv8y14eMdAtp5C60uvlH3BuMjnMVTpJqxF0YUM2grWmazgzDmle3n6Z3ZWCQJHNRyPl371g+pyMzRSKOCI5ySPQKBgCfChQDyt9bH0leHguC/xWupWpzlFT6dIDl/bmrrpPreBuG+Srrj5F9jyblVlCRVciUz0wSUblfSmEE4+e06VqrQl2xJjC3iBLjNsINQLEVW2IpHYR1Qdlcvdw8sQ3AJyBJ6iKxUenipHwBps/jKDULu0tXsnHC+0FGx+5NEjotBAoGAbLQrHI+62DVXuToA7MIi1xR/mdxadqQRwDPFrwIIN70y81jaZ2zR5flfbKXgVf+XGz4uxYqU8xPqapl62dlIbptYNgbYNnPTEwEtfBsWcpwb3l1pEFFcJ/CdRsdeT86XMbfmZnCsJjhkP92Mqd331mpw6+oda4U4G1araMseY7kCgYBgSaKMTZoHcJbRZZK+SBPuslpXt9CZ9EtIFnRqrnOtY6CkAehzxDSGfIIuo/0KtGa2l5uucdPyNr0ThcGw16Bt50QqgUi4/JhUjjPHwWukTf5ne59fJ9H6+8UbaRrOc0DNmmVpVdmYzyHPbW4GpHtCpy49h0rYHcKUvJ4lZAzOXQ=="


def generate_access_token(timestamp:object):
    print("=====> step2 : Create Access Token")
    # transaction time
    # client key
    clientKey = "10006"
    # string to sign
    stringToSign = clientKey + "|" + timestamp
    # signature
    signature = sign(privateKeyStr, stringToSign)
    print("signature=", signature)
    # url
    url = BASE_URL + ACCESS_TOKEN_API
    # data
    data = {
        "grantType": "client_credentials"
    }
    json_data = json.dumps(data)
    print(json_data)
    response = postJson(url, timestamp, clientKey, signature, json_data)
    data = json.loads(response)
    return data['access_token']


# run here

timestamp = Tool_Sign.get_formatted_datetime('Asia/Bangkok')
generate_access_token(timestamp)
# if you see '2007300'. congregations! AccessToken is success
# {'responseCode': '2007300', 'responseMessage': 'Successful', 'accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE3MDEwNjUzMTMsImV4cCI6MTcwMTA2NjIxMywiaWF0IjoxNzAxMDY1MzEzLCJNRVJDSEFOVF9JRCI6InNhbmRib3gtMTAwMDEifQ.EFRCYKIr6BOR6QodRBpEYkzEya3ZqMsbDg5yqF_K0gg', 'tokenType': 'Bearer', 'expiresIn': '900', 'additionalInfo': None}
