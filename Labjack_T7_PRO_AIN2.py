import csv
import os
import time
from labjack import ljm

# Function to generate a unique file name if the file already exists
def generate_unique_filename(base_filename, extension):
    counter = 1
    new_filename = f"{base_filename}{extension}"
    while os.path.exists(new_filename):
        new_filename = f"{base_filename}_{counter}{extension}"
        counter += 1
    return new_filename

# Ask for user input for sample rate in Hz and duration in seconds
sample_rate_hz = float(input("Enter the sampling rate in Hz (e.g., 1000 for 1000 samples per second): "))
duration = float(input("Enter the total duration in seconds before saving to file: "))

# Calculate the total number of samples to collect
num_samples = int(sample_rate_hz * duration)

# Open first found LabJack
handle = ljm.openS("T7", "ANY", "ANY")

try:
    # Configure the stream for AIN2
    scan_rate = sample_rate_hz
    scan_list_names = ["AIN2"]  # Stream AIN2
    scan_list = ljm.namesToAddresses(len(scan_list_names), scan_list_names)[0]

    # Start the stream with the specified scan rate
    actual_scan_rate = ljm.eStreamStart(handle, len(scan_list), len(scan_list), scan_list, scan_rate)

    print(f"Stream started with a scan rate of {actual_scan_rate} Hz.")

    readings = []
    total_samples_collected = 0

    # Record the start time for calculating elapsed time
    start_time = time.time()

    # Collect stream data until we have enough samples
    while total_samples_collected < num_samples:
        # Read a batch of samples from the stream
        ret = ljm.eStreamRead(handle)
        data = ret[0]  # Data array
        
        # Calculate elapsed time in ms since start
        elapsed_time_ms = int((time.time() - start_time) * 1000)

        # Append each sample with the current elapsed time
        for sample in data:
            readings.append([elapsed_time_ms, "AIN2", sample])
            total_samples_collected += 1
            
            # Stop if we have collected enough samples
            if total_samples_collected >= num_samples:
                break

    # Stop the stream
    ljm.eStreamStop(handle)

    # Get the directory where the Python script is running
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Base filename for the CSV file
    base_filename = os.path.join(script_dir, "voltage_readings")
    extension = ".csv"

    # Generate a unique filename if a file with the same name exists
    csv_file_path = generate_unique_filename(base_filename, extension)

    # Write the collected readings to the CSV file
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write a header
        writer.writerow(["Elapsed Time (ms)", "AIN Channel", "Voltage (V)"])
        # Write all the collected data
        writer.writerows(readings)

    # Print how many samples were saved
    print(f"Total number of samples saved: {len(readings)}")

    print(f"All voltage readings saved to {csv_file_path}")

finally:
    # Close the LabJack handle
    ljm.close(handle)
