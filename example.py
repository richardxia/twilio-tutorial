import requests

ACCOUNT_SID = None
AUTH_TOKEN = None
FROM_NUMBER = None

# Send text message
response = requests.post(
    'https://{account_sid}:{auth_token}@api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'.format(
        account_sid=ACCOUNT_SID,
        auth_token=AUTH_TOKEN,
    ),
    data={'From': FROM_NUMBER,
          'To': 'PHONE_NUMBER_GOES_HERE',
          'Body': "Hello!"},
)
print response.status_code
print response.content

# Get message details
#response = requests.get(
#    'https://{account_sid}:{auth_token}@api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}.json'.format(
#        account_sid=ACCOUNT_SID,
#        auth_token=AUTH_TOKEN,
#        message_sid='MESSAGE_SID_GOES_HERE',
#    ),
#)
#print response.status_code
#print response.content
