'''
Earth Systems - Detect Earthquakes
Last Updated: 12-11-2018
Author: QiLin Xue
Designer: Ethan Wang
'''

import detector, quake

detectionUnits = []
quakeList = []
simulation = []

min_magnitude = -1

'''
Load Files
'''
with open("qilin-detectionUnits.txt","r") as f:
    for line in f:
        newline = [float(i) for i in line.rstrip().split(",")]
        detectionUnits.append(newline)

with open("qilin-earthquakeLocations.txt","r") as f:
    for line in f:
        newline = [float(i) for i in line.rstrip().split(",")]
        quakeList.append(newline)

with open("qilin-simulation.txt","r") as f:
    min_magnitude = float(f.readline())
    for line in f:
        newline = [float(i) for i in line.rstrip().split(",")]
        simulation.append(newline)

'''Code to load in the objects
'''

quake_object_list = []
for j in simulation:
    xpos = j[0]
    ypos = j[1]
    period = j[2]
    power = j[3]
    decay = j[4]
    speed = j[5]

    temp = quake.Quake(xpos,ypos,period,power,decay,speed)
    quake_object_list.append(temp)

detector_object_list = []
for j in detectionUnits:
    xpos = j[0]
    ypos = j[1]
    radius = j[2]
    min_quake = j[3]

    temp = detector.Detector(xpos,ypos,radius,min_quake)
    detector_object_list.append(temp)

'''Initialize and run the field
'''


import field
mainField = field.Field(detector_object_list,quake_object_list)

mainField.run()