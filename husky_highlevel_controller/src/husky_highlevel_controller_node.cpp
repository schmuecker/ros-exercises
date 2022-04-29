#include <ros/ros.h>
#include "scan_subscriber/ScanSubscriber.hpp"

int main(int argc, char** argv)
{
  ros::init(argc, argv, "scan_subscriber");
  ros::NodeHandle nodeHandle("~");

  scan_subscriber::ScanSubscriber ScanSubscriber(nodeHandle);

  ros::spin();
  return 0;
}
