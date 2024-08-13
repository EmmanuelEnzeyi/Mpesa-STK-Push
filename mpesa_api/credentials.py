import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2bCredential:
    consumer_key = 'mX9gahGcxr4RQG31QSychrwn4Beddt3s'
    consumer_secret = 'LKFAU3Csmq7JAV4u'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "6211013"
    OffSetValue = '0'
    passkey = 'XdPmvdqgJpwZQi6SNvva2bVWi1aXpu9kGYhhlpPQDsX2XV9rmbHlBsZ86MNTFDVByo/sMWA+qTxzXZZLcr8ZwADdDIfjzlqHqzQbv4EJn67qWlLSg5fw37wxfiaDZP7I4+lwyeT1+cqIVCb+Gnjw9LB9aD7Blb8RDKQvgl+2uVSUZT3b7roCeY+m5ZbFLFTWTVAIb4+T/8SMlMUaTsp4POp2dyR5K6DKm8ROPTFziiWW7FM/I6tT9p2cZlAF8EiuhQZpqU/EM1twhtH9ySsFGuXF4NhIY7vLbaLo1RNdX7VBMnfPG2J1RRIHryDi9vn3Xe5zXBMen/vXWjqJ9Ql1PQ=='

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
