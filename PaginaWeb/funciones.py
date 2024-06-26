
import base64
import requests


PAYPAL_CLIENT_ID = 'AaJMhZKXGuDY2evK_NtTFbpxZ20ajqV2JtPgBWpOGkOBSwwXmgtub-Kh8f1sNmL9Mq2gwlL3v44aprYJ'
PAYPAL_CLIENT_SECRET ='EHRbkPAm3vgST8QI0wWLYs1m52YOtLezXTf6KbCQYIrkT8rXgTgAzbU5lHMcGSCEhaiMEGxzlPcPbcyS'
BASE_URL = "https://api-m.sandbox.paypal.com"

def generateAccessToken():
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        raise ValueError('no existen credenciales')
    
    auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
    auth = base64.b64encode(auth.encode()).decode('utf-8')
    
    respose = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        
        data={"grant_type": "client_credentials"},
        headers={"authorization":f"basics {auth}"}
    )
    
    data = respose.json() 

    return data['access_token']


def create_order(Productos):
    print(Productos)

    try:
        access_token = generateAccessToken()

        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
        
        payload = {
                "intent" : "CAPTURE",
                "purchase_units" : [{
                    "amount" : {
                       "currency_code" : "CLP",
                       "Values" : "1"
                    }
                }
            ]
        }

        headers = {
            "Content-Type" : "application/json",
            "Authotization": f"Bearer {access_token}"
        }

        response = requests.post(url, headers=headers, json=payload)

        return response.json()
    
    except Exception as error:
        print (error)