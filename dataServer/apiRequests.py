from requests import put, get

def putCheckIn(name, number):
    return put('http://tmobilehack.azurewebsites.net/echo/' + name, data={'data': number}).json()

print(putCheckIn("hi", 5))
