from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import requests


SECRET_KEY = 'a_secret_key'
app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_process():
    ''' handles incoming sms and sends a response. '''

    # Increment the counter and save in session
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter

    # if it's a new session, reset params
    if session['counter'] == 1:
        session['params'] = None

    # check session vars
    print("Counter: ", session['counter'])
    print(session['params'])

    # store message sid for later identification
    sms_sid = request.values.get('MessageSid')

    # extract body of incoming text
    sms_body = request.values.get('Body').lower().strip()

    # to restart
    if sms_body == 'quit':
        session['counter'] = 0
        session['params'] = None

        response = "Session restarted."
        resp = MessagingResponse()
        resp.message(response)
        print(response)
        return str(resp)

    # check if session "need" has been set
    if session['params'] is None:
        # if not, then parse the message body for either 'parking' or 'workspaces', else restart
        if sms_body in ['parking','workspaces']:
            session['params'] = {'need': sms_body}
            need = sms_body
        else:
            response = "Error: Please text either 'workspaces' or 'parking'"
            resp = MessagingResponse()
            resp.message(response)
            session['counter'] = 0
            session['params'] = None
            print(response)
            return str(resp)

    # handle incoming sms message
    processor = HandleIncomingMessage(session['params'], sms_body, sms_sid, counter)
    response = processor.GetResponse()
    updated_counter = processor.GetCounter()
    updated_params = processor.GetParams()

    print(sms_body)
    print(response)

    # update counter upon successful message receipt, before responding
    session['counter'] = updated_counter
    session['params'] = updated_params
    print('new counter', updated_counter)

    # make response to phone
    resp = MessagingResponse()
    resp.message(response)

    return str(resp)



class HandleIncomingMessage(object):
    ''' handles an incoming text message with parameters:
            params: session parameters
            sms_body: content of text message
            sms_sid: unique id of text message
            counter: session counter used to continue conversation

        Returns a response to be used as a texted reply '''
    def __init__(self, params, sms_body, sms_sid, counter):
        self.params = params
        self.body = sms_body
        self.sid = sms_sid
        self.counter = counter
        self.response = None

    def GetResponse(self):

        # validate response based on session counter
        is_error, msg = self._validate_response()
        if is_error is True:
            self.counter -= 1
            return msg

        # send request based on need
        if self.params['need'] == 'workspaces':
            return self.ParseWorkspaceRequest()
        elif self.params['need'] == 'parking':
            return self.ParseParkingRequest()

    def ParseWorkspaceRequest(self):
        if self.counter == 1:
            msg = 'How many people are meeting?'
            return msg

        elif self.counter == 2:
            self.params['people'] = self.body
            msg = 'What time are you booking?'
            return msg

        elif self.counter == 3:
            self.params['time'] = self.body

            # request to book a room
            rcd = RequestCurrentData(self.params)
            msg, room = rcd.GetBestRoom()
            self.params['room'] = room

            return msg

        elif self.counter == 4:

            if self.body == 'no':
                rcd = RequestCurrentData(self.params)
                rcd.CancelBooking()
                msg = 'You have canceled the room.'
                self.counter = 0
                self.params = None
            else:
                msg = "To cancel your reservation reply 'no'. Otherwise ignore this message or type 'quit' to restart."
                self.counter -= 1

            return msg


    def ParseParkingRequest(self):
        return "Parking has not been implemented yet."

    def GetCounter(self):
        return self.counter

    def GetParams(self):
        return self.params

    def _validate_response(self):
        ''' validates response based on conversation counter '''
        if self.counter == 1:
            if self.body not in ['parking','workspaces']:
                error = True
                msg = "Error: Please text either 'workspaces' or 'parking'"
                return error, msg
        elif self.counter == 2:
            if self._is_positive_int(self.body) is not True:
                error = True
                msg = "Error: Please input a positive integer."
                return error, msg
        elif self.counter == 3:
            if self._is_nonnegative_int(self.body) is not True:
                error = True
                msg = "Error: Please input a non-negative integer (0-23)."
                return error, msg
            elif int(self.body) > 23:
                error = True
                msg = "Error: Please input a non-negative integer (0-23)."
                return error, msg

        error = False
        msg = 'null'
        return error, msg

    def _is_positive_int(self, s):
        ''' makes sure input string represents a positive integer '''
        try:
            if int(s) > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def _is_nonnegative_int(self, s):
        ''' makes sure input string represents a positive integer '''
        try:
            if int(s) >= 0:
                return True
            else:
                return False
        except ValueError:
            return False


# class BookRoom(object):
#     ''' submits a booking request for a room '''
#
#     def __init__(self, ):

class RequestCurrentData(object):
    ''' Gets current room availabilities '''

    def __init__(self, params):
        self.current_data_url = 'http://tmobilehack.azurewebsites.net/reserve'
        self.cancel = 'http://tmobilehack.azurewebsites.net/cancel'
        self.params = params


    def GetBestRoom(self):

        # request current room / parking vacancies
        payload = {'hour': self.params['time'], 'number': self.params['people']}
        r = requests.put(self.current_data_url, payload)

        contents = r.json()

        formatted_message = "The following room has been reserved for you. Reply 'no' to cancel:\n" + contents

        return formatted_message, contents

    def CancelBooking(self):

        payload = {'room': self.params['room'], 'hour': self.params['time']}
        print(payload)
        r = requests.put(self.cancel, payload)

# class Session(object):
#
#     def __init__(self, cell_num):
#         self.from = cell_num
#         self.counter = 0
#
#     def increment(self):
#         self.counter += 1
#
#     def reset(self):
#         self.counter = 0
#
#
# class InitializeSessionList(object):
#
#     def __init__(self):
#         self.SessionList = []
#
#     def AddSession(session):
#         self.SessionList.append(session)



def keyboard_test():
    tmp = raw_input('Enter input: ')

    # extract body of incoming text
    sms_body = tmp.lower().strip()

    # handle incoming sms message
    processor = HandleIncomingMessage(sms_body, sms_sid)
    response = processor.GetResponse()


    print(sms_body)
    print(response)



if __name__=="__main__":

    # keyboard_test()

    app.run(debug=True)
