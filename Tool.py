from datetime import datetime

import requests


# Generating Signatures with Crypto
def postJson(url, timestamp, clientKey, signature, json_data) -> dict:
    # header
    headers = {
        'Content-Type': 'application/json',
        'X-TIMESTAMP': timestamp,
        'X-CLIENT-KEY': clientKey,
        'X-SIGNATURE': signature,
    }

    try:
        # POST request
        print("==request url: " + url)
        print("==request timestamp:" + headers['X-TIMESTAMP'])

        response = requests.post(url, data=json_data, headers=headers)
        response.raise_for_status()

        # Get response result
        result = response.json()
        print("Response: %s", result)
        return result

    except requests.exceptions.RequestException as e:
        print("Request failed: %s", e)
        raise


def getTimestamp():
    current_time_bangkok = datetime.now()
    return current_time_bangkok.strftime('%Y-%m-%dT%H:%M:%S') + "+07:00"
