# Serial-Printer
A professional program to receive data from the serial port (suitable for robots) + with serial plotter 

The program has been converted into an executable file for Windows with Tinker and is open source. Just run the PSP program in the Prog folder and work with it easily.
First, refresh the port and select the desired port
If the parameters below are correct, i.e. the port settings (such as Baud rate , Time Sleep , Byte Size , Stop Bit And...) click on the connection and wait for a few moments. If the port is correct, the connection is made and the data is displayed on the monitor.
Print settings
Print Time -> Displays the system time
Auto Scroll -> Scrolls down automatically
Read String -> receives the data in its real form
Auto Go End -> automatically goes to the end of the line
Data Analysis (ROLAN) -> this feature automatically if you have done the following:
 ardiuno code :
 Serial.print("A");
 Serial.print(A);
 Serial.print("B");
 Serial.print(B);
 Serial.print("C");
 Serial.print(C);
 Serial.print("AREF");
 Serial.print(V);
 Serial.println();
output cod :
A234B453C56732AREF6
It analyzes the data, writes its name, and displays the minimum, maximum, average, and moment of the number for you in the form of a list. This program can analyze data from 1 to 5 data.
Max char in Line -> specifies the maximum character in a line
RB -> reads in bits if enabled
The data sending part is not yet complete, but it is convenient to write whatever you want and send it as a string with the send button.
Open Plotter -> you can use it like Arduino Plotter but more advanced, actually it is a modified version of (https://github.com/taunoe/tauno-serial-plotter)
