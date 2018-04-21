from twilio.rest import Client

account_sid = "ACd42b430709743241a44c295b0dad4eac"
auth_token  = "2a36286b35a488fcb6cb11822606e367"
client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+13605217570",
#     from_="+12062079572",
#     body="Hello from Python!")
#
# print(message.sid)

for sms in client.messages.list():
    print(sms.to)
