#Libraries imported:
from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap
from math import pi, atan2, sqrt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


#User inputs for starting coordinates:
start_coordinates_x= float(input("Enter starting X coordinates of the robot: "))
start_coordinates_y= float(input("Enter starting Y coordinates of the robot: ")) 

#User inputs for target coordinates:
target_coordinates_x = float(input("Enter your targets X coordinates: ")) 
target_coordinates_y= float(input("Enter your targets Y coordinates: "))


obs_number=int(input('Enter the number of obstacles:'))

#Coordinates as put by the user:
start_coordinates=[start_coordinates_x, start_coordinates_y] #Starting coordinates on map, input by the user
target_coordinates=[target_coordinates_x, target_coordinates_y] #Target coordinates on map, input by the user
anim = VehicleIcon('panther.png', scale =5) #Creating a variable for the robot that's used on the map


veh = Bicycle(
animation= anim,
   control= RandomPath,
   dim=50, 
   x0= (start_coordinates_x, start_coordinates_y, 0)
   )

veh.init(plot=True)
veh._animation.update(veh.x)  

target_marker_style={
    'marker':'*',
    'markersize': '10',
    'color': 'pink'
}

plt.plot(target_coordinates_x, target_coordinates_y, **target_marker_style)
plt.plot()

goal_heading=atan2(
    target_coordinates[1]-veh.x[1     ], 
    target_coordinates[0]-veh.x[0]
    )


map=LandmarkMap(obs_number,50) 
map.plot()
image = mpimg.imread("map.png")
plt.imshow(image, extent = [-50,50,-50,50])

sensor=RangeBearingSensor(robot=veh,map=map,animate=True) 

print('Sensor Readings: \n ', sensor.h(veh.x))


run=True
while(run):
    goal_heading=atan2(
                target_coordinates[1]-veh.x[1], 
                target_coordinates[0]-veh.x[0]
            )
    steer = goal_heading- veh.x[2]
    veh.step(2,steer)
    if((abs(target_coordinates[0]-veh.x[0]) >0.05) or (abs(target_coordinates[1]-veh.x[1]) > 0.05)):
         run=True
         for i in sensor.h(veh.x):
             if (i[0] < 3):
                if(abs(i[1]) < pi/4):
                    veh.step(2,pi/2)

    else:
       run=False 
    veh._animation.update(veh.x)
    plt.pause(0.005)



plt.pause(1000)