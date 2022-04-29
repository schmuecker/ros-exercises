#pragma once

// ROS
#include <ros/ros.h>
#include <sensor_msgs/Temperature.h>
#include <std_srvs/Trigger.h>

namespace scan_subscriber {

/*!
 * Main class for the node to handle the ROS interfacing.
 */
class ScanSubscriber
{
 public:
  /*!
   * Constructor.
   * @param nodeHandle the ROS node handle.
   */
  ScanSubscriber(ros::NodeHandle& nodeHandle);

  /*!
   * Destructor.
   */
  virtual ~ScanSubscriber();

 private:
  /*!
   * Reads and verifies the ROS parameters.
   * @return true if successful.
   */
  bool readParameters();

  /*!
   * ROS topic callback method.
   * @param message the received message.
   */
  void topicCallback(const sensor_msgs::Temperature& message);


  //! ROS node handle.
  ros::NodeHandle& nodeHandle_;

  //! ROS topic subscriber.
  ros::Subscriber subscriber_;

  //! ROS topic name to subscribe to.
  std::string subscriberTopic_;

  //! ROS queue size for subscriber.
  std::int32_t queueSize_;

};

} /* namespace */
