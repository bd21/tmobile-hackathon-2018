from requests import put, get, post
from datetime import datetime

def putCheckIn(name, number):
    return put('http://tmobilehack.azurewebsites.net/echo', data={'name': name, 'data': number}).json()

def putReservation(number, hour):
    return put('http://tmobilehack.azurewebsites.net/reserve', data={'number': number, 'hour': hour}).json()

def getReservation():
    return get('http://tmobilehack.azurewebsites.net/reserve').json()

def getBestRoom():
    return get('http://tmobilehack.azurewebsites.net/twilio/workspaces/best').json()

def getWorkspaces():
    return get('http://tmobilehack.azurewebsites.net/twilio/workspaces/all').json()

def twilioPost():
    return get('http://tmobilehack.azurewebsites.net/twilio/all/all').json()

print(putReservation(30, 2))
print(getReservation())
