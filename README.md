A professional program to receive information from the serial port (suitable for robots) + has a serial plotter
## Screenshots
<img src="https://github.com/PAB-FA/Serial-Printer/blob/main/Img/1.png" />
<img src="https://github.com/PAB-FA/Serial-Printer/blob/main/Img/3.png" />

## Demo
You can download the latest beta version for your Windows from [here](https://github.com/PAB-FA/Serial-Printer/releases/tag/V0.2)



## Exampel

This app is made with Tinker. You can convert the PSP and PTSP that are in the code folder into an executable file and place it in the same folder as in the image below to make it work properly.

<img src="https://github.com/PAB-FA/Serial-Printer/blob/main/Img/2.png" />

-These libraries are prerequisites
```terminal
pip install tkinter
pip install serial
pip install PyQt5 
```

## How Work



https://github.com/PAB-FA/Serial-Printer/assets/169495280/384f4b22-d50c-4318-8242-6b833e0cb67b



- First, refresh the port and select the desired port. If the following comments are correct, that is, the port rate (such as Baud rate, Time Sleep, Byte Size, Stop Bit, etc.), click on connect and wait for a few moments. do. . . If the port is correct, it is connected and can be displayed on the monitor.
- Print Time -> Print Display System Time ,Auto Scroll -> Auto scroll down ,Read String -> Gets the data in real form Auto ,Go End -> Automatically go to the end 
- of the data analysis line (ROLAN) -> This feature automatically if you do the following Code:
  
```ino
//Ardiuno Code:
int A = 234; #And...
Serial.print("A");
Serial.print(A);
Serial.print("B");
Serial.print(B);
Serial.print("C");
Serial.print(C);
Serial.print("AREF");
Serial.print(V);
Serial.println();

// Output Code :
A234B453C56732AREF6
```
Analyzes the data, writes its name and displays the less than, value, value and moment of the number in a list format. This program can give and analyze data from 1 to 5.
- Max char in Line -> machine specifies character on a line ,RB -> reads in bit if enabled
- The sent part is not complete yet, but it's convenient to write whatever you can and make it as Do it. Submit a string with a button.
-  Open plotter -> you can use it like arduino plotter but more advanced, actually a modified version of [tauno-serial-plotter](https://github.com/taunoe/tauno-serial-plotter).


## CREDITS
Special Thanks to 
- [Pouya Aryani](https://github.com/PAB-FA)
- [Tauno](https://github.com/taunoe)

