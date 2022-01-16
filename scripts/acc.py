#! /usr/bin/env python3

import rosbag
import sys
import statistics

#should add class

#def countAcc (msg):
    
    

if __name__ == "__main__":    
    first_pass = True
    first_first = True
    acc = 0.0
    vel = 0
    vel1 = 0
    vel2 = 0
    time1 = 0
    time2 = 0
    cnt = 0
    list_of_vel = []
    inbag_filename = sys.argv[1]

    for topic, msg, t in rosbag.Bag(inbag_filename, 'r').read_messages(topics="/odom"):
        if (first_first): #while reading the very first info from the bag
            if first_pass:
                if (cnt == 1):
                    vel1 = statistics.median(list_of_vel) #teaking median from the velocity of first second
                    list_of_vel.clear()
                elif (cnt == 2):
                    vel2 = statistics.median(list_of_vel) #teaking median from the velocity of second second
                    list_of_vel.clear()
                    acc = vel2 - vel1    #calulating acceleration
                    vel1 = vel2;
                    print (acc)
                    cnt == 0;
                    first_first = False
                    first_pass = True
                time1 = msg.header.stamp.secs;
                print (time1)
                list_of_vel.append (msg.twist.twist.linear.x)
                first_pass = False
                cnt += 1
            time2 = msg.header.stamp.secs
            if (time2 == time1):    #looking for the first change in seconds
                list_of_vel.append (msg.twist.twist.linear.x)
                #print ("appendao")
            else:
                first_pass = True
        
        else:      #when it comes to third second of operation, vel1 becames velocity from vel2 and velocity from third second will be vel2 and so on
            if (first_pass): 
                vel2 = statistics.median(list_of_vel)
                list_of_vel.clear()

                time1 = msg.header.stamp.secs;
                print (time1)
                list_of_vel.append (msg.twist.twist.linear.x)
                first_pass = False

                acc = vel2 - vel1
                print (acc)
                vel1 = vel2
                
            time2 = msg.header.stamp.secs
            if (time2 == time1):
                list_of_vel.append (msg.twist.twist.linear.x)
                #print ("appendao")
            else:
                first_pass = True

