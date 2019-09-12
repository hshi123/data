#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   hshi
#   E-mail  :   snapwings3190@163.com
#   Date    :   19/09/07 11:31:39
#   Desc    :   

import rospy
import numpy as np
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TwistStamped
from matrix_driver.msg import Obstacle


list_time = []
list_position = []
def callback(self):
    list_time.append(float(self.header.stamp.secs) + round(float(self.header.stamp.nsecs)/10**9, 4))
    #list_position.append(round(float(self.pose.pose.position))
    a = self.pose.pose.position.x
    print "a= %f" % a
    print self.pose.pose.position.y
    print self.pose.pose.position.z

def listener_odom():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/sensor/gnss/odom', Odometry, callback, queue_size=10)
    rospy.spin()

def listener_vel():
    rospy.init_node('listenr', anonymous=True)
    rospy.SubScriber('/sensor/gnss/vel', TwistStamped, ca)
if __name__ == '__main__':
    listener_odom()
    b = np.array(list_time)
    np.savetxt('test.csv', b, delimiter = ',')
