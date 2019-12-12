#!/usr/bin/env python

import rospy
#if you want to test call hrc04.main() or if you want to measure 
import hrc04 as hr_distance
import time

from std_msgs.msg import String

def publish_distance():
    pub = rospy.Publisher('publisher', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(str(hr_distance.distance()))
        rate.sleep()

if __name__ == '__main__':
    #hrc04.main()
    #while True:
    #    time.sleep(0.5)        
    #    print(hr_distance.distance())   
    publish_distance()
    
