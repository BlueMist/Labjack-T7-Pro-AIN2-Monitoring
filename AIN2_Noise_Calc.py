from labjack import ljm
import numpy as np
import time

# Open first found LabJack device
handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier

# Configure the AIN2 input channel
channel = "AIN2"
num_samples = 1000  # Number of samples to take for noise analysis
interval = 0.01  # Sampling interval in seconds

# Array to store the readings
readings = []

try:
    for i in range(num_samples):
        # Read AIN2
        value = ljm.eReadName(handle, channel)
        readings.append(value)
        
        # Delay between readings
        time.sleep(interval)

finally:
    # Close the device
    ljm.close(handle)

# Convert the list of readings to a NumPy array for statistical analysis
readings_array = np.array(readings)

# Calculate noise metrics
mean_value = np.mean(readings_array)
std_deviation = np.std(readings_array)
rms_noise = np.sqrt(np.mean(np.square(readings_array - mean_value)))

print(f"Mean Value: {mean_value:.6f} V")
print(f"Standard Deviation (Noise Level): {std_deviation:.6f} V")
print(f"RMS Noise: {rms_noise:.6f} V")
