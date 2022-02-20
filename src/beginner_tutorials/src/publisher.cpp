#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

int main(int argc, char **argv){
    ros::init(argc, argv, "talker");
    ros::NodeHandle n;

    ros::Publisher  chatter_pub = n.advertise <std_msgs::String>("chatter", 1000);//「string」は送っている型

    ros::Rate loop_rate(10);

    int count = 0;

    while (ros::ok()) {
        std_msgs::String  msg;//変数msgを定義

        std::stringstream ss;//変数ssを定義
        ss << "hello world " << count;//ssにhello worldを代入

        msg.data = ss.str();//msgに代入する「.data」

        ROS_INFO("%s", msg.data.c_str());//「C_str」が読み込んだ回数

        chatter_pub.publish(msg);

        ros::spinOnce();
        loop_rate.sleep();

        ++count;
     }
     return 0;
}