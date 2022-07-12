import RPi.GPIO as GPIO                          #GPIOを利用するモジュールをインポート
import datetime                                  #日時データを扱うモジュールのインポート
import smbus                                     #モジュールsmbusのインポート
import pigpio
import time                                      #時間データを扱うモジュールのインポート
import random
from decimal import Decimal, ROUND_HALF_UP   #decimalより、DecimalとROUND_HALF_UPをインポート

GPIO.setmode(GPIO.BCM)                           #GPIOを番号指定とする
LE = 25                                          #LE端子をGPIO 25番に接続
BL = 24                                          #BL端子をGPIO 24番に接続
LT = 23                                          #LT端子をGPIO 23番に接続
dig1 = 22                                        #DIG.1をGPIO 22番に接続
dig2 = 27                                        #DIG.2をGPIO 27番に接続
dig3 = 17                                        #DIG.3をGPIO 17番に接続
dig4 = 4                                         #DIG.4をGPIO 4番に接続
D0 = 26                                          #D0端子をGPIO 26番に接続
D1 = 16                                          #D1端子をGPIO 16番に接続
D2 = 20                                          #D2端子をGPIO 20番に接続
D3 = 21                                          #D3端子をGPIO 21番に接続
DP = 10
LED_G = 8
LED_R = 7
BUZZER = 18
SW1 = 6                                           #タクトスイッチをGPIO 6番に接続
SW2 = 5
SW3 = 15
SW4 = 14
SW5 = 11
GPIO.setup(LE,GPIO.OUT,initial=GPIO.LOW)         #GPIO 25番を出力設定としてLEを制御
GPIO.setup(BL,GPIO.OUT,initial=GPIO.LOW)         #GPIO 24番を出力設定としてBLを制御
GPIO.setup(LT,GPIO.OUT,initial=GPIO.LOW)         #GPIO 23番を出力設定としてLTを制御
GPIO.setup(dig1,GPIO.OUT,initial=GPIO.LOW)       #GPIO 22番を出力設定としてdig1を制御
GPIO.setup(dig2,GPIO.OUT,initial=GPIO.HIGH)      #GPIO 27番を出力設定としてdig2を制御
GPIO.setup(dig3,GPIO.OUT,initial=GPIO.HIGH)      #GPIO 17番を出力設定としてdig3を制御
GPIO.setup(dig4,GPIO.OUT,initial=GPIO.HIGH)      #GPIO 4番を出力設定としてdig4を制御
GPIO.setup(DP,GPIO.OUT,initial=GPIO.LOW)         #GPIO 10番を出力設定としてD0を制御
GPIO.setup(D0,GPIO.OUT,initial=GPIO.LOW)         #GPIO 26番を出力設定としてD0を制御
GPIO.setup(D1,GPIO.OUT,initial=GPIO.LOW)         #GPIO 16番を出力設定としてD1を制御
GPIO.setup(D2,GPIO.OUT,initial=GPIO.LOW)         #GPIO 20番を出力設定としてD2を制御
GPIO.setup(D3,GPIO.OUT,initial=GPIO.LOW)         #GPIO 21番を出力設定としてD3を制御
GPIO.setup(LED_G,GPIO.OUT,initial=GPIO.LOW)      #GPIO 8番を出力設定として緑色LEDを制御
GPIO.setup(LED_R,GPIO.OUT,initial=GPIO.LOW)      #GPIO 7番を出力設定として赤色LEDを制御
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 6番をプルアップでの入力設定
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 5番をプルアップでの入力設定
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 15番をプルアップでの入力設定
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 14番をプルアップでの入力設定
GPIO.setup(SW5,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 11番をプルアップでの入力設定

pi = pigpio.pi()
pi.set_mode(BUZZER, pigpio.INPUT)

i2c = smbus.SMBus(1)           #インスタンスの作成
address = 0x48                 #スレーブアドレスの定義

s1 = 0                         #タクトスイッチによる信号の立ち下がりを検知した場合のみ1とする変数
s2 = 0
s3 = 0
s4 = 0
s5 = 0
def checkSW(pin):             #スイッチが押された時に利用する関数
    global s1                  #グローバル変数s1を定義する
    global s2                  #グローバル変数s2を定義する
    global s3                  #グローバル変数s3を定義する
    global s4                  #グローバル変数s4を定義する
    global s5                  #グローバル変数s5を定義する
    if pin == SW1:
        s1 = 1                     #変数s1の値を1とする
    elif pin == SW2:
        s2 = 1                     #変数s2の値を1とする
    elif pin == SW3:
        s3 = 1                     #変数s3の値を1とする
    elif pin == SW4:
        s4 = 1                     #変数s4の値を1とする
    elif pin == SW5:
        s5 = 1                     #変数s5の値を1とする

def display(num):                      #4桁7セグメントLEDへ数字を表示する関数
    if num == 0:                       #0を表示する場合
        GPIO.output(D0, GPIO.LOW)      #D0の信号をLOWとする
        GPIO.output(D1, GPIO.LOW)      #D1の信号をLOWとする
        GPIO.output(D2, GPIO.LOW)      #D2の信号をLOWとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 1:                     #1を表示する場合
        GPIO.output(D0, GPIO.HIGH)     #D0の信号をHIGHとする
        GPIO.output(D1, GPIO.LOW)      #D1の信号をLOWとする
        GPIO.output(D2, GPIO.LOW)      #D2の信号をLOWとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 2:                     #2を表示する場合
        GPIO.output(D0, GPIO.LOW)      #D0の信号をLOWとする
        GPIO.output(D1, GPIO.HIGH)     #D1の信号をHIGHとする
        GPIO.output(D2, GPIO.LOW)      #D2の信号をLOWとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 3:                     #3を表示する場合
        GPIO.output(D0, GPIO.HIGH)     #D0の信号をHIGHとする
        GPIO.output(D1, GPIO.HIGH)     #D1の信号をHIGHとする
        GPIO.output(D2, GPIO.LOW)      #D2の信号をLOWとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 4:                     #4を表示する場合
        GPIO.output(D0, GPIO.LOW)      #D0の信号をLOWとする
        GPIO.output(D1, GPIO.LOW)      #D1の信号をLOWとする
        GPIO.output(D2, GPIO.HIGH)     #D2の信号をHIGHとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 5:                     #5を表示する場合
        GPIO.output(D0, GPIO.HIGH)     #D0の信号をHIGHとする
        GPIO.output(D1, GPIO.LOW)      #D1の信号をLOWとする
        GPIO.output(D2, GPIO.HIGH)     #D2の信号をHIGHとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 6:                     #6を表示する場合
        GPIO.output(D0, GPIO.LOW)      #D0の信号をLOWとする
        GPIO.output(D1, GPIO.HIGH)     #D1の信号をHIGHとする
        GPIO.output(D2, GPIO.HIGH)     #D2の信号をHIGHとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 7:                     #7を表示する場合
        GPIO.output(D0, GPIO.HIGH)     #D0の信号をHIGHとする
        GPIO.output(D1, GPIO.HIGH)     #D1の信号をHIGHとする
        GPIO.output(D2, GPIO.HIGH)     #D2の信号をHIGHとする
        GPIO.output(D3, GPIO.LOW)      #D3の信号をLOWとする
    
    elif num == 8:                     #8を表示する場合
        GPIO.output(D0, GPIO.LOW)      #D0の信号をLOWとする
        GPIO.output(D1, GPIO.LOW)      #D1の信号をLOWとする
        GPIO.output(D2, GPIO.LOW)      #D2の信号をLOWとする
        GPIO.output(D3, GPIO.HIGH)     #D3の信号をHIGHとする
    
    elif num == 9:                     #9を表示する場合
        GPIO.output(D0, GPIO.HIGH)     #D0の信号をHIGHとする
        GPIO.output(D1, GPIO.LOW)      #D1の信号をLOWとする
        GPIO.output(D2, GPIO.LOW)      #D2の信号をLOWとする
        GPIO.output(D3, GPIO.HIGH)     #D3の信号をHIGHとする
    
    else:                              #表示しない場合
        GPIO.output(D0, GPIO.LOW)      #D0の信号をLOWとする
        GPIO.output(D1, GPIO.HIGH)     #D1の信号をHIGHとする
        GPIO.output(D2, GPIO.LOW)      #D2の信号をLOWとする
        GPIO.output(D3, GPIO.HIGH)     #D3の信号をHIGHとする

def digswitch(L_num, figs):            #7セグメントLEDを1桁ずつ制御する関数
    if L_num == 1:                     #左から1番目の7セグメントLEDを制御する場合
        GPIO.output(dig1, GPIO.LOW)    #dig1の信号をLOWとする
        GPIO.output(dig2, GPIO.HIGH)   #dig2の信号をHIGHとする
        GPIO.output(dig3, GPIO.HIGH)   #dig3の信号をHIGHとする
        GPIO.output(dig4, GPIO.HIGH)   #dig4の信号をHIGHとする
        display(figs)                  #その桁において数字を表示する
    
    elif L_num == 2:                   #左から2番目の7セグメントLEDを制御する場合
        GPIO.output(dig1, GPIO.HIGH)   #dig1の信号をHIGHとする
        GPIO.output(dig2, GPIO.LOW)    #dig2の信号をLOWとする
        GPIO.output(dig3, GPIO.HIGH)   #dig3の信号をHIGHとする
        GPIO.output(dig4, GPIO.HIGH)   #dig4の信号をHIGHとする
        display(figs)                  #その桁において数字を表示する
    
    elif L_num == 3:                   #左から3番目の7セグメントLEDを制御する場合
        GPIO.output(dig1, GPIO.HIGH)   #dig1の信号をHIGHとする
        GPIO.output(dig2, GPIO.HIGH)   #dig2の信号をHIGHとする
        GPIO.output(dig3, GPIO.LOW)    #dig3の信号をLOWとする
        GPIO.output(dig4, GPIO.HIGH)   #dig4の信号をHIGHとする
        display(figs)                  #その桁において数字を表示する
    
    elif L_num == 4:                   #左から4番目の7セグメントLEDを制御する場合
        GPIO.output(dig1, GPIO.HIGH)   #dig1の信号をHIGHとする
        GPIO.output(dig2, GPIO.HIGH)   #dig2の信号をHIGHとする
        GPIO.output(dig3, GPIO.HIGH)   #dig3の信号をHIGHとする
        GPIO.output(dig4, GPIO.LOW)    #dig4の信号をLOWとする
        display(figs)                  #その桁において数字を表示する

def modeprinter(mode_num):
    for p in range(222):
        digswitch(1, mode_num)    #左から1番目の7セグメントLEDへ、0番目の数字を表示する
        time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        digswitch(2, 10)    #左から2番目の7セグメントLEDへ、1番目の数字を表示する
        time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        digswitch(3, 10)    #左から3番目の7セグメントLEDへ、2番目の数字を表示する
        time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        digswitch(4, 10)    #左から4番目の7セグメントLEDへ、3番目の数字を表示する
        time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する

def read_adt7410():                               #温度センサモジュールの計測について定義する関数
    byte_data = i2c.read_byte_data(address,0x00)  #上位8bitについて変数へ代入
    data = byte_data<<8                           #左へ8bit分シフトする
    byte_data = i2c.read_byte_data(address,0x01)  #下位8bitについて変数へ代入
    data = data | byte_data                       #2つの変数に論理和を活用して変数へ代入
    data = data >> 3                              #右へ3bit分シフトする
    return data                                   #変数dataを返り値とする

GPIO.add_event_detect(SW1, GPIO.FALLING, callback=checkSW, bouncetime=200)    #イベント検出を定義
GPIO.add_event_detect(SW2, GPIO.FALLING, callback=checkSW, bouncetime=200)    #イベント検出を定義
GPIO.add_event_detect(SW3, GPIO.FALLING, callback=checkSW, bouncetime=200)    #イベント検出を定義
GPIO.add_event_detect(SW4, GPIO.FALLING, callback=checkSW, bouncetime=200)    #イベント検出を定義
GPIO.add_event_detect(SW5, GPIO.FALLING, callback=checkSW, bouncetime=200)    #イベント検出を定義

try:                                   #目的の処理を記述する
    GPIO.output(LE, GPIO.LOW)          #LEの信号をLOWとする
    GPIO.output(BL, GPIO.HIGH)         #BLの信号をHIGHとする
    GPIO.output(LT, GPIO.HIGH)         #LTの信号をHIGHとする
    mode = 0                           #7セグメントLEDへ表示する種類について格納する変数
    modeprint_time = True
    pushed = 0                         #タクトスイッチが押された回数を格納する変数
    alarm1 = 0
    alarm2 = 0
    alarm3 = 0
    alarm4 = 0
    setup = 0
    stoptime = 0
    timer1 = 0
    timer2 = 0
    set_tim = 0
    timetime = 0
    while True:                                      #以下の46行のプログラムを繰り返す
        nowtime = datetime.datetime.now()            #現在の日時を取得
        strtime = nowtime.strftime('%Y%m%d%H%M%S')   #日時を文字列へ変換
        if s5 == 1:                                   #タクトスイッチが押された際に以下の3行を実行
            pushed = pushed + 1                      #タクトスイッチを押した回数へ1を加算する
            mode = pushed % 10                        #8で割った余りを利用し、0から3の範囲を繰り返す
            modeprint_time = True
            s5 = 0                                    #変数s5の値を0にする
        
        if mode==0 or mode==1 or mode==2 or mode==3 or mode==8:
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
        
        if mode == 0:                        #表示する種類が「西暦」の場合、以下の8行の処理を行う
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            digswitch(1, int(strtime[0]))    #左から1番目の7セグメントLEDへ、0番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(strtime[1]))    #左から2番目の7セグメントLEDへ、1番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(strtime[2]))    #左から3番目の7セグメントLEDへ、2番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[3]))    #左から4番目の7セグメントLEDへ、3番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 1:                      #表示する種類が「月日」の場合、以下の8行の処理を行う
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            digswitch(1, int(strtime[4]))    #左から1番目の7セグメントLEDへ、4番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(strtime[5]))    #左から2番目の7セグメントLEDへ、5番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(strtime[6]))    #左から3番目の7セグメントLEDへ、6番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[7]))    #左から4番目の7セグメントLEDへ、7番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 2:                      #表示する種類が「時間」の場合、以下の8行の処理を行う
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            digswitch(1, int(strtime[8]))    #左から1番目の7セグメントLEDへ、8番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(strtime[9]))    #左から2番目の7セグメントLEDへ、9番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(strtime[10]))   #左から3番目の7セグメントLEDへ、10番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[11]))   #左から4番目の7セグメントLEDへ、11番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 3:                      #表示する種類が「秒」の場合、以下の8行の処理を行う
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            digswitch(1, 10)                 #左から1番目の7セグメントLEDには何も表示しない
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, 10)                 #左から2番目の7セグメントLEDには何も表示しない
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(strtime[12]))   #左から3番目の7セグメントLEDへ、12番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[13]))   #左から4番目の7セグメントLEDへ、13番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 4:
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            if s2 == 1:
                setup += 1
                setup = setup % 4
                s2 = 0
            elif s4 == 1:
                setup -= 1
                setup = setup % 4
                s4 = 0
            if setup == 0:
                if s1 == 1:
                    if alarm1 == 2:
                        alarm1 = 0
                    else:
                        alarm1 += 1
                    s1 = 0
                elif s3 == 1:
                    if alarm1 == 0:
                        alarm1 = 2
                    else:
                        alarm1 -= 1
                    s3 = 0
            elif setup == 1:
                if s1 == 1:
                    if alarm2 == 9:
                        alarm2 = 0
                    else:
                        alarm2 += 1
                    s1 = 0
                elif s3 == 1:
                    if alarm2 == 0:
                        alarm2 = 9
                    else:
                        alarm2 -= 1
                    s3 = 0
            elif setup == 2:
                if s1 == 1:
                    if alarm3 == 5:
                        alarm3 = 0
                    else:
                        alarm3 += 1
                    s1 = 0
                elif s3 == 1:
                    if alarm3 == 0:
                        alarm3 = 5
                    else:
                        alarm3 -= 1
                    s3 = 0
            elif setup == 3:
                if s1 == 1:
                    if alarm4 == 9:
                        alarm4 = 0
                    else:
                        alarm4 += 1
                    s1 = 0
                elif s3 == 1:
                    if alarm4 == 0:
                        alarm4 = 9
                    else:
                        alarm4 -= 1
                    s3 = 0
            alarm_time = str(alarm1) + str(alarm2) + str(alarm3) + str(alarm4)
            if strtime[8:12] != alarm_time:
                alarm_signal = True
            if strtime[8:12] == alarm_time and alarm_signal == True:
                print('時間です')                                                #要変更
                digswitch(4, 10)
                while(s1 != 1 and s2 != 1 and s3 != 1 and s4 != 1):
                    GPIO.output(LED_G, GPIO.HIGH)
                    pi.set_mode(BUZZER, pigpio.OUTPUT)
                    pi.hardware_PWM(BUZZER, 2100, 500000)
                    time.sleep(0.25)
                    GPIO.output(LED_G, GPIO.LOW)
                    GPIO.output(LED_R, GPIO.HIGH)
                    pi.set_mode(BUZZER, pigpio.INPUT)
                    time.sleep(0.25)
                    GPIO.output(LED_R, GPIO.LOW)
                GPIO.output(LED_G,GPIO.LOW)
                GPIO.output(LED_R, GPIO.LOW)
                pi.set_mode(BUZZER, pigpio.INPUT)
                alarm_signal = False
                s1 = 0
                s2 = 0
                s3 = 0
                s4 = 0
            digswitch(1, int(alarm1))    #左から1番目の7セグメントLEDへ、alarm1の数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(alarm2))    #左から2番目の7セグメントLEDへ、alarm2の数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(alarm3))   #左から3番目の7セグメントLEDへ、alarm3の数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(alarm4))   #左から4番目の7セグメントLEDへ、alarm4の数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 5:
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            if s1 == 1 or s2 == 1:
                s1 = 0
                s2 = 0
                stopsignal = False
                while (s1 != 1 or s2 != 1):
                    stop_h = stoptime // 60
                    stop_m = stoptime % 60
                    if stop_h <= 9 and stop_m <= 9:
                        stopview =str(0) + str(stop_h) + str(0) + str(stop_m)
                    elif stop_h <= 9 and stop_m > 9:
                        stopview = str(0) + str(stop_h) + str(stop_m)
                    elif stop_h > 9 and stop_m <= 9:
                        stopview = str(stop_h) + str(0) + str(stop_m)
                    else:
                        stopview = str(stop_h) + str(stop_m)
                    for p in range(222):
                        digswitch(1, int(stopview[0]))    #左から1番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(2, int(stopview[1]))    #左から2番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(3, int(stopview[2]))   #左から3番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(4, int(stopview[3]))   #左から4番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        if s1 == 1 or s2 == 1:
                            stopsignal = True
                            break
                    if s3 == 1 or s4 == 1:
                        laptime0 = int(stopview[0])
                        laptime1 = int(stopview[1])
                        laptime2 = int(stopview[2])
                        laptime3 = int(stopview[3])
                        GPIO.output(LED_G, GPIO.HIGH)
                        GPIO.output(LED_R, GPIO.HIGH)
                        s3 = 0
                        s4 = 0
                        while(s3 != 1 and s4 != 1):
                            stoptime += 1
                            for p in range(222):
                                digswitch(1, laptime0)    #左から1番目の7セグメントLEDへ、数字を表示する
                                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                                digswitch(2, laptime1)    #左から2番目の7セグメントLEDへ、数字を表示する
                                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                                digswitch(3, laptime2)   #左から3番目の7セグメントLEDへ、数字を表示する
                                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                                digswitch(4, laptime3)   #左から4番目の7セグメントLEDへ、数字を表示する
                                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        GPIO.output(LED_G, GPIO.LOW)
                        GPIO.output(LED_R, GPIO.LOW)
                        s3 = 0
                        s4 = 0
                    if stopsignal == True:
                        stopsignal = False
                        break
                    stoptime += 1
                s1 = 0
                s2 = 0
                s3 = 0
                s4 = 0
                
            stop_h = stoptime // 60
            stop_m = stoptime % 60
            if stop_h <= 9 and stop_m <= 9:
                stopview =str(0) + str(stop_h) + str(0) + str(stop_m)
            elif stop_h <= 9 and stop_m > 9:
                stopview = str(0) + str(stop_h) + str(stop_m)
            elif stop_h > 9 and stop_m <= 9:
                stopview = str(stop_h) + str(0) + str(stop_m)
            else:
                stopview = str(stop_h) + str(stop_m)
            digswitch(1, int(stopview[0]))    #左から1番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(stopview[1]))    #左から2番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(stopview[2]))   #左から3番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(stopview[3]))   #左から4番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            
            if s3 == 1 or s4 == 1:
                stoptime = 0
                s3 = 0
                s4 = 0
        
        elif mode == 6:
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            if s2 == 1:
                set_tim += 1
                set_tim = set_tim % 2
                s2 = 0
            if set_tim == 0:
                if s1 == 1:
                    if timer1 == 99:
                        timer1 = 0
                        timetime -= 5940
                    else:
                        timer1 += 1
                        timetime += 60
                    s1 = 0
                elif s3 == 1:
                    if timer1 == 0:
                        timer1 = 99
                        timetime += 5940
                    else:
                        timer1 -= 1
                        timetime -= 60
                    s3 = 0
            elif set_tim == 1:
                if s1 == 1:
                    if timer2 == 59:
                        timer2 = 0
                        timetime -= 59
                    else:
                        timer2 += 1
                        timetime += 1
                    s1 = 0
                elif s3 == 1:
                    if timer2 == 0:
                        timer2 = 59
                        timetime += 59
                    else:
                        timer2 -= 1
                        timetime -= 1
                    s3 = 0
            if s4 == 1:
                stopsignal = False
                time_lb = False
                timing_ctl = 222
                s4 = 0
                while (s4 != 1):
                    timer1 = timetime // 60
                    timer2 = timetime % 60
                    if timer1 <= 9 and timer2 <= 9:
                        timeview =str(0) + str(timer1) + str(0) + str(timer2)
                    elif timer1 <= 9 and timer2 > 9:
                        timeview = str(0) + str(timer1) + str(timer2)
                    elif timer1 > 9 and timer2 <= 9:
                        timeview = str(timer1) + str(0) + str(timer2)
                    else:
                        timeview = str(timer1) + str(timer2)
                    for p in range(timing_ctl):
                        digswitch(1, int(timeview[0]))    #左から1番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(2, int(timeview[1]))    #左から2番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(3, int(timeview[2]))   #左から3番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(4, int(timeview[3]))   #左から4番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        if s4 == 1:
                            stopsignal = True
                            break
                    if stopsignal == True:
                        stopsignal = False
                        break
                    if timetime == 0:
                        timing_ctl = 111
                        if time_lb == False:
                            GPIO.output(LED_G, GPIO.LOW)
                            GPIO.output(LED_R, GPIO.HIGH)
                            pi.set_mode(BUZZER, pigpio.OUTPUT)
                            pi.hardware_PWM(BUZZER, 1050, 500000)
                            print('time!!!!!!!!!!!')
                            time_lb = True
                        else:
                            GPIO.output(LED_R, GPIO.LOW)
                            GPIO.output(LED_G, GPIO.HIGH)
                            pi.set_mode(BUZZER, pigpio.INPUT)
                            time_lb = False
                    else:
                        timetime -= 1
                GPIO.output(LED_G,GPIO.LOW)
                GPIO.output(LED_R, GPIO.LOW)
                pi.set_mode(BUZZER, pigpio.INPUT)
                s1 = 0
                s2 = 0
                s3 = 0
                s4 = 0
            
            timer1 = timetime // 60
            timer2 = timetime % 60
            if timer1 <= 9 and timer2 <= 9:
                timeview =str(0) + str(timer1) + str(0) + str(timer2)
            elif timer1 <= 9 and timer2 > 9:
                timeview = str(0) + str(timer1) + str(timer2)
            elif timer1 > 9 and timer2 <= 9:
                timeview = str(timer1) + str(0) + str(timer2)
            else:
                timeview = str(timer1) + str(timer2)
            digswitch(1, int(timeview[0]))    #左から1番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(timeview[1]))    #左から2番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(timeview[2]))   #左から3番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(timeview[3]))   #左から4番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 7:
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            coll = False
            memory = [-1,-1,-1]
            answer = [-1,-1,-1, 0]
            if s4 == 1:
                score = 0
                coll = True
                s4 = 0
            while (coll == True):
                ans_num = 3
                memory.append(random.randint(0,9))
                for i in range (len(memory)-3):
                    for p in range(222):
                        digswitch(1, int(memory[i]))    #左から1番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(2, int(memory[i+1]))    #左から2番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(3, int(memory[i+2]))   #左から3番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(4, int(memory[i+3]))   #左から4番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                
                while (s4 != 1):
                    digswitch(1, int(answer[ans_num-3]))    #左から1番目の7セグメントLEDへ、数字を表示する
                    time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                    digswitch(2, int(answer[ans_num-2]))    #左から2番目の7セグメントLEDへ、数字を表示する
                    time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                    digswitch(3, int(answer[ans_num-1]))   #左から3番目の7セグメントLEDへ、数字を表示する
                    time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                    digswitch(4, int(answer[ans_num]))   #左から4番目の7セグメントLEDへ、数字を表示する
                    time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                    if s2 == 1:
                        answer.append(0)
                        ans_num += 1
                        s2 = 0
                    if s1 == 1:
                        if answer[ans_num] != 9:
                            answer[ans_num] += 1
                        else:
                            answer[ans_num] = 0
                        s1 = 0
                    elif s3 == 1:
                        if answer[ans_num] != 0:
                            answer[ans_num] -= 1
                        else:
                            answer[ans_num] = 9
                        s3 = 0
                s4 = 0
                    
                if memory == answer:
                    digswitch(4, 10)
                    score += 1
                    coll = True
                    print('success!')                    #testprint
                    GPIO.output(LED_G, GPIO.HIGH)
                    pi.set_mode(BUZZER, pigpio.OUTPUT)
                    pi.hardware_PWM(BUZZER, 1319, 500000)
                    time.sleep(0.25)
                    pi.hardware_PWM(BUZZER, 1047, 500000)
                    time.sleep(0.75)
                    GPIO.output(LED_G, GPIO.LOW)
                    pi.set_mode(BUZZER, pigpio.INPUT)
                    answer = [-1,-1,-1, 0]
                else:
                    digswitch(4, 10)
                    coll = False
                    print('failed.')
                    GPIO.output(LED_R, GPIO.HIGH)
                    pi.set_mode(BUZZER, pigpio.OUTPUT)
                    pi.hardware_PWM(BUZZER, 392, 500000)
                    time.sleep(1.0)
                    pi.set_mode(BUZZER, pigpio.INPUT)
                    if score <= 9:
                        scoreview =str(0) + str(0) + str(0) + str(score)
                    elif 10 <= score and score <= 99:
                        scoreview = str(0) + str(0) + str(score)
                    elif 100 <= score and timer2 <= 9999:
                        scoreview =str(0) + str(score)
                    else:
                        scoreview = str(score)
                    while (s1 != 1 and s2 != 1 and s3 != 1 and s4 != 1):
                        digswitch(1, int(scoreview[-4]))   #左から1番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)                  #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(2, int(scoreview[-3]))   #左から2番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)                  #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(3, int(scoreview[-2]))   #左から3番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)                  #7セグメントLEDを切り替えるため、0.001秒待機する
                        digswitch(4, int(scoreview[-1]))   #左から4番目の7セグメントLEDへ、数字を表示する
                        time.sleep(0.001)                  #7セグメントLEDを切り替えるため、0.001秒待機する
                    GPIO.output(LED_R, GPIO.LOW)
                    s1 = 0
                    s2 = 0
                    s3 = 0
                    s4 = 0
            digswitch(1, 10)        #左から1番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, 0)         #左から2番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, 0)         #左から3番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, 10)        #左から4番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            s1 = 0
            s2 = 0
            s3 = 0
        
        elif mode == 8:
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            module = read_adt7410()                        #温度センサモジュールによる計測を実行
            if (module > 4096):                            #温度が負の場合
                module = module - 8192                     #温度センサモジュールの整数値から8192を引く
            module = module*0.0625                         #温度センサモジュールの整数値へ0.0625をかける
            temp = str(Decimal(str(module)).quantize(Decimal('0.01'))*100)
            for p in range(222):
                digswitch(1, int(temp[0]))   #左から1番目の7セグメントLEDへ、数字を表示する
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                digswitch(2, int(temp[1]))   #左から2番目の7セグメントLEDへ、数字を表示する
                GPIO.output(DP, GPIO.HIGH)
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                GPIO.output(DP, GPIO.LOW)
                digswitch(3, int(temp[2]))   #左から3番目の7セグメントLEDへ、数字を表示する
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
                digswitch(4, int(temp[3]))   #左から4番目の7セグメントLEDへ、数字を表示する
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 9:
            if modeprint_time == True:
                modeprinter(mode)
                modeprint_time = False
            digswitch(1, 4)        #左から1番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, 3)         #左から2番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, 2)         #左から3番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, 1)        #左から4番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機する
            if s1 == 1:
                digswitch(4, 1)
                pi.set_mode(BUZZER, pigpio.OUTPUT)
                pi.hardware_PWM(BUZZER, 523, 500000)
                time.sleep(1.0)
                pi.hardware_PWM(BUZZER, 659, 500000)
                time.sleep(1.0)
                pi.hardware_PWM(BUZZER, 587, 500000)
                time.sleep(1.0)
                pi.hardware_PWM(BUZZER, 392, 500000)
                time.sleep(3.0)
            elif s2 == 1:
                digswitch(4, 2)
                pi.set_mode(BUZZER, pigpio.OUTPUT)
                GPIO.output(LED_G, GPIO.HIGH)
                pi.hardware_PWM(BUZZER, 523, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 587, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 659, 500000)
                time.sleep(0.5)
                pi.hardware_PWM(BUZZER, 587, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 523, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 0, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 523, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 587, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 659, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 587, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 523, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 587, 500000)
                time.sleep(1.0)
            elif s3 == 1:
                digswitch(4, 3)
                GPIO.output(LED_R, GPIO.HIGH)
                pi.set_mode(BUZZER, pigpio.OUTPUT)
                pi.hardware_PWM(BUZZER, 784, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 0, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 784, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 880, 500000)
                time.sleep(2.0)
            elif s4 == 1:
                digswitch(4, 4)
                GPIO.output(LED_G, GPIO.HIGH)
                GPIO.output(LED_R, GPIO.HIGH)
                pi.set_mode(BUZZER, pigpio.OUTPUT)
                pi.hardware_PWM(BUZZER, 988, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 1397, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 0, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 1397, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 0, 500000)
                time.sleep(0.05)
                pi.hardware_PWM(BUZZER, 1397, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 1319, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 1175, 500000)
                time.sleep(0.2)
                pi.hardware_PWM(BUZZER, 1047, 500000)
                time.sleep(1.0)
            GPIO.output(LED_G, GPIO.LOW)
            GPIO.output(LED_R, GPIO.LOW)
            pi.set_mode(BUZZER, pigpio.INPUT)
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0

except KeyboardInterrupt:             #プログラムの停止指示を検知
    pass                              #何もせずに終了する

pi.stop()
GPIO.cleanup()                        #GPIOの設定を初期化