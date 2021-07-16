import serial
from pygame import mixer
import time
import pyautogui
import math
import random

#mixer.init()
#mixer.music.load('/home/klepsydra/Music/Frozen-Let it go.mp3')
#mixer.music.play()

ser_port=input("Serial port : \n eg: /dev/ttyACM0::")
ser = serial.Serial(ser_port, 9600)

time.sleep(2)
time.sleep(2)


while(True):
    bbb = ser.readline()
    fg = bbb.decode()
    q = fg.rstrip()
    a = q.find('+')
    b = q.find('-')
    c = q.find('*')
    s1 = q[0:a]
    s2 = q[a+1:b]
    s3 = q[b+1:c]
    s4 = q[c+1:len(q)]
    if(s1.isdigit() and s2.isdigit()):
        r2=int(s1)
        r1=int(s2)
        r3=int(s3)
        r4=int(s4)
        if(r1<=12):
          pyautogui.press('s')

        if(r1<=25 and r1>12):
          pyautogui.press('d')

        if(r1<=38 and r1>25):
            pyautogui.press('f')

        if(r1<=50 and r1>38):
            pyautogui.press('g')

        if(r1<=64 and r1>50):
            pyautogui.press('h')

        if(r1<=78 and r1>64):
           pyautogui.press('j')

        if(r1<=90 and r1>78):
           pyautogui.press('k')
 #controller 2

        if(r2<=12):
          pyautogui.press('s')

        if(r2<=25 and r2>12):
          pyautogui.press('v')

        if(r2<=50 and r2>38):
            pyautogui.press('b')

        if(r2<=64 and r2>50):
            pyautogui.press('v')

        if(r2<=78 and r2>64):
            pyautogui.press('b')

        if(r2<=90 and r2>78):
           pyautogui.press('x')

        if(r2<=38 and r2>25):
            pyautogui.press('d')

#controller 3

        if(r3<=12):
          pyautogui.press('v')

        if(r3<=25 and r3>12):
          pyautogui.press('g')

        if(r3<=38 and r3>25):
            pyautogui.press('s')

        if(r3<=50 and r3>38):
            pyautogui.press('f')

        if(r3<=67 and r3>50):
            pyautogui.press('j')

        if(r3<=78 and r3>67):
           pyautogui.press('b')

        if(r3<=90 and r3>78):
           pyautogui.press('k')
#contr 4

        if(r4<=12):
          pyautogui.press('d')

        if(r4<=25 and r4>12):
          pyautogui.press('j')

        if(r4<=37 and r4>25):
            pyautogui.press('v')

        if(r4<=50 and r4>37):
            pyautogui.press('x')

        if(r4<=67 and r4>50):
            pyautogui.press('h')

        if(r4<=78 and r4>67):
           pyautogui.press('k')

        if(r4<=90 and r4>78):
           pyautogui.press('d')

#contr 5

