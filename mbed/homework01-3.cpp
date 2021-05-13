#include "mbed.h"
#define CONTROL_CYCLE 0.02f

//LEDが0％、20％、50％、100％と変わっていくプログラム
DigitalIn SW(A1);
PwmOut output_pwm(A3);
Timer control_ticker;

int main(){
  control_ticker.start();
  output_pwm.write(0);
  float ledout;
  ledout = 0;
  while(1){
    if(control_ticker.read() >= CONTROL_CYCLE){
      control_ticker.reset();
    if(ledout==0){
        if(SW==0){
            output_pwm.write(0.2);
            ledout = 1;
            wait(0.2);
            while(SW==0){}
        }
    }
    else if(ledout==1){
        if(SW==0){
            output_pwm.write(0.5);
            ledout = 2;
            wait(0.2);
            while(SW==0){}
        }
    }
    else if(ledout==2){
        if(SW==0){
            output_pwm.write(1.0);
            ledout = 3;
            wait(0.2);
            while(SW==0){}
        }
    }
    else{
        if(SW==0){
            output_pwm.write(0);
            ledout = 0;
            wait(0.2);
            while(SW==0){}
        } 
    }
    }
  }
}