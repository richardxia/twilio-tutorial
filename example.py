import requests

ACCOUNT_SID = None
AUTH_TOKEN = None
FROM_NUMBER = None

response = requests.post(
    'https://{account_sid}:{auth_token}@api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages'.format(
        account_sid=ACCOUNT_SID,
        auth_token=AUTH_TOKEN,
    ),
    data={'From': FROM_NUMBER,
          'To': '+14083945058',
          'Body': "Hello!"},
)
print response.status_code
