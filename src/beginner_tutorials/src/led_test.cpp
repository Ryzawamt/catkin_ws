#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include "mbed.h"
#include <std_msgs/Int32.h>
#include <std_msgs/Float32.h>

void chatterCallback(const std_msgs::String::ConstPtr &str_msg);
void chatterCallback(const std_msgs::String::ConstPtr &int_msg);

int main(int argc, char **argv){
    ros::init(argc, argv, "tester");
    ros::NodeHandle n;

    ros::Publisher  reference_pub = n.advertise <std_msgs::Float32>("reference", 1000);
    ros::Subscriber sub_led = n.subscribe("counter", 1000, chatterCallback);
    ros::Subscriber sub_test = n.subscribe("chatter", 1000, chatterCallback);

    ros::Rate loop_rate(10);

    float count.data = 0.1f;

    while (ros::ok()) {
        std_msgs::Float32  msg;

        std::stringstream ss;
        ss << count.data;

        msg.data = ss.float();

        reference_pub.publish(msg);

        ros::spinOnce();
        loop_rate.sleep();

     }
     return 0;
}

void chatterCallback(const std_msgs::String::ConstPtr &str_msg)
{
  ROS_INFO("I heard message: [%s]", msg->data.c_str());
}

void chatterCallback(const std_msgs::String::ConstPtr &int_msg)
{
  ROS_INFO("I heard led_time: [%f]", msg->data.c_str());
}