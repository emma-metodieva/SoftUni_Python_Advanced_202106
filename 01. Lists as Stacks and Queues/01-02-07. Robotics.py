# 01-02. Lists as Stacks and Queues - Exercise
# 07. Robotics

import datetime
from collections import deque

robots_list = input().split(';')
hh, mm, ss = input().split(':')
products = deque()

robots = {}
for robot_id, robot_data in enumerate(robots_list):
    name = robot_data.split('-')[0]
    processing_time = int(robot_data.split('-')[1])

    robot = {}
    robot['name'] = name
    robot['process_time'] = processing_time
    robot['status'] = 0  # =0: free; >0: busy

    robots.update({robot_id: robot})

while True:
    command = input()
    if command == 'End':
        break
    else:
        products.append(command)

t = int(ss) + int(mm) * 60 + int(hh) * 60 ** 2
while products:
    t += 1
    if t == 86400:
        t = 0
    processing = False

    for r in range(len(robots)):
        if robots[r]['status'] > 0:
            robots[r]['status'] -= 1

        if not processing and robots[r]['status'] == 0:
            robots[r]['status'] = robots[r]['process_time']
            processing = True
            print(f"{robots[r]['name']} - {products.popleft()} [{'{:0>8}'.format(str(datetime.timedelta(seconds=t)))}]")

    if not processing:
        products.rotate(-1)
