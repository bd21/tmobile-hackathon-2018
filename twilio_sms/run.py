from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_process():
    ''' handles incoming sms and sends a response '''

    # store message sid for later identification
    sms_sid = request.values.get('MessageSid')

    # extract body of incoming text
    sms_body = request.values.get('Body')

    # handle incoming sms message
    processor = IncomingMessage(sms_body, sms_sid)
    response = processor.Respond()

    print(sms_sid)
    print(sms_body)
    print(response)

    # make response to phone
    resp = MessagingResponse()
    resp.message(response)

    return str(resp)



class UpdateMessage():
    print('todo')


class IncomingMessage(object):

    def __init__(self, sms_body, sms_sid):
        self.body = sms_body
        self.sid = sms_sid

        if self.body == 'parking':
            pass
        elif self.body == 'workspace':
            pass

        # update_queue(self.sid)

    def Respond(self):
        return "this is a response"


if __name__=="__main__":
    app.run(debug=True)
