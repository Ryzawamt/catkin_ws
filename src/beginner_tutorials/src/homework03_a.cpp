#include "ros/ros.h" 
#include "std_msgs/String.h"
#include <sstream>
#include <std_msgs/Float32.h>
#include "std_msgs/MultiArrayLayout.h"
#include "std_msgs/MultiArrayDimension.h"
#include "std_msgs/Int32MultiArray.h"

#define period 0.02f

inline void topic_str(const std_msgs::String::ConstPtr &str_msg);



int main(int argc, char **argv){
    ros::init(argc, argv, "homework03_a");
    ros::NodeHandle n;

    ros::Publisher  pub_flo = n.advertise <std_msgs::Float32>("pushfloat", 1000);
    ros::Publisher  pub_int = n.advertise <std_msgs::Int32MultiArray>("pushint", 1000);
    ros::Subscriber sub_str = n.subscribe("pushstring", 1000, topic_str);

    ros::Rate loop_rate(1 / period);

    std_msgs::Float32 sp_flo;
    sp_flo.data = 4.1f;

    while (ros::ok()) {
        std_msgs::Int32MultiArray sp_arr;
        sp_arr.data.resize(2);
        sp_arr.data[0] = 29;
        sp_arr.data[1] = 76;


        //std::stringstream ss;
        //ss << sp_flo.data;

        //sp_flo.data = ss.float();

        pub_flo.publish(sp_flo);
        pub_int.publish(sp_arr);

        ros::spinOnce();
        loop_rate.sleep();

    }
}

inline void topic_str(const std_msgs::String::ConstPtr &str_msg)
{
  ROS_INFO("I heard string message: [%s]", str_msg->data.c_str());
}