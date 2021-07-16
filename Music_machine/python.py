import serial
from pygame import mixer
import time
import pyautogui
import math
#mixer.init()
#mixer.music.load('/home/klepsydra/Music/Frozen-Let it go.mp3')
#mixer.music.play()


ser = serial.Serial('/dev/ttyUSB0', 9600)

time.sleep(2)
time.sleep(2)


while(True):
    b = ser.readline()
    fg = b.decode()
    q = fg.rstrip()
    a = q.find('+')
    b = q.find('-')
   # c = q.find('_')
    #d = q.find('*')
    s1 = q[0:a]
    s2 = q[a+1:b]
    s3 = q[b+1: len(q)]
    #s4 = q[c+1:d]
    #s5 = q[d+1:len(q)]
    r1=int(s1)
    r2=int(s2)
    r3=int(s3)
    #r4=int(s4)
    #r5=int(s5)
   # print(r1)
   # print(r2)
    #print(r3)
    #print(r4)
    #print(r5)
    if(r1<=3):
        pyautogui.press('d')

    if(r1<=6 and r1>3):
        pyautogui.press('f')

    if(r1<=12 and r1>6):
        pyautogui.press('g')

    if(r1<=15 and r1>12):
        pyautogui.press('h')

    if(r1<=18 and r1>15):
        pyautogui.press('j')

    if(r1<=21 and r1>18):
        pyautogui.press('J')

    if(r1<=24 and r1>21):
        pyautogui.press('l')


    if(r1<=27 and r1>24):
        pyautogui.press('S')
    if(r2<=3):
        pyautogui.press('G')

    if(r2<=6 and r2>3):
        pyautogui.press('H')

    if(r2<=12 and r2>6):
        pyautogui.press('L')

    if(r2<=15 and r2>12):
        pyautogui.press('Z')

    if(r2<=18 and r2>15):
        pyautogui.press('J')

    if(r2<=21 and r2>18):
        pyautogui.press('P')

    if(r2<=24 and r2>21):
        pyautogui.press('O')


    if(r2<=27 and r2>24):
        pyautogui.press('I')
    if(r3<=3):
        mixer.init()
        mixer.music.load("/home/klepsydra/Music/Lost_Frequencies_Feat_Easton_Corbin-Are_You_With_Me_Original_mix_(iPlayer.fm).mp3")
        mixer.music.play()

    if(r3<=6 and r3>3):
        mixer.init()
        mixer.music.load("/home/klepsydra/Music/One Of Those Nights.mp3")
        mixer.music.play()



