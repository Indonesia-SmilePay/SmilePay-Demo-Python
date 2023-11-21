import requests


# Generating Signatures with Crypto
def postJson(url, timestamp, clientKey, signature, json_data):
    # header
    headers = {
        'Content-Type': 'application/json',
        'X-TIMESTAMP': timestamp,
        'X-CLIENT-KEY': clientKey,
        'X-SIGNATURE': signature,
    }
    # POST request
    response = requests.post(url, data=json_data, headers=headers)
    # Get response result
    result = response.json()
    print(result)
