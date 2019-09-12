#!/usr/bin/env python

import sys, os, time
import json
import redis
from collections import OrderedDict

import rospy, rostopic, rosmsg

# https://github.com/baalexander/rospy_message_converter
from rospy_message_converter import json_message_converter

from std_msgs.msg import String
from std_msgs.msg import Bool
from std_msgs.msg import Empty
from std_msgs.msg import Float32

from can_msgs.msg import Frame

from dynamic_reconfigure.msg import Config
from dynamic_reconfigure.msg import ConfigDescription

from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry
from nav_msgs.msg import Path

# http://docs.ros.org/kinetic/api/sensor_msgs/html/msg/NavSatFix.html
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu
from sensor_msgs.msg import JointState
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import TimeReference

from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import TwistStamped

from tf2_msgs.msg import TFMessage

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

import anm_msgs.msg as anm_msgs
import dbw_mkz_msgs.msg as dbw_mkz_msgs
# # import rea_perception_msgs.msg as rea_perception_msgs
import etrans_msgs.msg as etrans_msgs

# from dbw_mkz_msgs.msg import BrakeReport

hostname = 'localhost'
port = 6379
password = ''

# Make connection to redis database
con = redis.StrictRedis(
    host=hostname,
    port=port,
    db=0)

current_milli_time = lambda: int(round(time.time() * 1000))

def rosmsg_info():
    topics_and_types = rospy.get_published_topics()
    for topic, ttype in topics_and_types:
        print("topic: %40s \t type: %55s"%(topic, ttype))

def rosmag_redis_json(data,topic):
    # print(topic)
    json_str = json_message_converter.convert_ros_message_to_json(data)

    append_fields = ('"timestamp" : "%s", ')% (str(current_milli_time()).strip())
    json_str = json_str[:1]+append_fields+json_str[1:]
    json_str = '{"' + topic + '" : ' + json_str + ' }'
    json_str = json_str.replace('NaN', '"NaN"')
    # print(json_str)
  
    con.publish(topic, json_str)

    if topic.strip() == "_vehicle_brake_report":
        # var to check if the car is in autonomy mode
        autonomy_status =  '{"_autonomy_state" : {"timestamp" : "%s", "status" : "%s"} }' % (str(int(data.header.stamp.to_time()*1000)), str(data.enabled).lower())
        # print(autonomy_status)
        con.publish("_autonomy_state", autonomy_status)
def topicListener():
    rospy.init_node('rosmsg2redis_json', anonymous=False)
    rospy.Subscriber("vehicle/steering_report", dbw_mkz_msgs.SteeringReport, callback = rosmag_redis_json, callback_args =  "_vehicle_steering_report")
    rospy.Subscriber("vehicle/gear_report", dbw_mkz_msgs.GearReport, callback = rosmag_redis_json, callback_args =  "_vehicle_gear_report")
    rospy.Subscriber("vehicle_state", anm_msgs.VehicleState, callback = rosmag_redis_json, callback_args =  "_vehicle_state_report")
    rospy.Subscriber("control_commands", anm_msgs.ControlCommands, callback = rosmag_redis_json, callback_args =  "_control_commands")
    rospy.Subscriber("checked_commands", anm_msgs.ControlCommands, callback = rosmag_redis_json, callback_args =  "_checked_commands")
    rospy.Subscriber("navsat/fix", NavSatFix, callback = rosmag_redis_json, callback_args =  "_navsat_fix")
    rospy.Subscriber("vehicle/throttle_report", dbw_mkz_msgs.ThrottleReport, callback = rosmag_redis_json, callback_args =  "_vehicle_throttle_report")
    rospy.Subscriber("vehicle/brake_report", dbw_mkz_msgs.BrakeReport, callback = rosmag_redis_json, callback_args =  "_vehicle_brake_report")
    rospy.Subscriber("odom_datum", NavSatFix, callback = rosmag_redis_json, callback_args =  "_odom_datum")
    rospy.spin()

if __name__ == '__main__':
    try:
        topicListener()
    except rospy.ROSInterruptException:
        pass
