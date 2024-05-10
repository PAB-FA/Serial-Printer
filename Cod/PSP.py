from tkinter import * 
from tkinter import ttk      
from tkinter.filedialog import asksaveasfilename
import serial
import time
import serial.tools.list_ports
from datetime import datetime
import re
import os
import subprocess
ser = serial.Serial()

window = Tk()
window.title("P-Serial Printer")
window.minsize(1252,452)
window.maxsize(1252,452)
window.resizable(width=False,height=False)
window.config(bg="black",background='black')


Tol = 0


port_var = StringVar()
ports = ['none']
def PortList():
    global port_var
    global ports
    ports = list(serial.tools.list_ports.comports())
    ports = [(p.device +" : "+ p.description[0:15]+"...") for p in ports]
    port_menu.config(value=ports)
    try:
        port_menu.current(0)
    except:
        pass

baud_var = IntVar()
baud_var.set(9600)

delay_var = DoubleVar()
delay_var.set(0.0)
maxcaracter = IntVar()
maxcaracter.set(200)
PrintTime = IntVar()
ReadString = IntVar()
PrintTime.set(0)
Autoscroolx = IntVar()
Autoscrooly = IntVar()
NLineB = IntVar()
Autoscrooly.set(1)
Ghrapig = IntVar()
bytesize_var = IntVar()
bytesize_var.set(8)
timeout_var = DoubleVar()
timeout_var.set(1)
stopbit_var = DoubleVar()
stopbit_var.set(1)
conn_var = BooleanVar()
conn_var.set(False)
parity_options = ["NONE", "EVEN", "ODD", "MARK", "SPACE"]
parity_var = StringVar(window)
parity_var.set("NONE")
While = False
def toggle_conn():
    global ser
    global While
    with open("V.txt", "r") as f:
        V = f.read()
    if  V == "OFF":
        ReportWindow.insert(END,"Plase Close P-TSPlotter") 
    else :
        if conn_var.get():
            ser.close() 
            conn_var.set(False)
            While = False
            conectport.config(text="Disconected",background="red") 
        else: 
            port = port_var.get()
            ser.port = port[0:5] 
            ser.baudrate = baud_var.get() 
            ser.bytesize = bytesize_var.get()
            ser.timeout = timeout_var.get()
            ser.stopbits = stopbit_var.get()
            if parity_var.get() == "ODD" : ser.parity=serial.PARITY_ODD
            if parity_var.get() == "EVEN" : ser.parity=serial.PARITY_EVEN
            if parity_var.get() == "NONE" : ser.parity=serial.PARITY_NONE
            if parity_var.get() == "MARK" : ser.parity=serial.PARITY_MARK
            if parity_var.get() == "SPACE" : ser.parity=serial.PARITY_SPACE
            ser.open() 
            conn_var.set(True) 
            While = True 
            conectport.config(text="Connected",background="green",activebackground="white")
            read_data()
        

datar = ['Start',]
def read_data():
    global ser
    global Tol
    global datar
    global While
    while While == True:
        now = datetime.now()
        car = maxcaracter.get()
        if NLineB.get() == 0:
            data = ser.readline(car)
        else :
            data = ser.read()
        if PrintTime.get() == 1 : 
            if ReadString.get() == 1 : 
                datap = str(" " + now.strftime("%H:%M:%S.%f")[0:12]) + "-> " + str(data) 
                datar.append(datap)
            else :
                datap = str(" " + now.strftime("%H:%M:%S.%f")[0:12]) + "-> " + str(data)[2:len(data)]
                datar.append(datap)
            ReportWindow.insert(END, datap) 
        else: 
            if ReadString.get() == 1 : 
                ReportWindow.insert(END, str(data)) 
                datar.append(datap)
            else : 
                ReportWindow.insert(END, data) 
                datar.append(data)
        if Autoscrooly.get() == 1 : ReportWindow.yview(END)
        if Autoscroolx.get() == 1 : ReportWindow.xview(len(data))
        if Ghrapig.get() == 1 : Ghrapnum(data)
        Tol = Tol + 1
        scale.config(to=Tol)
        time.sleep(delay_var.get())
        window.update()
def CLAD():    
    Maxnum0.config(text="") 
    Minnum0.config(text="")
    Avernum0.config(text="")
    NameL0.config(text="")
    ValL0.config(text="")
    Maxnum1.config(text="") 
    Minnum1.config(text="")
    Avernum1.config(text="")
    NameL1.config(text="")
    ValL1.config(text="")
    Maxnum2.config(text="") 
    Minnum2.config(text="")
    Avernum2.config(text="")
    NameL2.config(text="")
    ValL2.config(text="")
    Maxnum3.config(text="") 
    Minnum3.config(text="")
    Avernum3.config(text="")
    NameL3.config(text="")
    ValL3.config(text="")
    Maxnum4.config(text="") 
    Minnum4.config(text="")
    Avernum4.config(text="")
    NameL4.config(text="")
    ValL4.config(text="")
    global my_dict
    global my_dicttow
    my_dict = {'MAX0': '-1000', 'MAX1': '-1000', 'MAX2': '-1000', 'MAX3': '-1000','MAX4':'-1000'}
    my_dicttow = {'MAX0': '10000', 'MAX1': '10000', 'MAX2': '10000', 'MAX3': '10000','MAX4':'10000'}
def Clear():
    global Tol
    ReportWindow.delete(0,END)
    Tol = 0
    scale.config(to=Tol)
def SaveWin():
    global folder_path
    global datar
    folder_path = asksaveasfilename(filetypes=[("Text files", "*.txt")])
    print(folder_path + ".txt")
    with open(folder_path + ".txt",'w') as file :
        file.write(str(datar))
        file.close()
        ReportWindow.insert(END,"Saved")
def Scroll(val):
    ReportWindow.yview(val)
def Ghrapnum(val):
    try:
        val = val.decode('utf-8')
        val = str(val)
        num = re.findall(r'[-+]?[0-9]*\.?[0-9]+', val)
        name = re.findall(r'[-+]?[a-zA-Z]*\.?[a-zA-Z]+', val)
        for i in range(0,len(num)):
            PAD(num,name,i)
    except:
        ReportWindow.insert(END,"DA > cannot recognize the data <")
def PAD(DATA1,DATA2,NUM):
    DATAA = DATA1[NUM]
    DATAB = DATA2[NUM]
    
    if len(DATA1) > NUM - 1:
            eval("ValL"+str(NUM)).config(text="V: " + (str(DATAA))[0:5])
            eval("NameL"+str(NUM)).config(text="LN: " + (DATAB)[0:5])
            eval("Maxnum"+str(NUM)).config(text="MA: "+ (str(my_dict["MAX" + str(NUM)]))[0:5])
            eval("Minnum"+str(NUM)).config(text="MI: "+ (str(my_dicttow["MAX" + str(NUM)]))[0:5])
            eval("Avernum"+str(NUM)).config(text="AV: "+ str((int((str(my_dict["MAX" + str(NUM)]))[0:5]) +  int((str(my_dicttow["MAX" + str(NUM)]))[0:5])) /2))
            PND(DATAA,NUM)


my_dict = {'MAX0': '-1000', 'MAX1': '-1000', 'MAX2': '-1000', 'MAX3': '-1000','MAX4':'-1000'}
my_dicttow = {'MAX0': '10000', 'MAX1': '10000', 'MAX2': '10000', 'MAX3': '10000','MAX4':'10000'}
def PND(NUMD,NUM):
    if int(NUMD) > int(my_dict["MAX"+str(NUM)]):
        my_dict["MAX" + str(NUM)] = int(NUMD)
    if int(NUMD) < int(my_dicttow["MAX"+str(NUM)]):
        my_dicttow["MAX" + str(NUM)] = int(NUMD)
def send_serial ():
    global ser
    value = ENTRY.get () 
    ReportWindow.insert(END,"Send -> " + value)
    value = bytes(value,"utf-8")
    ser.write (value)
def OpenPlott():
    if conn_var.get():
        toggle_conn()
        with open("PORT.txt", "w") as f:
            P = port_var.get()
            f.write(str(P)[0:5] + str(baud_var.get()) +" "+  str(timeout_var.get()))
        ReportWindow.insert(END, "In order to work with this program, it is enough to close the Politer program")
        ReportWindow.insert(END, "otherwise the program will not be implemented.")
        ReportWindow.insert(END, "Run Plotter")
        ReportWindow.insert(END, "Pleas Wiat...")
        window.update()
        time.sleep(1)
        ReportWindow.insert(END, "Welcome Back im Redy.")
        subprocess.run(["./PTSP.exe"])
    else:
        ReportWindow.insert(END, "Pleas Connect Port") 
        
    
Frametree = LabelFrame(window,text="Print setting",bg="black",fg="white",width=208,height=148)
Frameone = LabelFrame(window,text="Port setting",bg="black",fg="white",width=208,height=210)
Frametow = LabelFrame(window,text="Monitor",bg="black",fg="white",width=758,height=428)
Framefor= LabelFrame(window,text="Data analysis",bg="black",fg="white",width=230,height=428)
LabelPort = Label(window,text="Port =",bg="black",fg="white")
port_menu = ttk.Combobox(window,width=22,values=ports,textvariable=port_var)
refreshport = Button(window,text="Refresh Port List",command=PortList,background="black",foreground="white")
conectport = Button(window,text="Connect Port",command=toggle_conn,background="black",foreground="white",width=12)
baud_label = Label(window, text="Baud rate:",background="black",foreground="white")
baud_spin = Spinbox(window, from_=1200, to=2000000, increment=1200, textvariable=baud_var,width=18,background="black",foreground="green")
ReportWindow = Listbox(window,width=76,height=19,background="black",fg="green",font=("Arial","12","bold"))
delay_label = Label(window, text="Time Sleep:",background="black",foreground="white")
delay_spin = Spinbox(window, from_=0.00, to=1, increment=0.05, textvariable=delay_var,width=16,background="black",foreground="green")
bytesize_label = Label(window, text="Byte Size:",background="black",foreground="white")
bytesize_spin = Spinbox(window, from_=0, to=32, increment=1, textvariable=bytesize_var,width=3,background="black",foreground="green")
Button_clear = Button(window,text="Clear Window",command=Clear,background="black",foreground="white",width=12)
Button_Save = Button(window,text="Save Window",command=SaveWin,background="black",foreground="white",width=12)
Timeout_label = Label(window, text="Timeout :",background="black",foreground="white")
Timeout_spin = Spinbox(window, from_=0, to=2, increment=0.01, textvariable=timeout_var,width=3,background="black",foreground="green")
stopbit_label = Label(window, text="Stop Bit :",background="black",foreground="white")
stopbit_spin = Spinbox(window, from_=1, to=2, increment=0.5, textvariable=stopbit_var,width=5,background="black",foreground="green")
parity_menu = OptionMenu(window, parity_var, *parity_options)
Printtime = Checkbutton(window,text="Print Time",variable=PrintTime,background="black",fg="green",activebackground="black",activeforeground="green")
Autoend = Checkbutton(window,text="Auto Scroll",variable=Autoscrooly,background="black",fg="green",activebackground="black",activeforeground="green")
Autodown = Checkbutton(window,text="Auto Go End",variable=Autoscroolx,background="black",fg="green",activebackground="black",activeforeground="green")
Ghrapick = Checkbutton(window,text="Data analysis (ROLAN) (!)",variable=Ghrapig,background="black",fg="green",activebackground="black",activeforeground="green")
Ghrapig.set(1)
Readstring = Checkbutton(window,text="Read String",variable=ReadString,background="black",fg="green",activebackground="black",activeforeground="green")
scale = Scale(window, length=378,width=5, orient="vertical", from_=0, to=Tol, command=Scroll,bg="black",fg="green",activebackground="green")
NameL0 = Label(window,text="TAGVBDJN",background="black",foreground="white")
ValL0 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Maxnum0 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Avernum0 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Minnum0 = Label(window,text="TAGVBDJN",background="black",foreground="white")
NameL1 = Label(window,text="TAGVBDJN",background="black",foreground="white")
ValL1 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Maxnum1 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Avernum1 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Minnum1 = Label(window,text="TAGVBDJN",background="black",foreground="white")
NameL2 = Label(window,text="TAGVBDJN",background="black",foreground="white")
ValL2 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Maxnum2 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Avernum2 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Minnum2 = Label(window,text="TAGVBDJN",background="black",foreground="white")
NameL3 = Label(window,text="TAGVBDJN",background="black",foreground="white")
ValL3 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Maxnum3 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Avernum3 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Minnum3 = Label(window,text="TAGVBDJN",background="black",foreground="white")
NameL4 = Label(window,text="TAGVBDJN",background="black",foreground="white")
ValL4 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Maxnum4 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Avernum4 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Minnum4 = Label(window,text="TAGVBDJN",background="black",foreground="white")
Maxcaracter_label = Label(window, text="Max Char in Line :",background="black",foreground="white")
Maxcaracter = Spinbox(window,text="hi", from_=1, to=500, increment=5, textvariable=maxcaracter,width=5,background="black",foreground="green")
NLIB= Checkbutton(window,text="RB",variable=NLineB,background="black",fg="green",activebackground="black",activeforeground="green")
ENTRY = Entry (window,background="black",foreground="white",width=27) 
SEND = Button(window,text="Send",command=send_serial,background="black",foreground="white")
V = Label(window,text="PABFA - Serial Printer V1.6.0",background="black",foreground="blue")
CLADB = Button(window,text="CL",command=CLAD,background="black",foreground="green")
OpenPlottB = Button(window,text="Open Plotter",command=OpenPlott,background="white",foreground="black",width=28)
Frameone.place(x=780,y=10)
Frametow.place(x=10,y=10)
LabelPort.place(x=785,y=30)
port_menu.place(x=823,y=31)
refreshport.place(x=788,y=65)
conectport.place(x=888,y=65)
baud_spin.place(x=853,y=96)
baud_label.place(x=788,y=95)
ReportWindow.place(x=20,y=35)
delay_label.place(x=788,y=120)
delay_spin.place(x=865,y=120)
Button_clear.place(x=788,y=245)
Button_Save.place(x=888,y=245)
bytesize_spin.place(x=845,y=150)
bytesize_label.place(x=788,y=150)
Timeout_label.place(x=882,y=150)
Timeout_spin.place(x=942,y=150)
stopbit_label.place(x=788,y=180)
stopbit_spin.place(x=843,y=180)
parity_menu.place(x=901,y=175)
Frametree.place(x=780,y=225)
Printtime.place(x=788,y=275)
Autoend.place(x=788,y=295)
Autodown.place(x=885,y=295)
Ghrapick.place(x=788,y=315)
Readstring.place(x=885,y=275)
scale.place(x=710,y=35)
Maxnum0.place(x=1017,y=35)
Minnum0.place(x=1017,y=55)
Avernum0.place(x=1017,y=75)
NameL0.place(x=1153,y=55)
ValL0.place(x=1153,y=35)
Maxnum1.place(x=1017,y=110)
Minnum1.place(x=1017,y=130)
Avernum1.place(x=1017,y=150)
NameL1.place(x=1153,y=130)
ValL1.place(x=1153,y=110)
Maxnum2.place(x=1017,y=190)
Minnum2.place(x=1017,y=210)
Avernum2.place(x=1017,y=230)
NameL2.place(x=1153,y=210)
ValL2.place(x=1153,y=190)
Maxnum3.place(x=1017,y=270)
Minnum3.place(x=1017,y=290)
Avernum3.place(x=1017,y=310)
NameL3.place(x=1153,y=290)
ValL3.place(x=1153,y=270)
Maxnum4.place(x=1017,y=350)
Minnum4.place(x=1017,y=370)
Avernum4.place(x=1017,y=390)
NameL4.place(x=1153,y=370)
ValL4.place(x=1153,y=350)
Maxcaracter_label.place(x=788,y=345)
Maxcaracter.place(x=890,y=345)
NLIB.place(x=936,y=342)
ENTRY.place(x=782,y=382)
SEND.place(x=951,y=379)
Framefor.place(x=1005,y=10)
CLADB.place(x=1193,y=400)
OpenPlottB.place(x=782,y=413)
try:
    window.iconbitmap("ICO.ico")
except:
    ReportWindow.insert(END,"ICONNOTFIND")





CLAD()
PortList()
ReportWindow.insert(END,"Welcome")
window.mainloop()
