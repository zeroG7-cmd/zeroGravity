# CPD Entry 1 – Drone Simulation Development (ROS2 & Gazebo)

**Date:** Tuesday 31st March 2026

---

## 1. Overview

This CPD entry documents the development of a simulated drone system using ROS2 and Gazebo. The focus was on building a functional simulation environment with integrated perception sensors (camera and LiDAR), enabling realistic data generation for future autonomous system development.

---

## 2. Objectives

- Set up a ROS2 workspace for drone development  
- Create a modular package structure for the drone system  
- Develop a URDF/Xacro model representing the drone  
- Integrate simulation using Gazebo  
- Add perception sensors (camera and LiDAR)  
- Visualise sensor data using RViz  
- Establish a TF (transform) system for coordinate consistency  

---

## 3. Work Completed

- Created ROS2 workspace (`shadow_ws`) and package (`shadow_drone`)  
- Defined robot structure using URDF/Xacro (`base_link`, `camera_link`, `lidar_link`)  
- Built a Gazebo simulation environment and successfully spawned the drone  
- Integrated a camera sensor publishing to `/camera/image_raw`  
- Integrated a LiDAR sensor publishing to `/scan`  
- Verified sensor outputs using ROS2 CLI tools  
- Configured RViz to visualise camera and LiDAR data  
- Implemented `robot_state_publisher` to generate a TF tree  
- Validated frame relationships using `tf2_tools`  

---

## 4. System Architecture

### Workspace Structure

```text
shadow_ws/
├── build/
├── install/
├── log/
└── src/
    └── shadow_drone/
        ├── launch/
        ├── urdf/
        ├── worlds/
        ├── CMakeLists.txt
        └── package.xml
```
---

### System Flow
```text
URDF → robot_state_publisher → TF
↓
Gazebo → Sensor Plugins
↓
ROS Topics (/camera, /scan)
↓
RViz Visualisation
```
---

## 5. Challenges & Solutions

### Package Not Recognised
- **Cause:** Workspace not sourced and missing configuration  
- **Solution:** Fixed `package.xml`, rebuilt workspace, sourced environment  

### Launch and Execution Errors
- **Cause:** Confusion between editing files and running launch files  
- **Solution:** Correct use of `ros2 launch` and proper file structure  

### URDF/Xacro Errors
- **Cause:** Invalid XML syntax and formatting issues  
- **Solution:** Corrected LiDAR section and validated using `xacro`  

### LiDAR Plugin Failure
- **Cause:** Incorrect plugin (`libgazebo_ros_laser.so`)  
- **Solution:** Replaced with `libgazebo_ros_ray_sensor.so`  

### Camera Not Displaying in RViz
- **Cause:** QoS mismatch (Reliable vs Best Effort)  
- **Solution:** Adjusted RViz QoS settings  

### Missing TF Data
- **Cause:** No transform tree for robot links  
- **Solution:** Implemented `robot_state_publisher`  

### LiDAR Showing Infinite Values
- **Cause:** No objects in simulation environment  
- **Solution:** Confirmed expected behaviour and added objects for testing  

---

## 6. Key Learning

- ROS2 systems rely heavily on correct configuration and environment setup  
- Understanding system architecture is more important than individual commands  
- TF (transform frames) is critical for spatial awareness in robotics  
- Simulation allows safe testing before real-world deployment  
- Debugging involves identifying which system layer is failing  

---

## 7. Reflection

This phase marked a significant breakthrough in understanding ROS2 and robotic systems integration. Initially, the system appeared complex and fragmented, but through debugging and iterative development, a clear architecture emerged. I successfully built a working simulation pipeline, including perception sensors and coordinate frame management, forming a strong foundation for autonomous drone development.

---

## 8. Next Steps

- Improve drone model realism (quadcopter structure)  
- Introduce more complex simulation environments  
- Process LiDAR data for obstacle detection  
- Implement basic control behaviours  
- Progress toward SLAM and autonomous navigation  
- Transition to real hardware integration (RPLIDAR and camera)
