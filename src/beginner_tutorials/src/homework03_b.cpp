#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <std_msgs/Float32.h>
#include "std_msgs/MultiArrayLayout.h"
#include "std_msgs/MultiArrayDimension.h"
#include "std_msgs/Int32MultiArray.h"
#include <iostream>

#define PERIOD 0.02f

inline void flo_sub(const std_msgs::Float32::ConstPtr &float_msg);
inline void int_sub(const std_msgs::Int32MultiArray::ConstPtr &int_msg);

int main(int argc, char **argv){
    ros::init(argc, argv, "homework03_b");
    ros::NodeHandle n;

    ros::Publisher  pub_str = n.advertise <std_msgs::String>("pushstring", 1000);
    ros::Subscriber sub_flo = n.subscribe("pushfloat", 1000, flo_sub);
    ros::Subscriber sub_int = n.subscribe("pushint", 1000, int_sub);

    ros::Rate loop_rate(1 / PERIOD);

    std_msgs::String  word;

    std::stringstream ss;
    ss << "good choice";

    word.data = ss.str();

    while (ros::ok()) {
        ros::spinOnce();

        //ROS_INFO("%s", word.c_str());
        pub_str.publish(word);
        loop_rate.sleep();
    }
}

inline void flo_sub(const std_msgs::Float32::ConstPtr &float_msg)
{
  ROS_INFO("I heard float number: [%f]", float_msg->data);
}

inline void int_sub(const std_msgs::Int32MultiArray::ConstPtr &int_msg)
{
  int num = int_msg->data.size();
  //ROS_INFO("I heard int array: [%i]", int_msg->data);
  for (int i = 0; i < num; i++)
  { 
    ROS_INFO("I heard int array: [%i]:%d", i, int_msg->data[i]);
  }
}