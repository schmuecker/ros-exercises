#include "scan_subscriber/ScanSubscriber.hpp"

// STD
#include <string>

namespace scan_subscriber {

ScanSubscriber::ScanSubscriber(ros::NodeHandle& nodeHandle)
    : nodeHandle_(nodeHandle)
{
  if (!readParameters()) {
    ROS_ERROR("Could not read parameters.");
    ros::requestShutdown();
  }
  subscriber_ = nodeHandle_.subscribe(subscriberTopic_, queueSize_,
                                      &ScanSubscriber::topicCallback, this);
  ROS_INFO("Successfully launched node.");
}

ScanSubscriber::~ScanSubscriber()
{
}

bool ScanSubscriber::readParameters()
{
  if (!nodeHandle_.getParam("/subscriber_topic", subscriberTopic_)) return false;
  if (!nodeHandle_.getParam("/queue_size", queueSize_)) return false;
  return true;

}

void ScanSubscriber::topicCallback(const sensor_msgs::Temperature& message)
{
  
}


} /* namespace */
