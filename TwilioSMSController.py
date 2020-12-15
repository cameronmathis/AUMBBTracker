# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from auth import (
    twilioAccountSID,
    twilioAuthToken,
    twilioPhoneNumber
)

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = twilioAccountSID
auth_token = twilioAuthToken
client = Client(account_sid, auth_token)

'''
Sends a text

Parameters: 
    txt - the text to be sent
    num - the number to send the text to
'''
def sendSMS(msg, num):
    message = client.messages \
                    .create(
                        body=msg,
                        from_= twilioPhoneNumber,
                        to=num
                    )              
    print(f"\nMessage sent with sid: {message.sid}\n")