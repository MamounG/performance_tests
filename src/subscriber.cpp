#include "ros/ros.h"
#include <performance_tests/SuperAwesome.h>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

double time1, sum = 0;
int nb = 0;
bool firstUsage = true;


template<typename Out>
void split(const std::string &s, char delim, Out result) {
    std::stringstream ss;
    ss.str(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        *(result++) = item;
    }
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, std::back_inserter(elems));
    return elems;
}


void writeToFile(double sumToWrite, std::string rate, std::string serverType)
{
  std::string fileName = serverType+"ToCpp";
  //ROS_INFO_STREAM("fileName = " << fileName);
    
  ofstream myfile;
  myfile.open (fileName.c_str(), ios::app);
    
  std::ostringstream sstream;
  sstream << rate << "|" << sumToWrite;
  std::string varAsString = sstream.str();
  myfile << varAsString+"\n";
  myfile.close();
}

void pCallback(const performance_tests::SuperAwesome::ConstPtr& msg)
{
  double time2 = ros::Time::now().toSec();
  
  if (msg->s.find("FIN") != std::string::npos)
  {
    //ROS_INFO_STREAM("ending process");
    std::vector<std::string> serverInfo = split(msg->s.c_str(),'|');
    writeToFile((sum/nb),serverInfo[2],serverInfo[1]);
    return;
  }
  

  //ROS_INFO("I heard: [%s]", msg->s.c_str());
  if (firstUsage)
    firstUsage = false;
  else
  {
    sum += time2 - time1;
    nb++;
    //ROS_INFO_STREAM("curent time average = " << (sum/nb) << " s" );
  }
  time1 = ros::Time::now().toSec();
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "subs");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("SuperTopic", 1000, pCallback);
  ros::spin();

  return 0;
}
