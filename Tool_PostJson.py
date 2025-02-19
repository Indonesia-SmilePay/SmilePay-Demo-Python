import requests


# Generating Signatures with Crypto
def postJson(url: object, timestamp: object, clientKey: object, signature: object, json_data: object) -> object:
    # header
    headers = {
        'Content-Type': 'application/json',
        'X-TIMESTAMP': timestamp,
        'X-CLIENT-KEY': clientKey,
        'X-SIGNATURE': signature,
    }
    # POST request
    print("==request url:" + url)
    response = requests.post(url, data=json_data, headers=headers)
    # Get response result
    result = response.json()
    print(result)
    return result
