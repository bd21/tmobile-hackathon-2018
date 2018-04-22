from requests import put, get, post
from datetime import datetime

def putCheckIn(name, number):
    return put('http://tmobilehack.azurewebsites.net/echo', data={'name': name, 'data': number}).json()

def putCheckOut(name, number):
    return put('http://tmobilehack.azurewebsites.net/echo', data={'name': name, 'data': -number}).json()

def getOpenSpaces(room):
    return put('http://tmobilehack.azurewebsites.net/echo', data={'name': room, 'data': 0}).json()

def putReservation(number, hour):
    return put('http://tmobilehack.azurewebsites.net/reserve', data={'number': number, 'hour': hour}).json()

def cancelReservation(hour, room):
    return put('http://tmobilehack.azurewebsites.net/cancel', data={'room': room, 'hour': hour}).json()

def getReservation():
    return get('http://tmobilehack.azurewebsites.net/reserve').json()

def getBestRoom():
    return get('http://tmobilehack.azurewebsites.net/twilio/workspaces/best').json()

def getWorkspaces():
    return get('http://tmobilehack.azurewebsites.net/twilio/workspaces/all').json()

def twilioPost():
    return get('http://tmobilehack.azurewebsites.net/twilio/all/all').json()

def getGarageData(garage):
    return put('http://tmobilehack.azurewebsites.net/garages', data={'type': 'data', 'garage': garage}).json()

def incrementGarage(garage):
    return put('http://tmobilehack.azurewebsites.net/garages', data={'type': 'in', 'garage': garage}).json()

def decrementGarage(garage):
    return put('http://tmobilehack.azurewebsites.net/garages', data={'type': 'out', 'garage': garage}).json()

def getBestGarage():
    return put('http://tmobilehack.azurewebsites.net/garages', data={'type': 'best', 'garage': 'none'}).json()

#print(putCheckIn("Multipurpose Room 1", 5))
# print(cancelReservation(11, "Workspace 2"))
# print(putCheckOut("Table Room 1", 10))
print(getBestGarage())
print(getGarageData('all'))
incrementGarage("Newport 2")
print(getGarageData("Newport 2"))
# print(getBestGarage())
# print(getReservation())

# print(putCheckIn("Multipurpose Room 1", 15))
