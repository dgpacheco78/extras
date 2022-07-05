from tkinter import Entry, Frame,Label,Button,Checkbutton,Scale,StringVar,IntVar
from tkinter.constants import DISABLED
import serial
import time

class MainFrame(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=300, height=250)                
        self.master = master    
        self.master.protocol('WM_DELETE_WINDOW',self.askQuit)
        self.pack()
        self.arduino = serial.Serial("COM3",9600,timeout=1.0)
        time.sleep(1)
        self.value_pin1 = StringVar()
        self.value_pin2 = StringVar()
        self.value_pin3 = StringVar()
        self.create_widgets()
        self.isRun=True

    def askQuit(self):
        self.isRun=False
        self.arduino.write('0'.encode('ascii'))
        time.sleep(1.1)
        self.arduino.close()
        self.master.quit()
        self.master.destroy()
        print("*** finalizando...")

    def getSensorValues(self):
        while self.isRun:
            cad =self.arduino.readline().decode('ascii').strip()
            if cad:
                print(cad)         
                pos=cad.index(":")
                label=cad[:pos]
                value=cad[pos+1:]
                if label == 'pes':
                    self.value_dis.set(value)                   
                if label == 'tem':
                    self.value_pot.set(value)
                    
    def fEnviaColores(self):
        cad = self.value_pin1.get() + "a" + self.value_pin2.get() + "b" + self.value_pin3.get()
        self.arduino.write(cad.encode('ascii'))
        print(cad)

    def create_widgets(self):
        Label(self,text="R: ", font=('Georgia 20')).place(x=30,y=20)
        Entry(self,width=8,textvariable=self.value_pin1,justify='center', font=('Georgia 20')).place(x=100,y=20)
        Label(self,text="G: ", font=('Georgia 20')).place(x=30,y=70)
        Entry(self,width=8,textvariable=self.value_pin2,justify='center', font=('Georgia 20')).place(x=100,y=70)
        Label(self,text="B: ", font=('Georgia 20')).place(x=30,y=120)
        Entry(self,width=8,textvariable=self.value_pin3,justify='center', font=('Georgia 20')).place(x=100,y=120)
        Button(self,text="Enviar", font=('Georgia 20'), command=self.fEnviaColores).place(x=100,y=180)