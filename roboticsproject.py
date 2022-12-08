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

#User inputs for number of obstacles:
obs_number=int(input('Enter the number of obstacles:'))

#Coordinates as put by the user:
start_coordinates=[start_coordinates_x, start_coordinates_y] #Creating a list of the starting coordinates on map, input by the user
target_coordinates=[target_coordinates_x, target_coordinates_y] #Creating a list of the target coordinates on map, input by the user
anim = VehicleIcon('panther.png', scale =7) #Creating a variable for the robot that's used on the map and animating it


veh = Bicycle(
animation= anim, #Animates the motion of the robot
   control= RandomPath, #Generates a random path for robot to move in
   dim=50, #Dimention of the grid
   x0= (start_coordinates_x, start_coordinates_y, 0) #sets angle and coordinates 
   )

veh.init(plot=True)
veh._animation.update(veh.x)  

target_marker_style={ #Creating the obstacles
    'marker':'*', #Obstacle shape
    'markersize': '10', #Obstacle size
    'color': 'pink' #Obstacle colour
}

plt.plot(target_coordinates_x, target_coordinates_y, **target_marker_style)
plt.plot()

goal_heading=atan2( #Calculating the distance to the target goal
    target_coordinates[1]-veh.x[1     ], 
    target_coordinates[0]-veh.x[0]
    )


map=LandmarkMap(obs_number,50) #Creates a variable of the map, using the obstacle input and a dimension of 50
map.plot()
image = mpimg.imread("map.png")
plt.imshow(image, extent = [-50,50,-50,50]) #Generates the map and stretches the grid across the x and y axis

sensor=RangeBearingSensor(robot=veh,map=map,animate=True) #Reads and measures the angle and the distance between the vehicle and the obstacle

print('Sensor Readings: \n ', sensor.h(veh.x)) #Prints the sensor readings and calculates it


run=True
while(run):
    goal_heading=atan2( #Calculating the distance to the target goal
                target_coordinates[1]-veh.x[1], 
                target_coordinates[0]-veh.x[0]
            )
    steer = goal_heading- veh.x[2]
    veh.step(2,steer) #Speed of the Vehicleh.
    if((abs(target_coordinates[0]-veh.x[0]) >0.05) or (abs(target_coordinates[1]-vex[1]) > 0.05)): #If condition: if the vehicle is >0.05 away from the target, the robot 
         run=True
         for i in sensor.h(veh.x):
             if (i[0] < 3): check diis from obs les #If the robot is within a distance of 3 from the obstacle, it runs the angle command
                if(abs(i[1]) < pi/4): #If the angle is within pi/4 from the obstacle, it runs the step command
                    veh.step(2,pi/2) #If the distance and angle are not within range, the robot moves in steps of pi/2

    else:
       run=False #If there are no obstacles, it disregards the IF condition and carries on moving.
    veh._animation.update(veh.x)
    plt.pause(0.005)



plt.pause(1000) #nunber of seconds the map will be displayed
