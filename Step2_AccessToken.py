import json

from Constant import ACCESS_TOKEN_API, BASE_URL, MERCHANT_ID
from Tool import postJson, getTimestamp
from Tool_Sign import sign

# from step1
privateKeyStr = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDKLGRhtFQeghjAVl0FUa8artenjI57cZxvo5OaZmTLoDgtMWAC4T38RQ6I5nQFYP1LZlgHZlYxD0s8eI2gg3YgIW+D5BUBmZefvyl0ZtVrNRAGTeMxMa8k0fyJhlm2cIi181Xim7n5jHaIrrD6e7+B2StMOUlYgf/qEEQIb9MUgKMVECZBMwlbJHDsEjp9f/bPecQLYi6bkbVDo2Io3m1apG4Um2v8hykNvIsI6hY8FY9i+bXFYqS6x+F41w10S4BUVMprFlihPdzv/jqYDITSZciGZrGQPtZfpvKApb/5TCTOQZ1MXVyHAZn9VYOsfAQnUL83k9eZoZkU8YDzrrDTAgMBAAECggEAAhhN3ZTrFQcMSM+JFp+4wxVSII2izlTbjGz//9oVK+aYBNPdprn8+ySGC+7pzEJ4hw1jVrqw18CzHi6YaedJOpHOIFClOeDrD5mazUN7IHZdmT5TK9sHCxUhjkh2A1KmmZtEMqoIowIMs/1Ha5kLrEWuHq1hsEj/xPk9LNWbAaJDSQFJnO+GfEHaYZJlr5tFGu1Q4Z++lkfoRGeIew4BB6F2m/hMLpsbRTxBQxmifTQoI3L37q4GALWEC1fcTso4Yw1p6L+kjsPCnfQ70HZW+VymBUPSBZpfYNo2e4UFVDFmo9DgGjI+Mll4snLjacAaT0/YQ6DjRdsyDSh/EpSKBQKBgQDYQhmH55za64bn/T5fWpoYrdhdPeag0o11nPWLL9niu+vA1xsPrvDFeY9S8AZRXm/fwqQe1Q/vADRBspbuwIwbCoSnFrrhMYTiPjiaaxC2P6CNsk6b39BBkpfls8DHsDQo93lt2YgzANX7imvJ+qaQ184/V5VllVTbUeBV1wbS5QKBgQDvU6vIhirs9oStmkgNzLOc/f+3WJMcO4Ee2a7TUhn1jZwMts7AKTbWDHVCStbhdpqpoVl6uSbDBgn48XMHf922dc4d6lV4aekWZXRJoAOsAS0hE49wMNRyCPZrtYVjysKM0KtXHc8YfOiwddveBRmyaOWdI00UqZzh0VYRHB+hVwKBgHkjdbe6VxQOkRBMvG6fiug+IZABh7oYl6MFXEoucMfgamwoUoFTho2nzVAxIejclKBsIJEg2n8PxzXx+zgcZZ8UIkCSq/ZPTdeJ8R0W0lK0i5Q0CHKqSbchjbLfISL6og08qymMjA297x+rZzvKCxnhuSekQQyZPOJqF9cdzzW9AoGBALp4j/UqjJGbNh9pgVC3OQ9OXIsHiX/K4T0fUPc4Fh/cGUVSvl68/gvjIw3m7+w2FCWtIOHdF1WHBAgiYITsXNyIh3OJnNS4eLNJk0S2V4YSWI5YBj/c2/qJ/y5G/cqWNeWvxICZKj4jPM4Y1pnzkWUQFC/OTIWX7jOIfq3QItj7AoGBAIyEz8W1nAmJy/memRayZ719foYymp9rO7fY0cc0SUtFNkmMz3Jdvy0Rh36x8/b0e3IKJxElm7E/+y5sfnZAt1ZgYmcpqMXz1bfl7Y5514lO0vJcWZ0aM/4/CUUoCqBdPoTJmIM+3qJTh0gApsOo8YFnL2SlXHrw0JxiK2F9zWMi"


def generate_access_token():
    print("=====> step2 : Create Access Token")
    # transaction time
    timestamp = getTimestamp()
    # client key
    clientKey = MERCHANT_ID
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
    return response["accessToken"]

# run here

# timestamp = Tool_Sign.get_formatted_datetime('Asia/Bangkok')
# generate_access_token(timestamp)
# if you see '2007300'. congregations! AccessToken is success
# {'responseCode': '2007300', 'responseMessage': 'Successful', 'accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE3MDEwNjUzMTMsImV4cCI6MTcwMTA2NjIxMywiaWF0IjoxNzAxMDY1MzEzLCJNRVJDSEFOVF9JRCI6InNhbmRib3gtMTAwMDEifQ.EFRCYKIr6BOR6QodRBpEYkzEya3ZqMsbDg5yqF_K0gg', 'tokenType': 'Bearer', 'expiresIn': '900', 'additionalInfo': None}
