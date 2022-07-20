import RPi.GPIO as GPIO                           #GPIOを利用するモジュールをインポート
import datetime                                   #日時データを扱うモジュールのインポート
import smbus                                      #モジュールsmbusのインポート
import pigpio                                     #モジュールpigpioをインポート
import time                                       #時間データを扱うモジュールのインポート
import random                                     #乱数を扱うモジュールrandomをインポート
from decimal import Decimal, ROUND_HALF_UP        #decimalよりDecimalとROUND_HALF_UPをインポート

GPIO.setmode(GPIO.BCM)                            #GPIOを番号指定とする
LE = 25                                           #LE端子をGPIO 25番に接続
BL = 24                                           #BL端子をGPIO 24番に接続
LT = 23                                           #LT端子をGPIO 23番に接続
dig1 = 22                                         #DIG.1をGPIO 22番に接続
dig2 = 27                                         #DIG.2をGPIO 27番に接続
dig3 = 17                                         #DIG.3をGPIO 17番に接続
dig4 = 4                                          #DIG.4をGPIO 4番に接続
D0 = 26                                           #D0端子をGPIO 26番に接続
D1 = 16                                           #D1端子をGPIO 16番に接続
D2 = 20                                           #D2端子をGPIO 20番に接続
D3 = 21                                           #D3端子をGPIO 21番に接続
DP = 10                                           #DPをGPIO 10番に接続
LED_G = 8                                         #緑色LEDをGPIO 8番に接続
LED_R = 7                                         #赤色LEDをGPIO 7番に接続
BUZZER = 18                                       #ブザーをGPIO 18番に接続
SW1 = 6                                           #1つ目のタクトスイッチをGPIO 6番に接続
SW2 = 5                                           #2つ目のタクトスイッチをGPIO 5番に接続
SW3 = 15                                          #3つ目のタクトスイッチをGPIO 15番に接続
SW4 = 14                                          #4つ目のタクトスイッチをGPIO 14番に接続
SW5 = 11                                          #5つ目のタクトスイッチをGPIO 11番に接続
GPIO.setup(LE,GPIO.OUT,initial=GPIO.LOW)          #GPIO 25番を出力設定としてLEを制御
GPIO.setup(BL,GPIO.OUT,initial=GPIO.LOW)          #GPIO 24番を出力設定としてBLを制御
GPIO.setup(LT,GPIO.OUT,initial=GPIO.LOW)          #GPIO 23番を出力設定としてLTを制御
GPIO.setup(dig1,GPIO.OUT,initial=GPIO.LOW)        #GPIO 22番を出力設定としてdig1を制御
GPIO.setup(dig2,GPIO.OUT,initial=GPIO.HIGH)       #GPIO 27番を出力設定としてdig2を制御
GPIO.setup(dig3,GPIO.OUT,initial=GPIO.HIGH)       #GPIO 17番を出力設定としてdig3を制御
GPIO.setup(dig4,GPIO.OUT,initial=GPIO.HIGH)       #GPIO 4番を出力設定としてdig4を制御
GPIO.setup(DP,GPIO.OUT,initial=GPIO.LOW)          #GPIO 10番を出力設定としてDPを制御
GPIO.setup(D0,GPIO.OUT,initial=GPIO.LOW)          #GPIO 26番を出力設定としてD0を制御
GPIO.setup(D1,GPIO.OUT,initial=GPIO.LOW)          #GPIO 16番を出力設定としてD1を制御
GPIO.setup(D2,GPIO.OUT,initial=GPIO.LOW)          #GPIO 20番を出力設定としてD2を制御
GPIO.setup(D3,GPIO.OUT,initial=GPIO.LOW)          #GPIO 21番を出力設定としてD3を制御
GPIO.setup(LED_G,GPIO.OUT,initial=GPIO.LOW)       #GPIO 8番を出力設定として緑色LEDを制御
GPIO.setup(LED_R,GPIO.OUT,initial=GPIO.LOW)       #GPIO 7番を出力設定として赤色LEDを制御
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 6番をプルアップでの入力設定
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 5番をプルアップでの入力設定
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 15番をプルアップでの入力設定
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 14番をプルアップでの入力設定
GPIO.setup(SW5,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #GPIO 11番をプルアップでの入力設定

pi = pigpio.pi()                    #pigpioの初期化を行う
pi.set_mode(BUZZER, pigpio.INPUT)   #pigpioのピン番号および出力を設定

i2c = smbus.SMBus(1)           #インスタンスの作成
address = 0x48                 #スレーブアドレスの定義

s1 = 0                         #タクトスイッチSW1による信号の立ち下がりを検知した場合のみ1とする変数
s2 = 0                         #タクトスイッチSW2による信号の立ち下がりを検知した場合のみ1とする変数
s3 = 0                         #タクトスイッチSW3による信号の立ち下がりを検知した場合のみ1とする変数
s4 = 0                         #タクトスイッチSW4による信号の立ち下がりを検知した場合のみ1とする変数
s5 = 0                         #タクトスイッチSW5による信号の立ち下がりを検知した場合のみ1とする変数
def checkSW(pin):              #スイッチが押された時に利用する関数
    global s1                  #グローバル変数s1を定義する
    global s2                  #グローバル変数s2を定義する
    global s3                  #グローバル変数s3を定義する
    global s4                  #グローバル変数s4を定義する
    global s5                  #グローバル変数s5を定義する
    if pin == SW1:             #押されたタクトスイッチがSW1のとき
        s1 = 1                 #変数s1の値を1とする
    elif pin == SW2:           #押されたタクトスイッチがSW2のとき
        s2 = 1                 #変数s2の値を1とする
    elif pin == SW3:           #押されたタクトスイッチがSW3のとき
        s3 = 1                 #変数s3の値を1とする
    elif pin == SW4:           #押されたタクトスイッチがSW4のとき
        s4 = 1                 #変数s4の値を1とする
    elif pin == SW5:           #押されたタクトスイッチがSW5のとき
        s5 = 1                 #変数s5の値を1とする

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

def modeprinter(mode_num):             #約1秒間モード番号を左から1番目の7セグメントLEDへ表示する関数
    for p in range(222):               #以下の9行の処理を222回繰り返す
        digswitch(1, mode_num)         #左から1番目の7セグメントLEDへ、モード番号を表示する
        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機する
        digswitch(2, 10)               #左から2番目の7セグメントLEDには何も表示しない
        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機する
        digswitch(3, 10)               #左から3番目の7セグメントLEDには何も表示しない
        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機する
        digswitch(4, 10)               #左から4番目の7セグメントLEDには何も表示しない
        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機する

def read_adt7410():                               #温度センサモジュールの計測について定義する関数
    byte_data = i2c.read_byte_data(address,0x00)  #上位8bitについて変数へ代入
    data = byte_data<<8                           #左へ8bit分シフトする
    byte_data = i2c.read_byte_data(address,0x01)  #下位8bitについて変数へ代入
    data = data | byte_data                       #2つの変数に論理和を活用して変数へ代入
    data = data >> 3                              #右へ3bit分シフトする
    return data                                   #変数dataを返り値とする

GPIO.add_event_detect(SW1, GPIO.FALLING, callback=checkSW, bouncetime=200)  #SW1のイベント検出
GPIO.add_event_detect(SW2, GPIO.FALLING, callback=checkSW, bouncetime=200)  #SW2のイベント検出
GPIO.add_event_detect(SW3, GPIO.FALLING, callback=checkSW, bouncetime=200)  #SW3のイベント検出
GPIO.add_event_detect(SW4, GPIO.FALLING, callback=checkSW, bouncetime=200)  #SW4のイベント検出
GPIO.add_event_detect(SW5, GPIO.FALLING, callback=checkSW, bouncetime=200)  #SW5のイベント検出

try:                                   #目的の処理を記述する
    GPIO.output(LE, GPIO.LOW)          #LEの信号をLOWとする
    GPIO.output(BL, GPIO.HIGH)         #BLの信号をHIGHとする
    GPIO.output(LT, GPIO.HIGH)         #LTの信号をHIGHとする
    mode = 0                           #動作を行うモード番号について格納する変数
    modeprint_time = True              #モード番号の表示について実行を判定する変数
    pushed = 0                         #タクトスイッチが押された回数を格納する変数
    alarm1 = 0                         #アラーム時刻の左から1桁目を格納する変数
    alarm2 = 0                         #アラーム時刻の左から2桁目を格納する変数
    alarm3 = 0                         #アラーム時刻の左から3桁目を格納する変数
    alarm4 = 0                         #アラーム時刻の左から4桁目を格納する変数
    setup = 0                          #アラーム時刻を調整する桁番号について格納する変数
    stoptime = 0                       #ストップウォッチの計測時間を格納する変数
    timer1 = 0                         #タイマー時刻の時間数を格納する変数
    timer2 = 0                         #タイマー時刻の分数を格納する変数
    set_tim = 0                        #タイマー時刻を調整する位置について格納する変数
    timetime = 0                       #タイマーの計測時間を格納する変数
    while True:                                      #以下の46行のプログラムを繰り返す
        nowtime = datetime.datetime.now()            #現在の日時を取得
        strtime = nowtime.strftime('%Y%m%d%H%M%S')   #日時を文字列へ変換
        if s5 == 1:                                  #SW5が押された際に以下の3行を実行
            pushed = pushed + 1                      #SW5を押した回数へ1を加算する
            mode = pushed % 10                       #10で割った余りを利用し、0から9の範囲を繰り返す
            modeprint_time = True                    #モード番号の表示を実行するため、Trueを代入する
            s5 = 0                                   #変数s5の値を0にする
        
        if mode==0 or mode==1 or mode==2 or mode==3 or mode==8:   #モード番号が0、1、2、3、8の場合
            s1 = 0                           #変数s1の値を0にする
            s2 = 0                           #変数s2の値を0にする
            s3 = 0                           #変数s3の値を0にする
            s4 = 0                           #変数s4の値を0にする
        
        if mode == 0:                        #表示する種類が「西暦」の場合、以下の11行の処理を行う
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            digswitch(1, int(strtime[0]))    #左から1番目の7セグメントLEDへ、0番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(strtime[1]))    #左から2番目の7セグメントLEDへ、1番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(strtime[2]))    #左から3番目の7セグメントLEDへ、2番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[3]))    #左から4番目の7セグメントLEDへ、3番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 1:                      #表示する種類が「月日」の場合、以下の11行の処理を行う
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            digswitch(1, int(strtime[4]))    #左から1番目の7セグメントLEDへ、4番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(strtime[5]))    #左から2番目の7セグメントLEDへ、5番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(strtime[6]))    #左から3番目の7セグメントLEDへ、6番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[7]))    #左から4番目の7セグメントLEDへ、7番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 2:                      #表示する種類が「時間」の場合、以下の13行の処理を行う
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            digswitch(1, int(strtime[8]))    #左から1番目の7セグメントLEDへ、8番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(strtime[9]))    #左から2番目の7セグメントLEDへ、9番目の数字を表示する
            GPIO.output(DP, GPIO.HIGH)       #左から2番目のDPを点灯させる
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            GPIO.output(DP, GPIO.LOW)        #左から2番目のDPを消灯させる
            digswitch(3, int(strtime[10]))   #左から3番目の7セグメントLEDへ、10番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[11]))   #左から4番目の7セグメントLEDへ、11番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 3:                      #表示する種類が「秒」の場合、以下の11行の処理を行う
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            digswitch(1, 10)                 #左から1番目の7セグメントLEDには何も表示しない
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, 10)                 #左から2番目の7セグメントLEDには何も表示しない
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(3, int(strtime[12]))   #左から3番目の7セグメントLEDへ、12番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(strtime[13]))   #左から4番目の7セグメントLEDへ、13番目の数字を表示する
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 4:                      #表示する種類が「アラーム」の場合、以下の97行の処理を行う
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            if s2 == 1:                      #SW2が押された場合、アラーム時刻を調整する桁を変更する
                setup += 1                   #変数setupへ1を加算する
                setup = setup % 4            #変数setupを4で割った余りを利用し、0から3までとする
                s2 = 0                       #変数s2の値を0とする
            elif s4 == 1:                    #SW4が押された場合、アラーム時刻を調整する桁を変更する
                setup -= 1                   #変数setupから1を減算する
                setup = setup % 4            #変数setupを4で割った余りを利用し、0から3までとする
                s4 = 0                       #変数s4の値を0とする
            if setup == 0:                   #変数setupの値が0の場合、左から1番目の数字を調整する
                if s1 == 1:                  #SW1が押された場合
                    if alarm1 == 2:          #変数alarm1の値が2である場合
                        alarm1 = 0           #変数alarm1の数値を0とする
                    else:                    #変数alarm1の値が2でない場合
                        alarm1 += 1          #変数alarm1へ1を加算する
                    s1 = 0                   #変数s1の値を0とする
                elif s3 == 1:                #SW3が押された場合
                    if alarm1 == 0:          #変数alarm1の値が0である場合
                        alarm1 = 2           #変数alarm1の数値を2とする
                    else:                    #変数alarm1の値が0でない場合
                        alarm1 -= 1          #変数alarm1の値から1を減算する
                    s3 = 0                   #変数s3の値を0とする
            elif setup == 1 or setup == -1:  #変数setupの値が1または-1の場合、左から2番目の数字を調整
                if s1 == 1:                  #SW1が押された場合
                    if alarm2 == 9:          #変数alarm2の値が9である場合
                        alarm2 = 0           #変数alarm2の数値を0とする
                    else:                    #変数alarm2の値が9でない場合
                        alarm2 += 1          #変数alarm2の値へ1を加算する
                    s1 = 0                   #変数s1の値を0とする
                elif s3 == 1:                #SW3が押された場合
                    if alarm2 == 0:          #変数alarm2の値が0である場合
                        alarm2 = 9           #変数alarm2の数値を9とする
                    else:                    #変数alarm2の値が0でない場合
                        alarm2 -= 1          #変数alarm2の値から1を減算する
                    s3 = 0                   #変数s3の値を0とする
            elif setup == 2 or setup == -2:  #変数setupの値が2または-2の場合、左から3番目の数字を調整
                if s1 == 1:                  #SW1が押された場合
                    if alarm3 == 5:          #変数alarm3の値が5である場合
                        alarm3 = 0           #変数alarm3の数値を0とする
                    else:                    #変数alarm3の値が5でない場合
                        alarm3 += 1          #変数alarm3の値へ1を加算する
                    s1 = 0                   #変数s1の値を0とする
                elif s3 == 1:                #SW3が押された場合
                    if alarm3 == 0:          #変数alarm3の値が0である場合
                        alarm3 = 5           #変数alarm3の数値を5とする
                    else:                    #変数alarm3の値が0でない場合
                        alarm3 -= 1          #変数alarm3の値から1を減算する
                    s3 = 0                   #変数s3の値を0とする
            elif setup == 3 or setup == -3:  #変数setupの値が3または-3の場合、左から4番目の数字を調整
                if s1 == 1:                  #SW1が押された場合
                    if alarm4 == 9:          #変数alarm4の値が9である場合
                        alarm4 = 0           #変数alarm4の数値を0とする
                    else:                    #変数alarm4の値が9でない場合
                        alarm4 += 1          #変数alarm4の値へ1を加算する
                    s1 = 0                   #変数s1の値を0とする
                elif s3 == 1:                #SW3が押された場合
                    if alarm4 == 0:          #変数alarm4の値が0である場合
                        alarm4 = 9           #変数alarm4の数値を9とする
                    else:                    #変数alarm4の値が0でない場合
                        alarm4 -= 1          #変数alarm4の値から1を減算する
                    s3 = 0                   #変数s3の値を0とする
            alarm_time = str(alarm1) + str(alarm2) + str(alarm3) + str(alarm4)  #数字を連結
            if strtime[8:12] != alarm_time:                          #現在時刻と設定時刻が異なる時
                alarm_signal = True                                  #アラームの判定をTrueとする
            if strtime[8:12] == alarm_time and alarm_signal == True: #アラームの条件を満たす場合
                print('時間です')                                      #設定時間であることを表示する
                digswitch(4, 10)                                     #7セグメントLEDを消灯
                while(s1 != 1 and s2 != 1 and s3 != 1 and s4 != 1):  #スイッチの押下まで繰り返す
                    GPIO.output(LED_G, GPIO.HIGH)                    #緑色LEDを点灯する
                    pi.set_mode(BUZZER, pigpio.OUTPUT)               #ブザーを鳴らす
                    pi.hardware_PWM(BUZZER, 2100, 500000)            #ブザーの周波数を変更する
                    time.sleep(0.25)                                 #0.25秒待機する
                    GPIO.output(LED_G, GPIO.LOW)                     #緑色LEDを消灯する
                    GPIO.output(LED_R, GPIO.HIGH)                    #赤色LEDを点灯する
                    pi.set_mode(BUZZER, pigpio.INPUT)                #ブザーを停止
                    time.sleep(0.25)                                 #0.25秒待機する
                    GPIO.output(LED_R, GPIO.LOW)                     #赤色LEDを消灯する
                GPIO.output(LED_G,GPIO.LOW)                          #緑色LEDを消灯する
                GPIO.output(LED_R, GPIO.LOW)                         #赤色LEDを消灯する
                pi.set_mode(BUZZER, pigpio.INPUT)                    #ブザーを停止
                alarm_signal = False                                 #アラームの判定をFalseとする
                s1 = 0                   #変数s1の値を0とする
                s2 = 0                   #変数s2の値を0とする
                s3 = 0                   #変数s3の値を0とする
                s4 = 0                   #変数s4の値を0とする
            digswitch(1, int(alarm1))    #左から1番目の7セグメントLEDへ、alarm1の数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(alarm2))    #左から2番目の7セグメントLEDへ、alarm2の数字を表示する
            GPIO.output(DP, GPIO.HIGH)   #左から2番目のDPを点灯する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            GPIO.output(DP, GPIO.LOW)    #左から2番目のDPを消灯する
            digswitch(3, int(alarm3))    #左から3番目の7セグメントLEDへ、alarm3の数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(alarm4))    #左から4番目の7セグメントLEDへ、alarm4の数字を表示する
            time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 5:                  #表示する種類が「ストップウォッチ」の場合、以下の処理を実行
            if modeprint_time == True:   #モード番号の表示を実行する場合
                modeprinter(mode)        #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False   #モード番号の表示を実行しないようにFalseを代入する
            if s1 == 1 or s2 == 1:       #SW1またはSW2が押された場合、計測開始
                s1 = 0                   #変数s1の値を0とする
                s2 = 0                   #変数s2の値を0とする
                stopsignal = False                   #停止させる判定をFalseとする
                while (s1 != 1 or s2 != 1):          #SW1またはSW2が押されるまで繰り返す
                    stop_h = stoptime // 60          #計測時間を60で割った商を取り出し、分数とする
                    stop_m = stoptime % 60           #計測時間を60で割った余りを取り出し、秒数とする
                    if stop_h <= 9 and stop_m <= 9:  #分数と秒数がいずれも9以下の場合
                        stopview =str(0) + str(stop_h) + str(0) + str(stop_m) #分数と秒数へ連結
                    elif stop_h <= 9 and stop_m > 9:                   #分数が9以下、秒数が10以上
                        stopview = str(0) + str(stop_h) + str(stop_m)  #分数へ0を連結
                    elif stop_h > 9 and stop_m <= 9:                   #分数が10以上、秒数が9以下
                        stopview = str(stop_h) + str(0) + str(stop_m)  #秒数へ0を連結
                    else:                                      #分数と秒数が10以上の場合
                        stopview = str(stop_h) + str(stop_m)   #分数と秒数をそのまま連結
                    for p in range(221):                       #1秒となる221回分繰り返す
                        digswitch(1, int(stopview[-4]))  #左から1番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)                #7セグメントLEDの切り替えより、0.001秒待機
                        digswitch(2, int(stopview[-3]))  #左から2番目の7セグメントLEDへ、数字を表示
                        GPIO.output(DP, GPIO.HIGH)       #左から2番目のDPを点灯する
                        time.sleep(0.001)                #7セグメントLEDの切り替えより、0.001秒待機
                        GPIO.output(DP, GPIO.LOW)        #左から2番目のDPを消灯する
                        digswitch(3, int(stopview[-2]))  #左から3番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)                #7セグメントLEDの切り替えより、0.001秒待機
                        digswitch(4, int(stopview[-1]))  #左から4番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)                #7セグメントLEDの切り替えより、0.001秒待機
                        if s1 == 1 or s2 == 1:           #SW1またはSW2が押された場合
                            stopsignal = True            #停止させる判定をTrueとする
                            break                        #繰り返し処理を終了する
                    if s3 == 1 or s4 == 1:               #SW3またはSW4が押された場合
                        laptime0 = int(stopview[-4])     #左から1番目に表示する数字を格納
                        laptime1 = int(stopview[-3])     #左から2番目に表示する数字を格納
                        laptime2 = int(stopview[-2])     #左から3番目に表示する数字を格納
                        laptime3 = int(stopview[-1])     #左から4番目に表示する数字を格納
                        GPIO.output(LED_G, GPIO.HIGH)    #緑色LEDを点灯する
                        GPIO.output(LED_R, GPIO.HIGH)    #赤色LEDを点灯する
                        s3 = 0                           #変数s3の値を0とする
                        s4 = 0                           #変数s4の値を0とする
                        while(s3 != 1 and s4 != 1):        #SW3またはSW4が押されるまで繰り返す
                            stoptime += 1                  #計測時間へ1を加算する
                            for p in range(221):           #1秒となる221回分繰り返す
                                digswitch(1, laptime0)     #左から1番目の7セグメントLEDへ数字を表示
                                time.sleep(0.001)          #7セグメントLEDの切り替えより0.001秒待機
                                digswitch(2, laptime1)     #左から2番目の7セグメントLEDへ数字を表示
                                GPIO.output(DP, GPIO.HIGH) #左から2番目のDPを点灯する
                                time.sleep(0.001)          #7セグメントLEDの切り替えより0.001秒待機
                                GPIO.output(DP, GPIO.LOW)  #左から2番目のDPを消灯する
                                digswitch(3, laptime2)     #左から3番目の7セグメントLEDへ数字を表示
                                time.sleep(0.001)          #7セグメントLEDの切り替えより0.001秒待機
                                digswitch(4, laptime3)     #左から4番目の7セグメントLEDへ数字を表示
                                time.sleep(0.001)          #7セグメントLEDの切り替えより0.001秒待機
                        GPIO.output(LED_G, GPIO.LOW)       #緑色LEDを消灯する
                        GPIO.output(LED_R, GPIO.LOW)       #赤色LEDを消灯する
                        s3 = 0                             #変数s3の値を0とする
                        s4 = 0                             #変数s4の値を0とする
                    if stopsignal == True:                 #停止させる判定がTrueのとき
                        stopsignal = False                 #停止させる判定をFalseとする
                        break                              #繰り返し処理を終了する
                    stoptime += 1                          #計測時間へ1を加算する
                s1 = 0                                     #変数s1の値を0とする
                s2 = 0                                     #変数s2の値を0とする
                s3 = 0                                     #変数s3の値を0とする
                s4 = 0                                     #変数s4の値を0とする
                
            stop_h = stoptime // 60                        #計測時間を60で割った商を、分数とする
            stop_m = stoptime % 60                         #計測時間を60で割った余りを、秒数とする
            if stop_h <= 9 and stop_m <= 9:                #分数と秒数がいずれも9以下の場合
                stopview =str(0) + str(stop_h) + str(0) + str(stop_m)  #分数と秒数へ0を連結
            elif stop_h <= 9 and stop_m > 9:                   #分数が9以下、秒数が10以上の時
                stopview = str(0) + str(stop_h) + str(stop_m)  #分数へ0を連結
            elif stop_h > 9 and stop_m <= 9:                   #分数が10以上、秒数が9以下の時
                stopview = str(stop_h) + str(0) + str(stop_m)  #秒数へ0を連結
            else:                                      #分数と秒数が10以上の場合
                stopview = str(stop_h) + str(stop_m)   #分数と秒数をそのまま連結
            digswitch(1, int(stopview[-4]))            #左から1番目の7セグメントLEDへ、数字を表示
            time.sleep(0.001)                          #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(2, int(stopview[-3]))            #左から2番目の7セグメントLEDへ、数字を表示
            GPIO.output(DP, GPIO.HIGH)                 #左から2番目のDPを点灯する
            time.sleep(0.001)                          #7セグメントLEDを切り替えるため、0.001秒待機
            GPIO.output(DP, GPIO.LOW)                  #左から2番目のDPを消灯する
            digswitch(3, int(stopview[-2]))            #左から3番目の7セグメントLEDへ、数字を表示
            time.sleep(0.001)                          #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(4, int(stopview[-1]))            #左から4番目の7セグメントLEDへ、数字を表示
            time.sleep(0.001)                          #7セグメントLEDを切り替えるため、0.001秒待機
            
            if s3 == 1 or s4 == 1:                     #SW3またはSW4が押された場合
                stoptime = 0                           #計測時間を初期化する
                s3 = 0                                 #変数s3の値を0とする
                s4 = 0                                 #変数s4の値を0とする
        
        elif mode == 6:                      #表示する種類が「タイマー」の場合、以下の処理を実行
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            if s2 == 1:                      #SW2が押された場合、タイマーを調整する位置を変更
                set_tim += 1                 #変数set_timへ1を加算する
                set_tim = set_tim % 2        #変数set_timを2で割った余りを利用し、0から1までとする
                s2 = 0                       #変数s2の値を0とする
            if set_tim == 0:                 #変数set_timが0の場合、分数を調整する
                if s1 == 1:                  #SW1が押された場合
                    if timer1 == 99:         #変数timer1の値が99の場合
                        timer1 = 0           #変数timer1の数値を0とする
                        timetime -= 5940     #計測時間timetimeから5940を減算する
                    else:                    #変数timer1の値が99でない場合
                        timer1 += 1          #変数timer1の値へ1を加算
                        timetime += 60       #計測時間timetimeへ60を加算
                    s1 = 0                   #変数s1の値を0とする
                elif s3 == 1:                #SW3が押された場合
                    if timer1 == 0:          #変数timer1の値が0の場合
                        timer1 = 99          #変数timer1の数値を99とする
                        timetime += 5940     #計測時間timetimeへ5940を加算
                    else:                    #変数timer1の値が0でない場合
                        timer1 -= 1          #変数timer1の値から1を減算する
                        timetime -= 60       #変数timetimeから60を減算する
                    s3 = 0                   #変数s3の値を0とする
            elif set_tim == 1:               #変数set_timが1の場合、秒数を調整する
                if s1 == 1:                  #SW1が押された場合
                    if timer2 == 59:         #変数timer2の数値が59の場合
                        timer2 = 0           #timer2の数値を0とする
                        timetime -= 59       #timetimeの値から59を減算する
                    else:                    #timer2の数値が59でない場合
                        timer2 += 1          #変数timer2へ1を加算
                        timetime += 1        #計測時間timetimeへ1を加算
                    s1 = 0                   #変数s1の値を0とする
                elif s3 == 1:                #SW3が押された場合
                    if timer2 == 0:          #変数timer2の値が0の場合
                        timer2 = 59          #変数timer2の数値を59とする
                        timetime += 59       #計測時間timetimeへ59を加算
                    else:                    #変数timer2の値が0でない場合
                        timer2 -= 1          #変数timer2から1を減算する
                        timetime -= 1        #計測時間timetimeから1を減算する
                    s3 = 0                   #変数s3の値を0とする
            if s4 == 1:                      #SW4が押された場合
                stopsignal = False           #停止させる判定をFalseとする
                time_lb = False              #点滅の変化をFalseとする
                timing_ctl = 221             #繰り返しの回数を、1秒となる221回とおく
                s4 = 0                       #変数s4の値を0とする
                while (s4 != 1):             #SW4が押されるまで繰り返す
                    timer1 = timetime // 60  #計測時間を60で割った商を取り出し、分数とする
                    timer2 = timetime % 60   #計測時間を60で割った余りを取り出し、秒数とする
                    if timer1 <= 9 and timer2 <= 9:                   #分数と秒数がいずれも9以下
                        timeview =str(0) + str(timer1) + str(0) + str(timer2) #分数と秒数へ連結
                    elif timer1 <= 9 and timer2 > 9:                  #分数が9以下、秒数が10以上
                        timeview = str(0) + str(timer1) + str(timer2) #分数へ0を連結
                    elif timer1 > 9 and timer2 <= 9:                  #分数が10以上、秒数が9以下
                        timeview = str(timer1) + str(0) + str(timer2) #秒数へ0を連結
                    else:                                             #分数と秒数が10以上の場合
                        timeview = str(timer1) + str(timer2)          #分数と秒数をそのまま連結
                    for p in range(timing_ctl):         #指定された回数分繰り返す
                        digswitch(1, int(timeview[0]))  #左から1番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)               #7セグメントLEDの切り替えより、0.001秒待機
                        digswitch(2, int(timeview[1]))  #左から2番目の7セグメントLEDへ、数字を表示
                        GPIO.output(DP, GPIO.HIGH)      #左から2番目のDPを点灯する
                        time.sleep(0.001)               #7セグメントLEDの切り替えより、0.001秒待機
                        GPIO.output(DP, GPIO.LOW)       #左から2番目のDPを消灯する
                        digswitch(3, int(timeview[2]))  #左から3番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)               #7セグメントLEDの切り替えより、0.001秒待機
                        digswitch(4, int(timeview[3]))  #左から4番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)               #7セグメントLEDの切り替えより、0.001秒待機
                        if s4 == 1:                     #SW4が押された場合
                            stopsignal = True           #停止させる判定をTrueとする
                            break                       #繰り返し処理を終了する
                    if stopsignal == True:              #停止判定がTrueの場合
                        stopsignal = False              #停止させる判定をFalseとする
                        break                           #繰り返し処理を終了する
                    if timetime == 0:                   #計測時間timetimeが0となった場合
                        timing_ctl = 111                #繰り返しの回数を0.5秒となる111回とおく
                        if time_lb == False:                       #点滅の変化がFalseの場合
                            GPIO.output(LED_G, GPIO.LOW)           #緑色LEDを消灯する
                            GPIO.output(LED_R, GPIO.HIGH)          #赤色LEDを点灯する
                            pi.set_mode(BUZZER, pigpio.OUTPUT)     #ブザーを鳴らす
                            pi.hardware_PWM(BUZZER, 1050, 500000)  #ブザーの周波数を1050Hzとする
                            print('time!')                         #時間が0になったことを表示する
                            time_lb = True                         #点滅の変化をTrueとする
                        else:                                      #点滅の変化がTrueの場合
                            GPIO.output(LED_R, GPIO.LOW)           #赤色LEDを消灯する
                            GPIO.output(LED_G, GPIO.HIGH)          #緑色LEDを点灯する
                            pi.set_mode(BUZZER, pigpio.INPUT)      #ブザーを停止
                            time_lb = False                        #点滅の変化をFalseとする
                    else:                              #計測時間timetimeが0でない場合
                        timetime -= 1                  #計測時間timetimeから1を減算する
                GPIO.output(LED_G,GPIO.LOW)            #緑色LEDを消灯する
                GPIO.output(LED_R, GPIO.LOW)           #赤色LEDを消灯する
                pi.set_mode(BUZZER, pigpio.INPUT)      #ブザーを停止
                s1 = 0                           #変数s1の値を0とする
                s2 = 0                           #変数s2の値を0とする
                s3 = 0                           #変数s3の値を0とする
                s4 = 0                           #変数s4の値を0とする
            
            timer1 = timetime // 60              #計測時間を60で割った商を取り出し、分数とする
            timer2 = timetime % 60               #計測時間を60で割った余りを取り出し、秒数とする
            if timer1 <= 9 and timer2 <= 9:      #分数と秒数がいずれも9以下の場合
                timeview =str(0) + str(timer1) + str(0) + str(timer2)  #分数と秒数へ0を連結
            elif timer1 <= 9 and timer2 > 9:                   #分数が9以下、秒数が10以上の時
                timeview = str(0) + str(timer1) + str(timer2)  #分数へ0を連結
            elif timer1 > 9 and timer2 <= 9:                   #分数が10以上、秒数が9以下の時
                timeview = str(timer1) + str(0) + str(timer2)  #秒数へ0を連結
            else:                                              #分数と秒数が10以上の場合
                timeview = str(timer1) + str(timer2)           #分数と秒数をそのまま連結
            digswitch(1, int(timeview[0]))    #左から1番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)                 #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(2, int(timeview[1]))    #左から2番目の7セグメントLEDへ、数字を表示する
            GPIO.output(DP, GPIO.HIGH)        #左から2番目のDPを点灯する
            time.sleep(0.001)                 #7セグメントLEDを切り替えるため、0.001秒待機する
            GPIO.output(DP, GPIO.LOW)         #左から2番目のDPを消灯する
            digswitch(3, int(timeview[2]))    #左から3番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)                 #7セグメントLEDを切り替えるため、0.001秒待機する
            digswitch(4, int(timeview[3]))    #左から4番目の7セグメントLEDへ、数字を表示する
            time.sleep(0.001)                 #7セグメントLEDを切り替えるため、0.001秒待機する
        
        elif mode == 7:                  #表示する種類が「数字記憶ゲーム」の場合、以下の処理を実行
            if modeprint_time == True:   #モード番号の表示を実行する場合
                modeprinter(mode)        #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False   #モード番号の表示を実行しないようにFalseを代入する
            coll = False                 #ゲームを実行する判定をFalseとする
            memory = [-1,-1,-1]          #無作為に生成した整数について格納するリスト
            answer = [-1,-1,-1, 0]       #入力される解答を格納するリスト
            if s4 == 1:                  #SW4が押された場合
                score = 0                #ゲームの得点について格納する変数
                coll = True              #ゲームを実行する判定をTrueとする
                s4 = 0                   #変数s4の値を0とする
            while (coll == True):        #ゲームを実行する判定がTrueの間、繰り返す
                ans_num = 3              #7セグメントLEDへ表示する要素番号を格納する変数
                memory.append(random.randint(0,9))     #0から9の範囲の整数から、無作為に1つ生成
                for i in range (len(memory)-3):        #生成した要素の個数分繰り返す
                    for p in range(222):               #1秒となる222回分繰り返す
                        digswitch(1, int(memory[i]))   #左から1番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機
                        digswitch(2, int(memory[i+1])) #左から2番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機
                        digswitch(3, int(memory[i+2])) #左から3番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機
                        digswitch(4, int(memory[i+3])) #左から4番目の7セグメントLEDへ、数字を表示
                        time.sleep(0.001)              #7セグメントLEDを切り替えるため、0.001秒待機
                
                while (s4 != 1):                         #SW4が押されるまで繰り返す
                    digswitch(1, int(answer[ans_num-3])) #左から1番目の7セグメントLEDへ、数字を表示
                    time.sleep(0.001)                    #7セグメントLEDの切り替えより、0.001秒待機
                    digswitch(2, int(answer[ans_num-2])) #左から2番目の7セグメントLEDへ、数字を表示
                    time.sleep(0.001)                    #7セグメントLEDの切り替えより、0.001秒待機
                    digswitch(3, int(answer[ans_num-1])) #左から3番目の7セグメントLEDへ、数字を表示
                    time.sleep(0.001)                    #7セグメントLEDの切り替えより、0.001秒待機
                    digswitch(4, int(answer[ans_num]))   #左から4番目の7セグメントLEDへ、数字を表示
                    time.sleep(0.001)                    #7セグメントLEDの切り替えより、0.001秒待機
                    if s2 == 1:                   #SW2が押された場合
                        answer.append(0)          #解答を格納するリストへ要素0を加える
                        ans_num += 1              #要素番号を格納する変数へ1を加算
                        s2 = 0                    #変数s2の値を0とする
                    if s1 == 1:                   #SW1が押された場合
                        if answer[ans_num] != 9:  #解答入力位置の値が9でない場合
                            answer[ans_num] += 1  #解答入力位置の値へ1を加算
                        else:                     #解答入力位置の値が9である場合
                            answer[ans_num] = 0   #解答入力位置の数値を0とする
                        s1 = 0                    #変数s1の値を0とする
                    elif s3 == 1:                 #SW3が押された場合
                        if answer[ans_num] != 0:  #解答入力位置の値が0でない場合
                            answer[ans_num] -= 1  #解答入力位置の値から1を減算する
                        else:                     #解答入力位置の値が0である場合
                            answer[ans_num] = 9   #解答入力位置の数値を9とする
                        s3 = 0                    #変数s3の値を0とする
                s4 = 0                            #変数s4の値を0とする
                    
                if memory == answer:              #生成した整数のリストと解答のリストが一致した場合
                    digswitch(4, 10)              #7セグメントLEDを消灯する
                    score += 1                    #得点へ1を加算する
                    coll = True                   #ゲームを実行する判定をTrueとする
                    print('success!')             #正解したことを表示する
                    GPIO.output(LED_G, GPIO.HIGH)          #緑色LEDを点灯する
                    pi.set_mode(BUZZER, pigpio.OUTPUT)     #ブザーを鳴らす
                    pi.hardware_PWM(BUZZER, 1319, 500000)  #ブザーの音階を「ミ」とする
                    time.sleep(0.25)                       #0.25秒待機
                    pi.hardware_PWM(BUZZER, 1047, 500000)  #ブザーの音階を「ド」とする
                    time.sleep(0.75)                       #0.75秒待機する
                    GPIO.output(LED_G, GPIO.LOW)           #緑色LEDを消灯する
                    pi.set_mode(BUZZER, pigpio.INPUT)      #ブザーを停止
                    answer = [-1,-1,-1, 0]                 #解答を格納するリストを初期化する
                else:                                      #2つのリストが一致しない場合
                    digswitch(4, 10)                       #7セグメントLEDを消灯する
                    coll = False                           #ゲームを実行する判定をFalseとする
                    print('failed.')                       #不正解であったことを表示する
                    GPIO.output(LED_R, GPIO.HIGH)          #赤色LEDを表示する
                    pi.set_mode(BUZZER, pigpio.OUTPUT)     #ブザーを鳴らす
                    pi.hardware_PWM(BUZZER, 392, 500000)   #ブザーの周波数を392Hzとする
                    time.sleep(1.0)                        #1.0秒待機
                    pi.set_mode(BUZZER, pigpio.INPUT)      #ブザーを停止
                    f = open('game_score.txt', 'a', encoding = 'UTF-8')   #ファイルを開く
                    #下の行において西暦、日付、時刻を取得し、文字列として連結
                    tx_t =strtime[0:4]+'/'+strtime[4:8]+'/'+strtime[8:10]+':'+strtime[10:12]
                    tx_s ='  score: ' + str(score)         #得点の連結
                    f.write(tx_t + tx_s + '\n')            #文字列を連結し、ファイルへ書き込む
                    f.close()                              #ファイルを閉じる
                    if score <= 9:                         #得点が9以下の場合
                        scoreview =str(0) + str(0) + str(0) + str(score) #得点へ0を3つ連結する
                    elif 10 <= score and score <= 99:                #得点が10以上99以下の場合
                        scoreview = str(0) + str(0) + str(score)     #得点へ0を2つ連結する
                    elif 100 <= score and timer2 <= 999:             #得点が100以上999以下の場合
                        scoreview =str(0) + str(score)               #得点へ0を連結する
                    else:                                            #得点が1000以上の場合
                        scoreview = str(score)                       #得点をそのままとする
                    while (s1 != 1 and s2 != 1 and s3 != 1 and s4 != 1): #押されるまで繰り返す
                        digswitch(1, int(scoreview[-4]))  #左から1番目の7セグメントLEDへ数字を表示
                        time.sleep(0.001)                 #7セグメントLEDの切り替えより0.001秒待機
                        digswitch(2, int(scoreview[-3]))  #左から2番目の7セグメントLEDへ数字を表示
                        time.sleep(0.001)                 #7セグメントLEDの切り替えより0.001秒待機
                        digswitch(3, int(scoreview[-2]))  #左から3番目の7セグメントLEDへ数字を表示
                        time.sleep(0.001)                 #7セグメントLEDの切り替えより0.001秒待機
                        digswitch(4, int(scoreview[-1]))  #左から4番目の7セグメントLEDへ数字を表示
                        time.sleep(0.001)                 #7セグメントLEDの切り替えより0.001秒待機
                    GPIO.output(LED_R, GPIO.LOW)          #赤色LEDを消灯する
                    s1 = 0          #変数s1の値を0とする
                    s2 = 0          #変数s2の値を0とする
                    s3 = 0          #変数s3の値を0とする
                    s4 = 0          #変数s4の値を0とする
            digswitch(1, 10)        #左から1番目の7セグメントLEDへ、数字を表示
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(2, 0)         #左から2番目の7セグメントLEDへ、数字を表示
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(3, 0)         #左から3番目の7セグメントLEDへ、数字を表示
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(4, 10)        #左から4番目の7セグメントLEDへ、数字を表示
            time.sleep(0.001)       #7セグメントLEDを切り替えるため、0.001秒待機
            s1 = 0                  #変数s1の値を0とする
            s2 = 0                  #変数s2の値を0とする
            s3 = 0                  #変数s3の値を0とする
        
        elif mode == 8:                      #表示する種類が「温度」の場合、以下の処理を実行
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示する
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            module = read_adt7410()          #温度センサモジュールによる計測を実行
            if (module > 4096):              #温度が負の場合
                module = module - 8192       #温度センサモジュールの整数値から8192を引く
            module = module*0.0625           #温度センサモジュールの整数値へ0.0625をかける
            temp = str(Decimal(str(module)).quantize(Decimal('0.01'))*100)  #小数第2位で四捨五入
            for p in range(221):             #1秒となる221回分繰り返す
                digswitch(1, int(temp[0]))   #左から1番目の7セグメントLEDへ、数字を表示
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機
                digswitch(2, int(temp[1]))   #左から2番目の7セグメントLEDへ、数字を表示
                GPIO.output(DP, GPIO.HIGH)   #左から2番目のDPを点灯する
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機
                GPIO.output(DP, GPIO.LOW)    #左から2番目のDPを消灯する
                digswitch(3, int(temp[2]))   #左から3番目の7セグメントLEDへ、数字を表示
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機
                digswitch(4, int(temp[3]))   #左から4番目の7セグメントLEDへ、数字を表示
                time.sleep(0.001)            #7セグメントLEDを切り替えるため、0.001秒待機
        
        elif mode == 9:                      #表示する種類が「音楽」の場合、以下の処理を実行
            if modeprint_time == True:       #モード番号の表示を実行する場合
                modeprinter(mode)            #左から1番目の7セグメントLEDへ、モード番号を表示
                modeprint_time = False       #モード番号の表示を実行しないようにFalseを代入する
            digswitch(1, 4)                  #左から1番目の7セグメントLEDへ、4を表示
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(2, 3)                  #左から2番目の7セグメントLEDへ、3を表示
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(3, 2)                  #左から3番目の7セグメントLEDへ、2を表示
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機
            digswitch(4, 1)                  #左から4番目の7セグメントLEDへ、1を表示
            time.sleep(0.001)                #7セグメントLEDを切り替えるため、0.001秒待機
            if s1 == 1:                               #SW1が押された場合
                digswitch(4, 1)                       #左から4番目の7セグメントLEDへ、1を表示
                pi.set_mode(BUZZER, pigpio.OUTPUT)    #ブザーを鳴らす
                pi.hardware_PWM(BUZZER, 523, 500000)  #ブザーの音階を「ド」とする
                time.sleep(1.0)                       #1.0秒待機
                pi.hardware_PWM(BUZZER, 659, 500000)  #ブザーの音階を「ミ」とする
                time.sleep(1.0)                       #1.0秒待機
                pi.hardware_PWM(BUZZER, 587, 500000)  #ブザーの音階を「レ」とする
                time.sleep(1.0)                       #1.0秒待機
                pi.hardware_PWM(BUZZER, 392, 500000)  #ブザーの音階を「ソ」とする
                time.sleep(3.0)                       #3.0秒待機
            elif s2 == 1:                             #SW2が押された場合
                digswitch(4, 2)                       #左から4番目の7セグメントLEDへ、2を表示
                pi.set_mode(BUZZER, pigpio.OUTPUT)    #ブザーを鳴らす
                GPIO.output(LED_G, GPIO.HIGH)         #緑色LEDを点灯する
                pi.hardware_PWM(BUZZER, 523, 500000)  #ブザーの音階を「ド」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 587, 500000)  #ブザーの音階を「レ」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 659, 500000)  #ブザーの音階を「ミ」とする
                time.sleep(0.5)                       #0.5秒待機
                pi.hardware_PWM(BUZZER, 587, 500000)  #ブザーの音階を「レ」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 523, 500000)  #ブザーの音階を「ド」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 0, 500000)    #ブザーを一時停止する
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 523, 500000)  #ブザーの音階を「ド」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 587, 500000)  #ブザーの音階を「レ」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 659, 500000)  #ブザーの音階を「ミ」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 587, 500000)  #ブザーの音階を「レ」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 523, 500000)  #ブザーの音階を「ド」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 587, 500000)  #ブザーの音階を「レ」とする
                time.sleep(1.0)                       #1.0秒待機
            elif s3 == 1:                             #SW3が押された場合
                digswitch(4, 3)                       #左から4番目の7セグメントLEDへ、3を表示
                GPIO.output(LED_R, GPIO.HIGH)         #赤色LEDを点灯する
                pi.set_mode(BUZZER, pigpio.OUTPUT)    #ブザーを鳴らす
                pi.hardware_PWM(BUZZER, 784, 500000)  #ブザーの音階を「ソ」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 0, 500000)    #ブザーを一時停止する
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 784, 500000)  #ブザーの音階を「ソ」とする
                time.sleep(0.2)                       #0.2秒待機
                pi.hardware_PWM(BUZZER, 880, 500000)  #ブザーの音階を「ラ」とする
                time.sleep(2.0)                       #2.0秒待機
            elif s4 == 1:                              #SW4が押された場合
                digswitch(4, 4)                        #左から4番目の7セグメントLEDへ、4を表示
                GPIO.output(LED_G, GPIO.HIGH)          #緑色LEDを点灯する
                GPIO.output(LED_R, GPIO.HIGH)          #赤色LEDを点灯する
                pi.set_mode(BUZZER, pigpio.OUTPUT)     #ブザーを鳴らす
                pi.hardware_PWM(BUZZER, 988, 500000)   #ブザーの音階を「シ」とする
                time.sleep(0.2)                        #0.2秒待機
                pi.hardware_PWM(BUZZER, 1397, 500000)  #ブザーの音階を「ファ」とする
                time.sleep(0.2)                        #0.2秒待機
                pi.hardware_PWM(BUZZER, 0, 500000)     #ブザーを一時停止する
                time.sleep(0.2)                        #0.2秒待機
                pi.hardware_PWM(BUZZER, 1397, 500000)  #ブザーの音階を「ファ」とする
                time.sleep(0.2)                        #0.2秒待機
                pi.hardware_PWM(BUZZER, 0, 500000)     #ブザーを一時停止する
                time.sleep(0.05)                       #0.05秒待機
                pi.hardware_PWM(BUZZER, 1397, 500000)  #ブザーの音階を「ファ」とする
                time.sleep(0.2)                        #0.2秒待機
                pi.hardware_PWM(BUZZER, 1319, 500000)  #ブザーの音階を「ミ」とする
                time.sleep(0.2)                        #0.2秒待機
                pi.hardware_PWM(BUZZER, 1175, 500000)  #ブザーの音階を「レ」とする
                time.sleep(0.2)                        #0.2秒待機
                pi.hardware_PWM(BUZZER, 1047, 500000)  #ブザーの音階を「ド」とする
                time.sleep(1.0)                        #1.0秒待機
            GPIO.output(LED_G, GPIO.LOW)       #緑色LEDを消灯する
            GPIO.output(LED_R, GPIO.LOW)       #赤色LEDを消灯する
            pi.set_mode(BUZZER, pigpio.INPUT)  #ブザーを停止
            s1 = 0                             #変数s1の値を0とする
            s2 = 0                             #変数s2の値を0とする
            s3 = 0                             #変数s3の値を0とする
            s4 = 0                             #変数s4の値を0とする

except KeyboardInterrupt:       #プログラムの停止指示を検知
    pass                        #何もせずに終了する

pi.stop()                       #pigpioを停止
GPIO.cleanup()                  #GPIOの設定を初期化