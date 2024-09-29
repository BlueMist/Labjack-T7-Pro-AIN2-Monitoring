from labjack import ljm
import numpy as np
import time

def capture_data(channel="AIN2", num_samples=1000, frequency=100, resolution_index=0):
    """
    Captures data from a specified analog input channel on a LabJack device.

    Parameters:
    - channel: The AIN channel to read from (e.g., "AIN2").
    - num_samples: The number of samples to capture.
    - frequency: The sampling frequency in Hertz (samples per second).
    - resolution_index: The resolution index for the analog input channel.
    """
    
    # Calculate the sampling interval from the frequency
    interval = 1 / frequency

    # Open first found LabJack device
    handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier

    # Set the resolution index for the specified channel
    ljm.eWriteName(handle, f"{channel}_RESOLUTION_INDEX", resolution_index)

    # Array to store the readings
    readings = []

    try:
        start_time = time.time()  # Start timing loop

        for i in range(num_samples):
            # Read the value from the specified channel
            value = ljm.eReadName(handle, channel)
            readings.append(value)

            # Calculate time taken and adjust sleep for next loop
            elapsed_time = time.time() - start_time
            next_sample_time = (i + 1) * interval
            sleep_time = next_sample_time - elapsed_time
            if sleep_time > 0:
                time.sleep(sleep_time)

    finally:
        # Close the device
        ljm.close(handle)

    # Convert the list of readings to a NumPy array for statistical analysis
    readings_array = np.array(readings)

    # Calculate noise metrics
    mean_value = np.mean(readings_array)
    std_deviation = np.std(readings_array)
    rms_noise = np.sqrt(np.mean(np.square(readings_array - mean_value)))

    # Print the results
    print(f"\nResults:")
    print(f"Mean Value: {mean_value:.6f} V")
    print(f"Standard Deviation (Noise Level): {std_deviation:.6f} V")
    print(f"RMS Noise: {rms_noise:.6f} V")

    # Return the results if needed for further processing
    return mean_value, std_deviation, rms_noise

def get_user_input():
    """
    Function to gather user input for the data capture configuration.
    """
    print("Configure your data acquisition:")
    
    # Get user inputs with validation and defaults
    channel = input("Enter the AIN channel (e.g., AIN2) [default: AIN2]: ") or "AIN2"
    
    try:
        num_samples = int(input("Enter the number of samples to capture [default: 1000]: ") or 1000)
    except ValueError:
        num_samples = 1000
    
    try:
        frequency = float(input("Enter the sampling frequency in Hz (e.g., 100 for 100 Hz) [default: 100]: ") or 100)
    except ValueError:
        frequency = 100

    try:
        resolution_index = int(input("Enter the resolution index (0-12) [default: 0]: ") or 0)
    except ValueError:
        resolution_index = 0

    # Return the collected inputs
    return channel, num_samples, frequency, resolution_index

# Get user input for configuration
channel, num_samples, frequency, resolution_index = get_user_input()

# Run the data capture with user-defined settings
capture_data(channel=channel, num_samples=num_samples, frequency=frequency, resolution_index=resolution_index)
