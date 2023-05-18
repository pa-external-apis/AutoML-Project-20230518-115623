
import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if (
        allowed
        and not os.environ.get("PYTHONHTTPSVERIFY", "")
        and getattr(ssl, "_create_unverified_context", None)
    ):
        ssl._create_default_https_context = ssl._create_unverified_context

def classify_loan(testdata):

    allowSelfSignedHttps(
        True
    )


    url = os.environ["ENDPOINT_URI"]
    api_key = os.environ["ENDPOINT_KEY"]  # Replace this with the API key for the web service

    headers = {
        "Content-Type": "application/json",
        "Authorization": ("Bearer " + api_key),
        "azureml-model-deployment": "marketingautomldeploy",
    }
    
    
    data = {"Inputs": {"data": [testdata]}, "GlobalParameters": {"method": "predict"}}

    body = str.encode(json.dumps(data))
    
    print("body:",body)
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read().decode("utf8", "ignore")
        print("reached here")
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the request ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(error.read().decode("utf8", "ignore"))
    return None
    
    