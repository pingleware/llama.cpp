import pyopencl as cl

def get_opencl_info():
    """Fetch OpenCL platform and device information."""
    platforms = cl.get_platforms()
    for platform in platforms:
        print(f"Platform: {platform.name}")
        print(f"Vendor: {platform.vendor}")
        print(f"Version: {platform.version}")

        devices = platform.get_devices()
        for device in devices:
            print(f"\nDevice: {device.name}")
            print(f"Type: {cl.device_type.to_string(device.type)}")
            print(f"Max Compute Units: {device.max_compute_units}")
            print(f"Global Memory Size: {device.global_mem_size / (1024 ** 2)} MB")
            print(f"Local Memory Size: {device.local_mem_size / 1024} KB")
            print(f"Max Clock Frequency: {device.max_clock_frequency} MHz")
            print(f"Max Memory Allocation: {device.max_mem_alloc_size / (1024 ** 2)} MB")
            print(f"Global Memory Cache Size: {device.global_mem_cache_size / 1024} KB")
            print(f"OpenCL Version: {device.version}")
            print(f"Driver Version: {device.driver_version}")
            print(f"Available: {device.available}")
            print(f"Extensions: {device.extensions}")

if __name__ == "__main__":
    get_opencl_info()

################################################################
# Expected Output
# ---------------
#
# Platform: NVIDIA CUDA
# Vendor: NVIDIA Corporation
# Version: OpenCL 1.2 CUDA 9.1.84
# 
# Device: GeForce GT 730
# Type: ALL | GPU
# Max Compute Units: 2
# Global Memory Size: 4096.0 MB
# Local Memory Size: 48.0 KB
# Max Clock Frequency: 1400 MHz
# Max Memory Allocation: 1024.0 MB
# Global Memory Cache Size: 32.0 KB
# OpenCL Version: OpenCL 1.1 CUDA
# Driver Version: 391.35
# Available: 1
# Extensions: cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics 
#             cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics 
#             cl_khr_fp64 cl_khr_byte_addressable_store cl_khr_icd cl_khr_gl_sharing 
#             cl_nv_compiler_options cl_nv_device_attribute_query cl_nv_pragma_unroll 
#             cl_nv_d3d10_sharing cl_khr_d3d10_sharing cl_nv_d3d11_sharing cl_nv_copy_opts 
#             cl_nv_create_buffer
################################################################
