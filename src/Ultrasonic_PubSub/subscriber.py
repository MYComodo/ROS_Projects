#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def distanceListen(data):
    rospy.loginfo(rospy.get_caller_id()+ "Distance: %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rpspy.Subscriber("chatter", String, distanceListen)
    rospy.spin()

if __name__ = '__main__':
    listener()
