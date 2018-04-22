from requests import put, get, post

def putCheckIn(name, number):
    return put('http://127.0.0.1:5002/echo', data={'name': name, 'data': number}).json()

def getBestRoom():
    return get('http://tmobilehack.azurewebsites.net/twilio/workspaces/best').json()

def getWorkspaces():
    return get('http://tmobilehack.azurewebsites.net/twilio/workspaces/all').json()

def twilioPost():
    return post('http://tmobilehack.azurewebsites.net/twilio').json()

#print(twilioPost())
