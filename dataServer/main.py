from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
from datetime import datetime, timedelta
from threading import Timer
import time

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

# available 2 = fully available
# available 1 = reserved but not checked in yet (before deadline)
# available 0 = reserved and checked in

workspaces = {  "Workspace 1": {"index": 1, "cap": 12, "used": 0, "available": 2},
                "Workspace 2": {"index": 2, "cap": 18, "used": 0, "available": 2},
                "Project Room 1": {"index": 3, "cap": 11, "used": 0, "available": 2},
                "Small Project Room 1": {"index": 4, "cap": 3, "used": 0, "available": 2},
                "Small Project Room 2": {"index": 5, "cap": 3, "used": 0, "available": 2},
                "Small Project Room 3": {"index": 6, "cap": 2, "used": 0, "available": 2},
                "Small Project Room 4": {"index": 7, "cap": 2, "used": 0, "available": 2},
                "Small Project Room 5": {"index": 8, "cap": 2, "used": 0, "available": 2},
                "Workspace 3": {"index": 9, "cap": 19, "used": 0, "available": 2},
                "Small Project Room 6": {"index": 10, "cap": 6, "used": 0, "available": 2},
                "Multipurpose Room 1": {"index": 11, "cap": 32, "used": 0, "available": 2},
                "Cafe": {"index": 12, "cap": 26, "used": 0, "available": 2},
                "Big Workspace 1": {"index": 13, "cap": 29, "used": 0, "available": 2},
                "Table Room 1": {"index": 14, "cap": 16, "used": 0, "available": 2},
                "Small Project Room 7": {"index": 15, "cap": 5, "used": 0, "available": 2},
                "Lobby": {"index": 16, "cap": 4, "used": 0, "available": 2},
                "Weird Room 1": {"index": 17, "cap": 14, "used": 0, "available": 2},
                "Small Project Room 8": {"index": 18, "cap": 4, "used": 0, "available": 2},
                "Small Project Room 9": {"index": 19, "cap": 4, "used": 0, "available": 2},
                "Small Project Room 10": {"index": 20, "cap": 10, "used": 0, "available": 2},
                "Small Project Room 11": {"index": 21, "cap": 14, "used": 0, "available": 2},
                "Small Project Room 12": {"index": 22, "cap": 3, "used": 0, "available": 2},
                "Small Project Room 13": {"index": 23, "cap": 3, "used": 0, "available": 2},
                "Small Project Room 14": {"index": 24, "cap": 4, "used": 0, "available": 2},
                "Project Room 2": {"index": 25, "cap": 14, "used": 0, "available": 2},
                "Project Room 3": {"index": 26, "cap": 11, "used": 0, "available": 2}
                }

garages = {
                "Newport 2": {"available": 51},
                "Newport Tower": {"available": 18},
                "Newport Terrace": {"available": 83},
                "Newport 4": {"available": 101},
                "Newport 5": {"available": 8},
                "Crossroads Bible Church": {"available": 19},
                "Eastgate Bible Fellowship": {"available": 30},
}

# list of maps from time to room
reservations = []

# def checkOutTime(res):
#     hour = res["hour"]
#     room = res["room"]
#     if res in reservations:
#         reservations.remove(res)
#     workspaces[room]["available"] = 2
#
# def timeOut(res):
#     hour = res["hour"]
#     room = res["room"]
#     if workspaces[room]["available"] == 0:
#         Timer(55 * 60, checkOutTime, args=[res]).start()
#     elif res in reservations:
#         reservations.remove(res)
#         workspaces[room]["available"] = 2
#
# def checkInTime(res):
#     print(res)
#     hour = res["hour"]
#     room = res["room"]
#     workspaces["Multipurpose Room 1"]["used"] = 5000
#     print(room)
#     print(hour)
#     if workspaces[room]["available"] == 0:
#         Timer(60 * 60, checkOutTime, args=[res]).start()
#     else:
#         workspaces[room]["available"] = 1
#         Timer(5 * 60, timeOut, args=[res]).start()


class Garages(Resource):
    def put(self):
        garage = request.form["garage"]
        type = request.form["type"]
        if type == "best" or garage == "none":
            mostAvailable = 0
            best = None
            for gary in garages:
                if not best or int(garages[gary]["available"]) > mostAvailable or garages[gary]["available"] == mostAvailable:
                    best = gary
                    mostAvailable = int(garages[gary]["available"])
            return best
        if type == "data":
            if garage in garages:
                return garages[garage]["available"]
            else:
                return garages
        elif type == "in":
            garages[garage]["available"] += 1
            return garages
        elif type == "out":
            garages[garage]["available"] -= 1
            return garages
        else:
            return "failed"
    def get(self):
        return garages

class Workspaces(Resource):
    def get(self):
        return workspaces

class Twilio(Resource):
    def get(self, type, req):
        if type == "workspaces":
            if req == "all":
                return workspaces
            elif req == "best":
                best = None
                most = 0
                for workspace in workspaces:
                    cap = workspaces[workspace]["cap"]
                    taken = workspaces[workspace]["used"]
                    available = cap - taken
                    if not best or available > most:
                        best = workspace
                        most = available
                return [best, most]
        elif type == "all":
            if req == "all":
                return {"workspaces": workspaces, "garages": garages}


class Echo(Resource):
    def put(self): # check into room
        number = int(request.form["data"])
        name = request.form["name"]
        if number == 0:
            for workspace in workspaces:
                if name.lower() == workspace.lower():
                    return int(workspaces[workspace]["cap"]) - int(workspaces[workspace]["used"])
        found = False
        space = ""
        for workspace in workspaces:
            if name.lower() == workspace.lower():
                found = True
                space = workspace
        if not found:
            return "failed"
        workspaces[space]["used"] += int(number)
        workspaces[space]["available"] = 0
        return workspaces

class Reserve(Resource):
    def put(self):
        number = request.form["number"]
        hour = request.form["hour"]
        possibleSpaces = list(workspaces.keys()).copy()
        if not reservations or len(reservations) == 0:
            for space in workspaces:
                if workspaces[space]["cap"] >= int(number):
                    reserveRoomAtTime(space, hour)
                    return space
            return "No Available Rooms"

        for res in reservations:
            resTime = res["hour"]
            if int(hour) == int(resTime) and res["room"] in possibleSpaces:
                possibleSpaces.remove(res["room"])

        for space in possibleSpaces:
            if int(workspaces[space]["cap"]) >= int(number):
                reserveRoomAtTime(space, hour)
                return space
        return "No Available Rooms"

    def get(self):
        return reservations

class Cancel(Resource):
    def put(self):
        room = request.form["room"]
        hour = request.form["hour"]
        for res in reservations:
            if res["room"] == room and res["hour"] == hour:
                reservations.remove(res)
                return "success"
        return "failed"

    def get(self):
        # clear the db
        for workspace in workspaces:
            workspaces[workspace]["used"] = 0
            workspaces[workspace]["available"] = 2
        reserved = []


def reserveRoomAtTime(room, hour):
    res = {
        "hour": hour,
        "room": room,
    }
    reservations.append(res)
    reservations.sort(key=lambda x: int(x["hour"]) - datetime.now().hour)
    numHours = int(hour) - int(datetime.now().hour)
    numMinutes = int(datetime.now().minute) + numHours * 60
    # t = Timer(numMinutes * 60, checkInTime, args=[res])
    # t.start()

#
# class Tracks(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)
#
# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)




api.add_resource(Garages, '/garages') # Route_1
api.add_resource(Workspaces, '/workspaces') # Route_1
api.add_resource(Echo, '/echo')
api.add_resource(Twilio, '/twilio/<string:type>/<string:req>')
api.add_resource(Reserve, '/reserve')
api.add_resource(Cancel, '/cancel')
#api.add_resource(Unity, '/unity') # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3

if __name__ == '__main__':
     app.run(port=5002)
