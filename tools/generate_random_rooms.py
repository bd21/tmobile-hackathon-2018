from requests import put, get, post
import csv
import apiRequests
import time

def get_room_name(number):
   workspace_data = get('http://tmobilehack.azurewebsites.net/workspaces').json()
   for room in workspace_data:
       if int(workspace_data[room]["index"]) == number:
           return room
   return None

# set of rooms
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

with open('paths.csv', 'r') as csvfile:
   write = csv.writer(csvfile)
   idx = 0
   workspace_data = get('http://tmobilehack.azurewebsites.net/workspaces').json()
   start_time = None
   for line in AAAAAAAAAA:
       if idx == 0:
           print("skipping")
           idx += 1
           continue
       length = float(line[0])# * 500
       if not start_time:
           start_time = length
       if line[1]:
           room = get_room_name(int(line[1]))
       print(length)
       people = int(line[2])
       
       idx += 1
       time.sleep(length)