#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from husky_highlevel_controller import util
from sensor_msgs.msg import LaserScan


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

    min_distance = data.range_min
    print("Minimum Distance : %s", min_distance)

    min_index = data.ranges.index(min_distance)

    measurements_5 = data.ranges[min_index-2: min_index+2]
    print(measurements_5)

    new_msg = LaserScan()
    new_msg.angle_min = data.angle_min
    new_msg.angle_max = data.angle_max
    new_msg.angle_increment = data.angle_increment
    new_msg.ranges = measurements_5

    publisher.publish(new_msg)
    

if __name__ == '__main__':
    rospy.init_node('husky_highlevel_controller')
    queue_size = rospy.get_param("/husky_controller/queue_size")
    topic_name = rospy.get_param("/husky_controller/topic_name")

    # Create publisher
    publisher = rospy.Publisher("~topic",String,queue_size=1)
    rospy.Subscriber(topic_name, String, callback=callback, queue_size=queue_size)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()