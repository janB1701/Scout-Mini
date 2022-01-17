#! /usr/bin/env python3

from json import load
import rospy
import sys
import statistics
from nav_msgs.msg import Odometry

#should add class

class AngleCalculator:
    
    def __init__ (self):
        rospy.init_node ("angle_calculator", anonymous=True)

        self.subscriber_odom = rospy.Subscriber ("/odom", Odometry, self.acceleration_calculation)
        self.first_pass = True
        self.first_first = True
        self.acc = 0.0
        self.vel = 0
        self.vel1 = 0
        self.vel2 = 0
        self.time1 = 0
        self.time2 = 0
        self.cnt = 0
        self.list_of_vel = []

    def acceleration_calculation (self, msg):
        if (self.first_first): #while reading the very first info from the bag
            if self.first_pass:
                if (self.cnt == 1):
                    self.vel1 = statistics.median(self.list_of_vel) #teaking median from the velocity of first second
                    self.list_of_vel.clear()
                elif (self.cnt == 2):
                    self.vel2 = statistics.median(self.list_of_vel) #teaking median from the velocity of second second
                    self.list_of_vel.clear()
                    self.acc = self.vel2 - self.vel1    #calulating acceleration
                    self.vel1 = self.vel2;
                    print ("Acceleration: " + str(self.acc))
                    load_transfer = 20 * self.acc * (150/460)
                    if load_transfer < 0:
                        load_transfer = load_transfer * (-1)
                    print ("    load transfer: " + str (load_transfer) + " N")
                    self.cnt == 0;
                    self.first_first = False
                    self.first_pass = True
                self.time1 = msg.header.stamp.secs;
                print (self.time1)
                self.list_of_vel.append (msg.twist.twist.linear.x)
                self.first_pass = False
                self.cnt += 1
            self.time2 = msg.header.stamp.secs
            if (self.time2 == self.time1):    #looking for the first change in seconds
                self.list_of_vel.append (msg.twist.twist.linear.x)
                #print ("appendao")
            else:
                self.first_pass = True
        
        else:      #when it comes to third second of operation, vel1 becames velocity from vel2 and velocity from third second will be vel2 and so on
            if (self.first_pass): 
                self.vel2 = statistics.median(self.list_of_vel)
                self.list_of_vel.clear()

                self.time1 = msg.header.stamp.secs;
                print (self.time1)
                self.list_of_vel.append (msg.twist.twist.linear.x)
                self.first_pass = False

                self.acc = self.vel2 - self.vel1
                print ("Acceleration: " + str(self.acc))
                load_transfer = 20 * self.acc * (150/460)
                if load_transfer < 0:
                    load_transfer = load_transfer * (-1)
                print ("    load transfer: " + str (load_transfer) + " N")
                self.vel1 = self.vel2
                
            self.time2 = msg.header.stamp.secs
            if (self.time2 == self.time1):
                self.list_of_vel.append (msg.twist.twist.linear.x)
                #print ("appendao")
            else:
                self.first_pass = True
    def acceleration (self):
        rospy.spin();
    
    


if __name__ == "__main__":    
    try:
        x = AngleCalculator()
        x.acceleration()
    except rospy.ROSInterruptException:
        pass
    