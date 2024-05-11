A professional program to receive information from the serial port (suitable for robots) + has a serial plotter
## Screenshots
<img src="img/1.png" />
This program is converted to an executable file for Windows with Tinker and is open source. Just run the PSP program in the PSP folder and work with it easily.( Note that the plotter program has not been uploaded due to the large volume, and if you need it, you should use Tinker to convert the PTSP code in the code folder to an executable EXE file with the same name, and make sure that the two files V.TXT & PORT. TXT should be available in that location, also the executable file and two text files should be in the location of PSP.EXE)
## Exampel
<img src="img/2.png" />
## How Work
- First, refresh the port and select the desired port. If the following comments are correct, that is, the port rate (such as Baud rate, Time Sleep, Byte Size, Stop Bit, etc.), click on connect and wait for a few moments. do. . . If the port is correct, it is connected and can be displayed on the monitor.
- Print Time -> Print Display System Time ,Auto Scroll -> Auto scroll down ,Read String -> Gets the data in real form Auto ,Go End -> Automatically go to the end of
- of the data analysis line (ROLAN) -> This feature automatically if you do the following: ardiuno code :
```
Serial.print("A"); Serial.print(A); Serial.print("B"); Serial.print(B); Serial.print("C"); Serial.print(C); Serial.print("AREF"); Serial.print(V); Serial.println();
```
