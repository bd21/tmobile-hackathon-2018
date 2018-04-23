from requests import put, get, post
import csv
import apiRequests
import time

workspace_data = get('http://tmobilehack.azurewebsites.net/workspaces').json()

def get_room_name(number):
    for room in workspace_data:
        if int(workspace_data[room]["index"]) == number:
            return room
    return None

# increases time step
MULT = 5

with open('paths.csv', 'r') as csvfile:
    reads = csv.reader(csvfile)
    idx = 0
    start_time = None
    for line in reads:
        if idx == 0:
            idx += 1
            continue
        length = float(line[1]) * MULT
        if not start_time:
            duration = 0.25 * MULT
        else:
            duration = length - start_time
        start_time = length
        print(line)
        room_from = get_room_name(int(line[2]))
        room_to = get_room_name(int(line[3]))
        amount = int(line[4])
        if room_from in workspace_data and room_to in workspace_data:
            old_amount_from = workspace_data[room_from]["used"]
            old_amount_to = workspace_data[room_to]["used"]
            workspace_data[room_from]["used"] -= amount
            workspace_data[room_to]["used"] += amount
            apiRequests.putCheckIn(room_from, -amount)
            apiRequests.putCheckIn(room_to, amount)

        idx += 1
        print(duration)
        time.sleep(duration)
