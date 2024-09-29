Reads the voltage inputs on the Labjack T7-Pro on AIN2 to check the quality of the electrical signal. The max input is 10v so if you need to go above that consider using a voltage divider. If you break your unit, I warned you. 


====================================AIN2_Noise_Calc.py====================================
This will attempt to check how much noise is on the power signal. Its not a perfect solution without having a scope but its better then nothing. 
==================OPTIONS==================
* Enter the AIN channel (e.g., AIN2) [default: AIN2]:
* Enter the number of samples to capture [default: 1000]:
* Enter the sampling frequency in Hz (e.g., 100 for 100 Hz) [default: 100]:
* Enter the resolution index (0-12) [default: 0]:
  
==================Example==================
Configure your data acquisition:
Enter the AIN channel (e.g., AIN2) [default: AIN2]: 
Enter the number of samples to capture [default: 1000]: 2000
Enter the sampling frequency in Hz (e.g., 100 for 100 Hz) [default: 100]: 1000
Enter the resolution index (0-12) [default: 0]: 

Results:
Mean Value: 8.003120 V
Standard Deviation (Noise Level): 0.000856 V
RMS Noise: 0.000856 V
