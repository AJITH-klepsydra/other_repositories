from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
import serial
import serial
from PyQt5 import uic,QtWidgets,QtCore
import pyautogui
import time
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key, Listener
import multiprocessing
pyautogui.FAILSAFE = False
m1 = mouse.Controller()
def on_functionf8(key):                                                                  #function that handles keystrokes
    handle = open("log.klep" , 'a')
    handle.write("press: " + str(key) + '\n')

    handle.close()
def on_scroll(x, y, dx, dy):                                                            #function to monitor scroll events and store it
    handle = open('log.klep', 'a')
    handle.write("scroll: " + str(dx) + ' ' + str(dy) + '\n')
    time.sleep(0.009)
    handle.close()


def on_click(x, y, button, pressed):
    if(pressed):
        if (button == mouse.Button.left):
            handle = open("log.klep", "a")                                                   #function to handle mouse click event and store it  
            handle.write("click: " + str(x) + ' ' + str(y) +'\n')
            handle.close()
        if(button == mouse.Button.right):  
            handle = open("log.klep", "a")                                                   #function to handle mouse click event and store it  
            handle.write("clickr: " + str(x) + ' ' + str(y) +'\n')
            handle.close()  
        
    
       # handle.write("clickr: " + str(x) + ' ' + str(y) +'\n')

    



#Main window class
class main(QtWidgets.QMainWindow):                                                      #MainWindow class
    sig = QtCore.pyqtSignal()
    inf = QtCore.pyqtSignal()
    tm = QtCore.pyqtSignal()
    re = QtCore.pyqtSignal()
    strt = QtCore.pyqtSignal()    
    def __init__(self):
        super(main,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/pillow.ui',self)

        self.info.clicked.connect(self.to_info)
        self.btn_3.clicked.connect(self.to_rep)
        self.btn_4.clicked.connect(self.to_strt)

        self.show()
#repeter function
    def to_rep(self):
        self.re.emit()
    def to_strt(self):
        self.strt.emit()
#info function
    def to_info(self):
        self.inf.emit()
#arduino function

#repeter class
class rep(QtWidgets.QMainWindow):
    bck_r = QtCore.pyqtSignal()
    fin=QtCore.pyqtSignal(str)
    def __init__(self):
        super(rep,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/rep.ui',self)
        self.rec1.clicked.connect(self.repeter_f) 
        self.rp.clicked.connect(self.bck_rf)



    def repeter_f(self):
        self.rec1.setText("DONE!!") 
        self.rec1.setStyleSheet("background-color: red")
                                
        f = open("log.klep",'+w')
        f.close()
        k=int(self.tm.text())
        key_listener = keyboard.Listener(on_release=on_functionf8)
        key_listener.start()
        listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
        listener.start()
        time.sleep(k)
        listener.stop()
        key_listener.stop()
        listener.join()
        strng="Time Expired"
        self.fin.emit(strng)

 
        
    def bck_rf(self):
        self.bck_r.emit()

#arduino class

#help class
class hel(QtWidgets.QMainWindow):
    def __init__(self):
        super(hel,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/help.ui',self)
        self.show()

class start(QtWidgets.QMainWindow):
    bck4 = QtCore.pyqtSignal()
    
    def __init__(self):
        super(start,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/start.ui',self)
        self.rp2_2.clicked.connect(self.back4)
        self.rep_s.clicked.connect(self.l_start)

        self.show()
    def back4 (self):
        self.bck4.emit()
    def l_start(self):
        handle = open("log.klep","r")


        it = self.it.text()
        it = int(it)
        k1=0
        while(k1<it):
            for line in handle:
                tg = float(self.tg.text())
                key_1=""  
                if(line.startswith('press:')):
                    key = line.strip().split()
                    for k_ in key[-1]:
                        if(k_ != '\''):
                            key_1 = key_1+k_
                if(len(key_1) == 1):
                    print(key_1)
                    pyautogui.press(key_1)
                    time.sleep(tg)
                else:
                    if(key_1 == 'Key.space'):
                        pyautogui.press('space')
                        time.sleep(tg)
                        print("done")

                    elif(key_1 =='Key.enter'):
                        pyautogui.press('enter')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.shift_r'):
                        pyautogui.press('shiftright')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.alt'):
                        pyautogui.press('altleft')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.shift'):
                        pyautogui.press('shiftleft')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.tab'):
                        pyautogui.press('tab')
                        time.sleep(tg)
                        print("done")

                    elif(key_1 =='Key.f1'):
                        pyautogui.press('f1')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f2'):
                        pyautogui.press('f2')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f3'):
                        pyautogui.press('f3')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f4'):
                        pyautogui.press('f4')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f5'):
                        pyautogui.press('f5')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f6'):
                        pyautogui.press('f6')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f7'):
                        pyautogui.press('f7')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f8'):
                        pyautogui.press('f8')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f9'):
                        pyautogui.press('f9')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f10'):
                        pyautogui.press('f10')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f11'):
                        pyautogui.press('f11')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.f12'):
                        pyautogui.press('f12')
                        time.sleep(tg)
                        print("done")

                    elif(key_1 =='Key.insert'):
                        pyautogui.press('insert')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.delete'):
                        pyautogui.press('delete')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.page_up'):
                        pyautogui.press('pageup')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.page_down'):
                        pyautogui.press('pagedown')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.home'):
                        pyautogui.press('home')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.end'):
                        pyautogui.press('end')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.backspace'):
                        pyautogui.press('backspace')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.left'):
                        pyautogui.press('left')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.right'):
                        pyautogui.press('right')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.down'):
                        pyautogui.press('down')
                        time.sleep(tg)
                        print("done")
                    elif(key_1 =='Key.up'):
                        pyautogui.press('up')
                        time.sleep(tg)
                        print("done")
        
                    
                    
                    

                    
                if (line.startswith('click:')):
                    click = line.strip().split()
                    pyautogui.click(int(click[-2]),int(click[-1]))
                    print(int(click[-2]), int(click[-1]))
                    time.sleep(0.25)
                if (line.startswith('scroll:')):
                    scroll = line.strip().split()
                    m1.scroll(int(scroll[-2]),int(scroll[-1]))
                    print(int(scroll[-2]), int(scroll[-1]))
                    time.sleep(0.05)
                if(line.startswith('clickr:')):
                    clickr = line.strip().split()
                    pyautogui.rightClick(int(clickr[-2]),int(clickr[-1]))

            k1 = k1+1
            

            print("k1",k1)
            handle = open("log.klep","r")

           
        print(k1,it)
        handle.close()
        if(it == k1):
            sys.exit()

#info class        
class info(QtWidgets.QMainWindow):
    inr = QtCore.pyqtSignal()
    her = QtCore.pyqtSignal()
    def __init__(self):
        super(info,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/info.ui',self)
        self.inb.clicked.connect(self.on)
        self.help.clicked.connect(self.hell)
        self.show()
    def hell(self):
        self.her.emit()
    def on(self):
        self.inr.emit()
class out(QtWidgets.QMainWindow):
    def __init__(self):
        super(out,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/timeex.ui',self)
        self.show()
     
class ctr:
    def __init__(self):
        pass
    def show_main(self):
        self.window = main()
        self.window.show()
        self.window.sig.connect(self.next)
        self.window.strt.connect(self.s_start)

        self.window.inf.connect(self.infop)
        self.window.re.connect(self.show_rep)
        self.window.setWindowTitle("REPEATER")
    def s_start(self):
        self.start_1=start()
        self.start_1.setWindowTitle("REPEATER")
        
        self.start_1.bck4.connect(self.back5)

        self.window.hide()

    def back5(self):
        self.start_1.close()
        self.window.show()
    def show_rep(self):
        self.repp = rep()

        self.repp.show()
        self.window.hide()
        self.repp.bck_r.connect(self.bck_r)
        self.repp.fin.connect(self.final)
        self.repp.setWindowTitle("REPEATER")
    def final(self,text):
        self.out = out()
        self.out.show()
        self.out.setWindowTitle("message")
        self.out.label.setText(text)
        
        
    def bck_r(self):
        self.window.show()
        self.repp.close()

    def back(self,x):
            self.window.show()
            self.win2.hide()
    def back3(self):
        self.inp.close()
        self.window.show()
        
    def back2(self):
        self.window.show()
        self.win2.hide()
    def infop(self):
        self.inp = info()
        self.inp.show()
        self.window.hide()
        x=5
        self.inp.her.connect(self.help1)
    
        self.inp.inr.connect(self.back3)
        self.inp.setWindowTitle("INFO")
    def help1(self):
        self.hel2 = hel()
        self.hel2.show()
        self.hel2.setWindowTitle("HELP")
        
    def next(self):
        self.win2 = second()
        self.win2.show()
        self.win2.bk.connect(self.back2)
        self.window.hide()
        self.win2.setWindowTitle("ARD MAPPER")
def ma():
    appctxt = ApplicationContext()
    ctrl = ctr()
    ctrl.show_main()
    sys.exit(appctxt.app.exec_()  )
if(__name__ == '__main__'):
    ma()
