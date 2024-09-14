# Intel GPU Support
The chuwi.com HEROBOX has a GPU but to get recognized under WSL2, follow these steps from https://www.intel.com/content/www/us/en/docs/oneapi/installation-guide-linux/2023-0/configure-wsl-2-for-gpu-workflows.html

but in this order,

## Ubuntu Jammy

### Step 1: Add package repository

Install the repositories.intel.com/graphics package repository by executing the following command in your WSL 2 console:

```
sudo apt-get install -y gpg-agent wget
wget -qO - https://repositories.intel.com/graphics/intel-graphics.key |
  sudo gpg --dearmor --output /usr/share/keyrings/intel-graphics.gpg
echo 'deb [arch=amd64,i386 signed-by=/usr/share/keyrings/intel-graphics.gpg] https://repositories.intel.com/graphics/ubuntu jammy arc' | \
  sudo tee  /etc/apt/sources.list.d/intel.gpu.jammy.list
```

### Step 2: Install support Steam games, install i386 packages:
```
sudo dpkg --add-architecture i386
sudo apt-get update

sudo apt-get install  -y \
    udev mesa-va-drivers:i386 mesa-common-dev:i386 mesa-vulkan-drivers:i386 \
    libd3dadapter9-mesa-dev:i386 libegl1-mesa:i386  libegl1-mesa-dev:i386   \
    libgbm-dev:i386 libgl1-mesa-glx:i386 libgl1-mesa-dev:i386   \
    libgles2-mesa:i386 libgles2-mesa-dev:i386 libosmesa6:i386   \
    libosmesa6-dev:i386 libwayland-egl1-mesa:i386  libxatracker2:i386 \
    libxatracker-dev:i386 mesa-vdpau-drivers:i386  libva-x11-2:i386
```

### Step 3: Install runtime and development (optional) packages
When I did this step before the step above, clinfo would not recognized the GPU.

Install GPU software packages with the following command:

```
sudo apt-get install -y \
  intel-opencl-icd intel-level-zero-gpu level-zero \
  intel-media-va-driver-non-free libmfx1 libmfxgen1 libvpl2 \
  libegl-mesa0 libegl1-mesa libegl1-mesa-dev libgbm1 libgl1-mesa-dev libgl1-mesa-dri \
  libglapi-mesa libgles2-mesa-dev libglx-mesa0 libigdgmm12 libxatracker2 mesa-va-drivers \
  mesa-vdpau-drivers mesa-vulkan-drivers va-driver-all
```

OPTIONAL: If you plan to perform development tasks, you need to install the following optional development packages to make sure that oneAPI tools function correctly:

```
sudo apt-get install -y \
  libigc-dev \
  intel-igc-cm \
  libigdfcl-dev \
  libigfxcmrt-dev \
  level-zero-dev
```

### Step 4: Configure permissions

To access GPU capabilities, the user needs to have correct permissions on system. Use the following command to list the group assigned ownership of the render nodes and list the groups the active user is a member of:

```
stat -c "%G" /dev/dri/render*
groups ${USER}
```

If a group is listed for the render node that is not listed for the user, add the user to the group using gpasswd:

```
sudo gpasswd -a ${USER} render
newgrp render
```

### Step 5: Verify installation

Verify Computing drivers installation:

```
sudo apt-get install clinfo
clinfo
```

results

```
Number of platforms                               1
  Platform Name                                   Intel(R) OpenCL Graphics
  Platform Vendor                                 Intel(R) Corporation
  Platform Version                                OpenCL 3.0 
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_byte_addressable_store cl_khr_device_uuid cl_khr_fp16 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_icd cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_intel_command_queue_families cl_intel_subgroups cl_intel_required_subgroup_size cl_intel_subgroups_short cl_khr_spir cl_intel_accelerator cl_intel_driver_diagnostics cl_khr_priority_hints cl_khr_throttle_hints cl_khr_create_command_queue cl_intel_subgroups_char cl_intel_subgroups_long cl_khr_il_program cl_intel_mem_force_host_memory cl_khr_subgroup_extended_types cl_khr_subgroup_non_uniform_vote cl_khr_subgroup_ballot cl_khr_subgroup_non_uniform_arithmetic cl_khr_subgroup_shuffle cl_khr_subgroup_shuffle_relative cl_khr_subgroup_clustered_reduce cl_intel_device_attribute_query cl_khr_suggested_local_work_size cl_intel_split_work_group_barrier cl_intel_spirv_media_block_io cl_intel_spirv_subgroups cl_khr_spirv_no_integer_wrap_decoration cl_intel_unified_shared_memory cl_khr_mipmap_image cl_khr_mipmap_image_writes cl_ext_float_atomics cl_intel_planar_yuv cl_intel_packed_yuv cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_image2d_from_buffer cl_khr_depth_images cl_khr_3d_image_writes cl_intel_media_block_io cl_intel_subgroup_local_block_io cl_khr_integer_dot_product cl_khr_gl_sharing cl_khr_gl_depth_images cl_khr_gl_event cl_khr_gl_msaa_sharing cl_intel_va_api_media_sharing cl_intel_sharing_format_query cl_khr_pci_bus_info
  Platform Extensions with Version                cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_device_uuid                                               0x400000 (1.0.0)
                                                  cl_khr_fp16                                                      0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_icd                                                       0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_intel_command_queue_families                                  0x400000 (1.0.0)
                                                  cl_intel_subgroups                                               0x400000 (1.0.0)
                                                  cl_intel_required_subgroup_size                                  0x400000 (1.0.0)
                                                  cl_intel_subgroups_short                                         0x400000 (1.0.0)
                                                  cl_khr_spir                                                      0x400000 (1.0.0)
                                                  cl_intel_accelerator                                             0x400000 (1.0.0)
                                                  cl_intel_driver_diagnostics                                      0x400000 (1.0.0)
                                                  cl_khr_priority_hints                                            0x400000 (1.0.0)
                                                  cl_khr_throttle_hints                                            0x400000 (1.0.0)
                                                  cl_khr_create_command_queue                                      0x400000 (1.0.0)
                                                  cl_intel_subgroups_char                                          0x400000 (1.0.0)
                                                  cl_intel_subgroups_long                                          0x400000 (1.0.0)
                                                  cl_khr_il_program                                                0x400000 (1.0.0)
                                                  cl_intel_mem_force_host_memory                                   0x400000 (1.0.0)
                                                  cl_khr_subgroup_extended_types                                   0x400000 (1.0.0)
                                                  cl_khr_subgroup_non_uniform_vote                                 0x400000 (1.0.0)
                                                  cl_khr_subgroup_ballot                                           0x400000 (1.0.0)
                                                  cl_khr_subgroup_non_uniform_arithmetic                           0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle                                          0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle_relative                                 0x400000 (1.0.0)
                                                  cl_khr_subgroup_clustered_reduce                                 0x400000 (1.0.0)
                                                  cl_intel_device_attribute_query                                  0x400000 (1.0.0)
                                                  cl_khr_suggested_local_work_size                                 0x400000 (1.0.0)
                                                  cl_intel_split_work_group_barrier                                0x400000 (1.0.0)
                                                  cl_intel_spirv_media_block_io                                    0x400000 (1.0.0)
                                                  cl_intel_spirv_subgroups                                         0x400000 (1.0.0)
                                                  cl_khr_spirv_no_integer_wrap_decoration                          0x400000 (1.0.0)
                                                  cl_intel_unified_shared_memory                                   0x400000 (1.0.0)
                                                  cl_khr_mipmap_image                                              0x400000 (1.0.0)
                                                  cl_khr_mipmap_image_writes                                       0x400000 (1.0.0)
                                                  cl_ext_float_atomics                                             0x400000 (1.0.0)
                                                  cl_intel_planar_yuv                                              0x400000 (1.0.0)
                                                  cl_intel_packed_yuv                                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_image2d_from_buffer                                       0x400000 (1.0.0)
                                                  cl_khr_depth_images                                              0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
                                                  cl_intel_media_block_io                                          0x400000 (1.0.0)
                                                  cl_intel_subgroup_local_block_io                                 0x400000 (1.0.0)
                                                  cl_khr_integer_dot_product                                       0x800000 (2.0.0)
                                                  cl_khr_gl_sharing                                                0x400000 (1.0.0)
                                                  cl_khr_gl_depth_images                                           0x400000 (1.0.0)
                                                  cl_khr_gl_event                                                  0x400000 (1.0.0)
                                                  cl_khr_gl_msaa_sharing                                           0x400000 (1.0.0)
                                                  cl_intel_va_api_media_sharing                                    0x400000 (1.0.0)
                                                  cl_intel_sharing_format_query                                    0x400000 (1.0.0)
                                                  cl_khr_pci_bus_info                                              0x400000 (1.0.0)
  Platform Numeric Version                        0xc00000 (3.0.0)
  Platform Extensions function suffix             INTEL
  Platform Host timer resolution                  1ns

  Platform Name                                   Intel(R) OpenCL Graphics
Number of devices                                 1
  Device Name                                     Intel(R) Graphics [0x46d1]
  Device Vendor                                   Intel(R) Corporation
  Device Vendor ID                                0x8086
  Device Version                                  OpenCL 3.0 NEO
  Device UUID                                     8680d146-0000-0000-0002-000000000000
  Driver UUID                                     32332e31-372e-3236-3234-312e33330000
  Valid Device LUID                               No
  Device LUID                                     e018-4dc3fd7f0000
  Device Node Mask                                0
  Device Numeric Version                          0xc00000 (3.0.0)
  Driver Version                                  23.17.26241.33
  Device OpenCL C Version                         OpenCL C 1.2
  Device OpenCL C all versions                    OpenCL C                                                         0x400000 (1.0.0)
                                                  OpenCL C                                                         0x401000 (1.1.0)
                                                  OpenCL C                                                         0x402000 (1.2.0)
                                                  OpenCL C                                                         0xc00000 (3.0.0)
  Device OpenCL C features                        __opencl_c_int64                                                 0xc00000 (3.0.0)
                                                  __opencl_c_3d_image_writes                                       0xc00000 (3.0.0)
                                                  __opencl_c_images                                                0xc00000 (3.0.0)
                                                  __opencl_c_read_write_images                                     0xc00000 (3.0.0)
                                                  __opencl_c_atomic_order_acq_rel                                  0xc00000 (3.0.0)
                                                  __opencl_c_atomic_order_seq_cst                                  0xc00000 (3.0.0)
                                                  __opencl_c_atomic_scope_all_devices                              0xc00000 (3.0.0)
                                                  __opencl_c_atomic_scope_device                                   0xc00000 (3.0.0)
                                                  __opencl_c_generic_address_space                                 0xc00000 (3.0.0)
                                                  __opencl_c_program_scope_global_variables                        0xc00000 (3.0.0)
                                                  __opencl_c_work_group_collective_functions                       0xc00000 (3.0.0)
                                                  __opencl_c_subgroups                                             0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp32_global_atomic_add                            0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp32_local_atomic_add                             0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp32_global_atomic_min_max                        0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp32_local_atomic_min_max                         0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp16_global_atomic_load_store                     0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp16_local_atomic_load_store                      0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp16_global_atomic_min_max                        0xc00000 (3.0.0)
                                                  __opencl_c_ext_fp16_local_atomic_min_max                         0xc00000 (3.0.0)
                                                  __opencl_c_integer_dot_product_input_4x8bit                      0xc00000 (3.0.0)
                                                  __opencl_c_integer_dot_product_input_4x8bit_packed               0xc00000 (3.0.0)
  Latest comfornace test passed                   v2022-04-22-00
  Device Type                                     GPU
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               24
  Max clock frequency                             750MHz
  Device Partition                                (core)
    Max number of sub-devices                     0
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             512x512x512
  Max work group size                             512
  Preferred work group size multiple (device)     64
  Preferred work group size multiple (kernel)     64
  Max sub-groups per work group                   64
  Sub-group sizes (Intel)                         8, 16, 32
  Preferred / native vector sizes
    char                                                16 / 16
    short                                                8 / 8
    int                                                  4 / 4
    long                                                 1 / 1
    half                                                 8 / 8        (cl_khr_fp16)
    float                                                1 / 1
    double                                               0 / 0        (n/a)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  No
  Double-precision Floating-point support         (n/a)
  Address bits                                    64, Little-Endian
  Global memory size                              3327766528 (3.099GiB)
  Error Correction support                        No
  Max memory allocation                           1073741824 (1024MiB)
  Unified memory for Host and Device              Yes
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   No
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics
    SVM                                           64 bytes
    Global                                        64 bytes
    Local                                         64 bytes
  Atomic memory capabilities                      relaxed, acquire/release, sequentially-consistent, work-group scope, device scope, all-devices scope
  Atomic fence capabilities                       relaxed, acquire/release, sequentially-consistent, work-item scope, work-group scope, device scope, all-devices scope
  Max size for global variable                    65536 (64KiB)
  Preferred total size of global vars             1073741824 (1024MiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        1966080 (1.875MiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             16
    Max size for 1D images from buffer            67108864 pixels
    Max 1D or 2D image array size                 2048 images
    Base address alignment for 2D image buffers   4 bytes
    Pitch alignment for 2D image buffers          4 pixels
    Max 2D image size                             16384x16384 pixels
    Max planar YUV image size                     16384x16352 pixels
    Max 3D image size                             2048x2048x2048 pixels
    Max number of read image args                 128
    Max number of write image args                128
    Max number of read/write image args           128
  Pipe support                                    No
  Max number of pipe args                         0
  Max active pipe reservations                    0
  Max pipe packet size                            0
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Max number of constant args                     8
  Max constant buffer size                        1073741824 (1024MiB)
  Generic address space support                   Yes
  Max size of kernel argument                     2048 (2KiB)
  Queue properties (on host)
    Out-of-order execution                        Yes
    Profiling                                     Yes
  Device enqueue capabilities                     (n/a)
  Queue properties (on device)
    Out-of-order execution                        No
    Profiling                                     No
    Preferred size                                0
    Max size                                      0
  Max queues on device                            0
  Max events on device                            0
  Prefer user sync for interop                    Yes
  Profiling timer resolution                      52ns
  Execution capabilities
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Non-uniform work-groups                       Yes
    Work-group collective functions               Yes
    Sub-group independent forward progress        No
    IL version                                    SPIR-V_1.2
    ILs with version                              SPIR-V                                                           0x402000 (1.2.0)
    SPIR versions                                 1.2
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Built-in kernels with version                   (n/a)
  Device Extensions                               cl_khr_byte_addressable_store cl_khr_device_uuid cl_khr_fp16 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_icd cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_intel_command_queue_families cl_intel_subgroups cl_intel_required_subgroup_size cl_intel_subgroups_short cl_khr_spir cl_intel_accelerator cl_intel_driver_diagnostics cl_khr_priority_hints cl_khr_throttle_hints cl_khr_create_command_queue cl_intel_subgroups_char cl_intel_subgroups_long cl_khr_il_program cl_intel_mem_force_host_memory cl_khr_subgroup_extended_types cl_khr_subgroup_non_uniform_vote cl_khr_subgroup_ballot cl_khr_subgroup_non_uniform_arithmetic cl_khr_subgroup_shuffle cl_khr_subgroup_shuffle_relative cl_khr_subgroup_clustered_reduce cl_intel_device_attribute_query cl_khr_suggested_local_work_size cl_intel_split_work_group_barrier cl_intel_spirv_media_block_io cl_intel_spirv_subgroups cl_khr_spirv_no_integer_wrap_decoration cl_intel_unified_shared_memory cl_khr_mipmap_image cl_khr_mipmap_image_writes cl_ext_float_atomics cl_intel_planar_yuv cl_intel_packed_yuv cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_image2d_from_buffer cl_khr_depth_images cl_khr_3d_image_writes cl_intel_media_block_io cl_intel_subgroup_local_block_io cl_khr_integer_dot_product cl_khr_gl_sharing cl_khr_gl_depth_images cl_khr_gl_event cl_khr_gl_msaa_sharing cl_intel_va_api_media_sharing cl_intel_sharing_format_query cl_khr_pci_bus_info
  Device Extensions with Version                  cl_khr_byte_addressable_store                                    0x400000 (1.0.0)
                                                  cl_khr_device_uuid                                               0x400000 (1.0.0)
                                                  cl_khr_fp16                                                      0x400000 (1.0.0)
                                                  cl_khr_global_int32_base_atomics                                 0x400000 (1.0.0)
                                                  cl_khr_global_int32_extended_atomics                             0x400000 (1.0.0)
                                                  cl_khr_icd                                                       0x400000 (1.0.0)
                                                  cl_khr_local_int32_base_atomics                                  0x400000 (1.0.0)
                                                  cl_khr_local_int32_extended_atomics                              0x400000 (1.0.0)
                                                  cl_intel_command_queue_families                                  0x400000 (1.0.0)
                                                  cl_intel_subgroups                                               0x400000 (1.0.0)
                                                  cl_intel_required_subgroup_size                                  0x400000 (1.0.0)
                                                  cl_intel_subgroups_short                                         0x400000 (1.0.0)
                                                  cl_khr_spir                                                      0x400000 (1.0.0)
                                                  cl_intel_accelerator                                             0x400000 (1.0.0)
                                                  cl_intel_driver_diagnostics                                      0x400000 (1.0.0)
                                                  cl_khr_priority_hints                                            0x400000 (1.0.0)
                                                  cl_khr_throttle_hints                                            0x400000 (1.0.0)
                                                  cl_khr_create_command_queue                                      0x400000 (1.0.0)
                                                  cl_intel_subgroups_char                                          0x400000 (1.0.0)
                                                  cl_intel_subgroups_long                                          0x400000 (1.0.0)
                                                  cl_khr_il_program                                                0x400000 (1.0.0)
                                                  cl_intel_mem_force_host_memory                                   0x400000 (1.0.0)
                                                  cl_khr_subgroup_extended_types                                   0x400000 (1.0.0)
                                                  cl_khr_subgroup_non_uniform_vote                                 0x400000 (1.0.0)
                                                  cl_khr_subgroup_ballot                                           0x400000 (1.0.0)
                                                  cl_khr_subgroup_non_uniform_arithmetic                           0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle                                          0x400000 (1.0.0)
                                                  cl_khr_subgroup_shuffle_relative                                 0x400000 (1.0.0)
                                                  cl_khr_subgroup_clustered_reduce                                 0x400000 (1.0.0)
                                                  cl_intel_device_attribute_query                                  0x400000 (1.0.0)
                                                  cl_khr_suggested_local_work_size                                 0x400000 (1.0.0)
                                                  cl_intel_split_work_group_barrier                                0x400000 (1.0.0)
                                                  cl_intel_spirv_media_block_io                                    0x400000 (1.0.0)
                                                  cl_intel_spirv_subgroups                                         0x400000 (1.0.0)
                                                  cl_khr_spirv_no_integer_wrap_decoration                          0x400000 (1.0.0)
                                                  cl_intel_unified_shared_memory                                   0x400000 (1.0.0)
                                                  cl_khr_mipmap_image                                              0x400000 (1.0.0)
                                                  cl_khr_mipmap_image_writes                                       0x400000 (1.0.0)
                                                  cl_ext_float_atomics                                             0x400000 (1.0.0)
                                                  cl_intel_planar_yuv                                              0x400000 (1.0.0)
                                                  cl_intel_packed_yuv                                              0x400000 (1.0.0)
                                                  cl_khr_int64_base_atomics                                        0x400000 (1.0.0)
                                                  cl_khr_int64_extended_atomics                                    0x400000 (1.0.0)
                                                  cl_khr_image2d_from_buffer                                       0x400000 (1.0.0)
                                                  cl_khr_depth_images                                              0x400000 (1.0.0)
                                                  cl_khr_3d_image_writes                                           0x400000 (1.0.0)
                                                  cl_intel_media_block_io                                          0x400000 (1.0.0)
                                                  cl_intel_subgroup_local_block_io                                 0x400000 (1.0.0)
                                                  cl_khr_integer_dot_product                                       0x800000 (2.0.0)
                                                  cl_khr_gl_sharing                                                0x400000 (1.0.0)
                                                  cl_khr_gl_depth_images                                           0x400000 (1.0.0)
                                                  cl_khr_gl_event                                                  0x400000 (1.0.0)
                                                  cl_khr_gl_msaa_sharing                                           0x400000 (1.0.0)
                                                  cl_intel_va_api_media_sharing                                    0x400000 (1.0.0)
                                                  cl_intel_sharing_format_query                                    0x400000 (1.0.0)
                                                  cl_khr_pci_bus_info                                              0x400000 (1.0.0)

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  Intel(R) OpenCL Graphics
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [INTEL]
  clCreateContext(NULL, ...) [default]            Success [INTEL]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 Intel(R) OpenCL Graphics
    Device Name                                   Intel(R) Graphics [0x46d1]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 Intel(R) OpenCL Graphics
    Device Name                                   Intel(R) Graphics [0x46d1]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 Intel(R) OpenCL Graphics
    Device Name                                   Intel(R) Graphics [0x46d1]

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.14
  ICD loader Profile                              OpenCL 3.0
```

## Run a Sample GPU Program

1. Install Python and PIP

    sudo apt install python3 python3-pip python3.10-venv -y

2. Create a python virtual environment

    python -m venv ./venv

3. Activate the python virtual environment

    source venv/bin/activate

4. Install TensorFlow with GPU support:

    pip install tensorflow

5. Test GPU access:

    import tensorflow as tf
    print(tf.config.list_physical_devices('GPU'))

6. Deactivate the python virtual environment

    deactivate


llama-baby-llama.exe
llama-batched.exe
llama-batched-bench.exe
llama-bench.exe
llama-bench-matmult.exe
llama-cli.exe
llama-convert-llama2c-to-ggml.exe
llama-cvector-generator.exe
llama-embedding.exe
llama-eval-callback.exe
llama-export-lora.exe
llama-gbnf-validator.exe
llama-gguf.exe
llama-gguf-hash.exe
llama-gguf-split.exe
llama-gritlm.exe
llama-imatrix.exe
llama-infill.exe
llama-llava-cli.exe
llama-lookahead.exe
llama-lookup.exe
llama-lookup-create.exe
llama-lookup-merge.exe
llama-lookup-stats.exe
llama-minicpmv-cli.exe
llama-parallel.exe
llama-passkey.exe
llama-perplexity.exe
llama-q8dot.exe
llama-quantize.exe
llama-quantize-stats.exe
llama-retrieval.exe
llama-save-load-state.exe
llama-server.exe
llama-simple.exe
llama-speculative.exe
llama-tokenize.exe
llama-vdot.exe