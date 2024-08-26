import pyopencl as cl
import numpy as np
import time

def get_platforms_and_devices():
    platforms = cl.get_platforms()
    devices = [device for platform in platforms for device in platform.get_devices()]
    return platforms, devices

def get_device_info(device):
    device_name = device.name
    global_mem_size = device.global_mem_size
    max_compute_units = device.max_compute_units
    clock_frequency = device.max_clock_frequency
    
    return {
        "name": device_name,
        "global_mem_size": global_mem_size,
        "max_compute_units": max_compute_units,
        "clock_frequency": clock_frequency
    }

def monitor_gpu(devices, interval=1):
    try:
        while True:
            for i, device in enumerate(devices):
                device_info = get_device_info(device)
                
                print(f"Device {i}: {device_info['name']}")
                print(f"  Global Memory Size: {device_info['global_mem_size'] / (1024**2):.2f} MB")
                print(f"  Max Compute Units: {device_info['max_compute_units']}")
                print(f"  Clock Frequency: {device_info['clock_frequency']} MHz")
                print("-" * 40)
                
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("Stopping GPU load monitor...")

if __name__ == "__main__":
    platforms, devices = get_platforms_and_devices()
    if not devices:
        print("No OpenCL devices found.")
    else:
        monitor_gpu(devices, interval=5)  # Adjust the interval as needed