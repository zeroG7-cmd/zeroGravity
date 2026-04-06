# CPD Entry 2 – Drone Onboard Systems Development & Data Pipeline Integration

##  Date:
[5th Sunday March 2026]

---

##  Context

Following **CPD Entry 1 – Drone Simulation Development (ROS2 & Gazebo)**, I progressed from simulation into setting up the onboard computing environment on the Raspberry Pi.

This marked the transition from a simulated system to a **real-world executable system**.

---

##  Key Realisation

Today was a turning point in my project.

Since starting this project in 2020, I had been working on different parts (hardware, ROS, sensors) without fully understanding how they connected.

Today, it became clear that:

> The drone is not just a collection of components — it is a **connected system with a data pipeline**.

---

##  System Pipeline Understanding

I now understand my system as a structured pipeline:
'''text
Desktop (Development & Simulation)
↓
Raspberry Pi (Onboard Execution)
↓
Runtime Environment (Data Output & Logging)
↓
R&D Repository (Analysis & Iteration)
↓
ZeroGravity (Presentation & System Narrative)
'''
This helped me see how each part of my project contributes to a continuous workflow.

---

##  Understanding of Roles

###  Desktop (Development Environment)
- Acts as the main workspace for coding and simulation  
- Hosts the `shadow_drone_ros` repository  
- Used to develop and test system logic  

---

###  Raspberry Pi (Onboard Computer)
- Executes ROS nodes on the drone  
- Interfaces with sensors (LiDAR, camera)  
- Collects real-world data  

---

###  Runtime Environment (`shadow_runtime`)
- Stores sensor outputs, logs, and recordings  
- Represents the real-world behaviour of the system  

---

###  R&D Repository (`shadow_drone_rnd`)
- Used for analysing experimental data  
- Supports iterative development and improvement  

---

##  Practical Progress

- Set up SSH access to Raspberry Pi  
- Built onboard workspace structure:
'''text
~/shadow_ws
~/shadow_runtime
'''
- Installed ROS tools (`colcon`, `rosdep`)  
- Successfully built first ROS package (`rplidar_ros`)  
- Began hardware integration (LiDAR), identifying power and connection issues  

---

##  Challenges

- LiDAR not detected due to power/cable issues  
- Raspberry Pi undervoltage warnings  
- Inconsistent USB communication  

---

##  Key Technical Insight

> Power delivery is a critical part of system design.

Even with correct software, hardware will not function without stable and sufficient power.

---

##  Reflection on Learning Journey

Since starting this project in 2020, I was largely working without a clear system structure, relying on tutorials and trial-and-error.

Today, I recognised that:

- I was not lacking effort, but **lacking system-level understanding**  
- Tools like GitHub are not just for storing code, but for structuring and organising the entire project  
- Understanding how data flows through the system is more important than individual components  

---

## Shift in Thinking

I moved from:

> “Trying to make parts work individually”

to:

> “Designing how the entire system connects and operates”

---

## Next Steps

- Resolve LiDAR hardware issue (power and cable validation)  
- Confirm device detection (`/dev/ttyUSB0`)  
- Launch LiDAR ROS node and verify `/scan` topic  
- Begin recording real sensor data into runtime environment  
- Introduce camera testing and integration  

---

## Closing Reflection

After working on this project since 2020, this is the first time the system feels structured and connected.

The project is no longer just a collection of experiments — it is becoming a **coherent, functioning system**.

---

## Closing Thought

> The system is starting to come alive — not because new components were added, but because the **connections between them are now understood**.
