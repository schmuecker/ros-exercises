#!/usr/bin/env python3
import rospy
from husky_highlevel_controller import util
from sensor_msgs.msg import LaserScan


def callback(data):
    new_msg = util.filter_scan(data)
    publisher.publish(new_msg)
    

if __name__ == '__main__':
    rospy.init_node('husky_highlevel_controller')
    queue_size = rospy.get_param("queue_size")
    topic_name = rospy.get_param("topic_name")

    # Create publisher
    publisher = rospy.Publisher("~topic",LaserScan,queue_size=1)
    rospy.Subscriber(topic_name, LaserScan, callback=callback, queue_size=queue_size)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()