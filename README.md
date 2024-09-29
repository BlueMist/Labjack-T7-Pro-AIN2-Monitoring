
# Labjack T7-Pro

Reads the voltage inputs on the Labjack T7-Pro on AIN2 to check the quality of the electrical signal. The max input is 10v so if you need to go above that consider using a voltage divider. If you break your unit, I warned you. 


AIN2_Noise_Calc.py

This will attempt to check how much noise is on the power signal. Its not a perfect solution without having a scope but its better then nothing. 

### OPTIONS
* Enter the AIN channel (e.g., AIN2) [default: AIN2]:
* Enter the number of samples to capture [default: 1000]:
* Enter the sampling frequency in Hz (e.g., 100 for 100 Hz) [default: 100]:
* Enter the resolution index (0-12) [default: 0]:
  
## Example
* Configure your data acquisition:
* Enter the AIN channel (e.g., AIN2) [default: AIN2]: 
* Enter the number of samples to capture [default: 1000]: 2000
* Enter the sampling frequency in Hz (e.g., 100 for 100 Hz) [default: 100]: 1000
* Enter the resolution index (0-12) [default: 0]: 

### Results:
* Mean Value: 8.003120 V
* Standard Deviation (Noise Level): 0.000856 V
* RMS Noise: 0.000856 V



## Installation

1. To run the script you will need to install Python. Python.org if you need to install it
2. pip install labjack-ljm

```bash
Make sure you the library is called from
from labjack import ljm
not 
import ljm 
```
    
## FAQ

#### Why?

Because I dont own a scope

#### Whats my input limit

±10V AC or DC. If you go outside that limit that you will break it. If you need to measure outside that consider making a voltage divider circuit. 

