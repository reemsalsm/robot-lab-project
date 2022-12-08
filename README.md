#                                               **DOCUMENTATION**

# robot-lab-project

## **Project by:** 
- _Fatimaalzahraa Mohamed ***(202101311)***_ 
- _Reem Salem ***(202200411)***_
- _Yara Hussein ***(202100130)***_

We created a simulation of Panther walking across a maze-like course
while avoiding obstacles and reaching the target input by the user,
on Visual Studio Code using the Python programming language, for our
Introduction to Computer Engineering course's lab final.

### **Python version(s):** 
3.6 - 3.8

### **Libraries imported:** 
- roboticstoolbox
- math
- matplotlib.pyplot
- matplotlib.image
- numpy

### **Map size:**
The map simulated is stretched to a 50mx50m scale

![map](Media/Map_and_robot.jpeg)

## **User inputs:**
1. Starting coordinates *(The user **must** input **BOTH** the x & y coordinates of the starting point)*
2. Target coordinates *(The user **must** input **BOTH** the x & y coordinates of the target point)*
3. Number of obstacles *(The user **must** input the number of obstacles to be displayed in the map)*

![user inputs](Media/User_input.jpeg) 

## **Output of code:**
1. Sensor readings, which calculate and display the distance between the vehicle and the obstacles.
2. The map uploaded with an autonomous robot navigating it's way through the obstacles to reach a target point

### **Sensor Readings:**
![sensor reasdings](Media/Sensor_readings.jpeg)


Figure description: First, the user is required to enter the required points and decide whether to 
the changes in obstacle and target position, the Sensor Readings of the robots positions are then printed. 
As seen in the previous figure, the simulation is running and Panther is moving to the target, 
while avoiding collisions with the map walls and obstacles.

## **How the code works:**
The code is put together using the libraries mentioned previously
to create a simulation of a moving "vehicle", which in our case is Panther,
that is able to move from a starting point input by the user to the target point- also
input by the user, whilst avoiding numerous obstacles.
The Panther is able to identify the obstacles using "RangeBearingSensor"
and bypassing them. 

## **Areas for improvement:**
The code written to run this task has been thought through to have a simplistic approach for the user to avoid any complications or confusion in errors. It could've been improved by programming the robot to detect the map walls and avoiding collisions with them as it does obstacles. Unfortunately, the code design was sudden to meet this limitation though may be solved using a different approach of creating an array of free points and placing manual obstacles and finally placing it into a loop to create a path the robot can move in freely to reach the target. Although this method may work, it is set to meet limitations and run to a certain point.

## **Flowchart:**
![flow chart](/Media/Flowchart.png)













