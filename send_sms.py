from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC00b0db4128bdf9e869bed9ec08e8xxxx"  //check your account
auth_token = "9887b585dd9f708da2a154f33cd4xxxx"     //check your account
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+xxx", from_="+twilio_number",
                                     body="Hello there!")
