#include "ros/ros.h"
#include <performance_tests/SuperAwesome.h>
#include <sstream>
#include <string>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "pub");

  std::string rate = "10";
  std::string nbTests = "50";
  
  if (argc > 3 || argc <= 0)
  {
    ROS_ERROR("FAIL");
    ROS_ERROR("usage: rosrun performance_tests pub [rate] [nbTests]");
    return 0;
  } 
  else if ( argc == 1) 
  {
    ROS_INFO("no rate nor nbTests defined, using default rate: [%s] hz and default nbTests: [%s]", rate.c_str(), nbTests.c_str());
  }
    else if ( argc == 2) 
  {
    ROS_INFO("no nbTests defined, using default nbTests: [%s]", nbTests.c_str(), nbTests.c_str());
    rate = argv[1];
  }
  else
  {
      rate = argv[1];
      nbTests = argv[2];
  }
  

  int iRate = atoi(rate.c_str());
  int iNbTests = atoi(nbTests.c_str());


  ros::NodeHandle n;

  ros::Publisher p = n.advertise<performance_tests::SuperAwesome>("SuperTopic", 1000);

  ros::Rate loop_rate(iRate);

  int count = 0;
  while (ros::ok() && count < iNbTests)
  {
    performance_tests::SuperAwesome msg;

    std::stringstream ss;
    ss << "nb " << count;
    msg.s = ss.str();

    //ROS_INFO("%s", msg.s.c_str());
    p.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }
  //sleep(1);
  
  performance_tests::SuperAwesome endMsg;
  endMsg.s = "FIN|Cpp|"+rate;

  //ROS_INFO("%s", endMsg.s.c_str());
  p.publish(endMsg);

  ros::spinOnce();
  loop_rate.sleep();


  return 0;
}
