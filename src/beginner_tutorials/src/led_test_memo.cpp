#include "ros/ros.h" /*rosを使うときに必要*/
#include "std_msgs/String.h" /*文字列をやり取りするときに必要*/
#include <sstream> /*文字列から数値を抜き出すのに必要*/
#include "mbed.h" /*mbedを利用するために必要*/
#include <std_msgs/Int32.h> /*整数をやり取りするのに必要*/
#include <std_msgs/Float32.h> /*小数をやり取りするのに必要*/

void chatterCallback(const std_msgs::String::ConstPtr &str_msg); /*<下にvoidを書くときは上に定義が必要、voidの前に「Inline」を付けると処理が軽くなる>*/
void chatterCallback(const std_msgs::String::ConstPtr &int_msg);

int main(int argc, char **argv){
    ros::init(argc, argv, "tester"); //ノード名の変更(したほうがいいのか分からなかったため、一応)<プログラムにつき一つのみ、ノード名がかぶらないように>
    ros::NodeHandle n;

    ros::Publisher  reference_pub = n.advertise <std_msgs::Float32>("reference", 1000); //LEDの点灯時間の送信、float32型へ変更 <publish、subscribeするものにつき1つずつ>
    ros::Subscriber sub_led = n.subscribe("counter", 1000, chatterCallback); //インスタンス名を「sub_led」&トピック名を「counter」へ変更、LEDの点灯時間の受け取り?
    ros::Subscriber sub_test = n.subscribe("chatter", 1000, chatterCallback); //インスタンス名を「sub_test」&トピック名を「chatter」へ変更、「test」の受け取り?

    //ros::spin(); ←{subscriber}のプログラム、今回は「ros::spinonce()」があるので必要ない
    ros::Rate loop_rate(10); /*制御周期が10Hz <whileの動作周期、今回は一つでよい>*/

    float count.data = 0.1f; //LEDの点灯時間、とりあえず0.1秒にしてみた & floatへ変更 <「.data」をつけると後で変数の中身を変えられる>

    while (ros::ok()) {
        std_msgs::Float32  msg; //Float32型へ変更 <mainの中で書くとmainの中でのみ有効、嫌ならmainの外で>

        std::stringstream ss; /*stringstream型でssを定義*/
        ss << count.data; //LEDの点灯時間に変更

        msg.data = ss.float(); //「str」を「float」に変更

        //ROS_INFO("%f", msg.data.c_str()); ←「"%s"」を「"%f"」へ変更、点灯時間の出力は必要か不明だったので

        reference_pub.publish(msg); //「reference_pub」へ変更、「msg」をpublishするもの

        ros::spinOnce();
        loop_rate.sleep(); /*先ほどの「loop_rate(10)」の実行*/

        //「++count;」の削除
     }
     return 0;
}

void chatterCallback(const std_msgs::String::ConstPtr &str_msg) //{subscriber}のプログラム(41-44行)、「str_msg」へ変更
{
  ROS_INFO("I heard message: [%s]", msg->data.c_str()); //「message」の追加
}

void chatterCallback(const std_msgs::String::ConstPtr &int_msg) //{subscriber}のプログラム(46-49行)、「int_msg」へ変更
{
  ROS_INFO("I heard led_time: [%f]", msg->data.c_str()); //[%f]へ変更、「led_time」の追加
}