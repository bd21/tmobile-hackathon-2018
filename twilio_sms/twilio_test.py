from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse

account_sid = "ACd42b430709743241a44c295b0dad4eac"
auth_token  = "2a36286b35a488fcb6cb11822606e367"
client = Client(account_sid, auth_token)



message = client.messages.create(
    to="+13605217570",
    from_="+12062079572",
    body="Hello from Python!")
#

# request.values.get('From')
# request.values.get('To')
# print(message.sid)

for sms in client.messages.list():
    print(sms.to)


# message = client.messages("MM800f449d0399ed014aae2bcc0cc2f2ec") \
#                 .fetch()
#
# print(message.body)

response = MessagingResponse()
response.message('Store Location: 123 Easy St.')

print(response)
