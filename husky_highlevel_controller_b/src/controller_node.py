#!/usr/bin/env python3
import rospy
from husky_highlevel_controller_b import util
from sensor_msgs.msg import LaserScan


def callback(data):
    filtered_msg = util.filter_scan(data)
    publisher.publish(filtered_msg)
    
if __name__ == '__main__':
    rospy.init_node('husky_highlevel_controller_b')

    # load parameter
    queue_size = rospy.get_param("/queue_size")
    topic_name = rospy.get_param("/topic_name")


    # Create publisher
    # Eport Env Variable so LaserScan is available
    # export HUSKY_LMS1XX_ENABLED=1
    publisher = rospy.Publisher("scan_filtered", LaserScan,queue_size=1)
    rospy.Subscriber(topic_name, LaserScan, callback=callback, queue_size=queue_size)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()