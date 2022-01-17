## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Feature](#feature)
* [Use](#use)

## General info
This robotics colledge project is about determening robot's pitch and roll angle while driving. Robot used in this project is [Scout Mini](quora.com/profile/Ashish-Kulkarni-100) from Agilex. 
	
## Technologies
Project is created with:
* ROS
* Python

## Feature
Project will be helpful in many practical uses of robot:
* while carying high load, determening the overroll angle
* improvement of robot's stability

## Use
There are two programs, acc.py for reading a bag file and acceleration.py that subscribes to topic "/odom". Both programs are capable of calculating longitudinal load transfet that is used to determin pitch angle. Typically, the odometry (/odom topic) describes the "internal" state of the robot, i.e. the integrated position using wheel encoders. It is not very precise measure of robot's movements but it is good for this kinf of operation. Later on, program (acceleration.py) can be used to subscribe to node "/odom" so we can get measurements of angles in real time while driving the robot.

### To do:
* roll angle
