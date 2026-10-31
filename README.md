# TurtleBot3 Autonomous Navigation (ROS 2 Jazzy + Gazebo Harmonic + Nav2)

This repository documents a reproducible TurtleBot3 simulation using the Nav2
quickstart supplied by `nav2_bringup`. It is intended for Ubuntu 24.04 + ROS 2 Jazzy.

## What this project demonstrates

- TurtleBot3 simulation in Gazebo
- Nav2 navigation to a goal pose using RViz2
- Localization and TF inspection
- LiDAR-based obstacle sensing and costmap-based navigation

> Important: This repository does not claim that a robot has been trained with
> machine learning. Nav2 is a configured navigation stack, not an ML training task.
> Only mark obstacle avoidance as demonstrated after testing it in your running world.

## Prerequisites

- Ubuntu 24.04 (native installation or WSL2 with working WSLg graphics)
- ROS 2 Jazzy Desktop
- Gazebo Harmonic integration
- Nav2 packages

Install packages:

```bash
sudo apt update
sudo apt install -y ros-jazzy-ros-gz ros-jazzy-navigation2 ros-jazzy-nav2-bringup
sudo apt install -y 'ros-jazzy-nav2-minimal-tb*'
```

## Run the reference simulation

In a terminal:

```bash
source /opt/ros/jazzy/setup.bash
ros2 launch nav2_bringup tb3_simulation_launch.py headless:=False
```

The launch file starts the reference TurtleBot3 simulation and Nav2 setup.
In RViz2, initialize the robot with **2D Pose Estimate** if needed, then use
**Nav2 Goal** to send a destination.

## Run using this repository's launch wrapper

From the repository root:

```bash
source /opt/ros/jazzy/setup.bash
python3 launch/navigation.launch.py
```

The wrapper includes the same official Nav2 quickstart launch. It does not
replace the upstream robot, world, map, or Nav2 configuration.

## Useful diagnostics

Open a second terminal and source ROS:

```bash
source /opt/ros/jazzy/setup.bash
ros2 node list
ros2 action list
ros2 topic list
ros2 topic echo /scan --once
ros2 topic echo /odom --once
ros2 run tf2_ros tf2_echo map base_link
```

The `/navigate_to_pose` action should be available when Nav2 is running.
The `map -> base_link` transform appears only after the map/localization and
robot TF chain are correctly active. If it is missing, inspect `/map`, `/tf`,
AMCL lifecycle state, and the terminal that launched Nav2.

## Maps

`maps/map.yaml` is a template. Generate a real map from a running SLAM session
or use the map supplied by your chosen simulation. Do not submit an empty or
invented map as if it were measured.

For a SLAM Toolbox mapping session, after mapping is complete:

```bash
ros2 run nav2_map_server map_saver_cli -f maps/map
```

This generates `maps/map.yaml` and `maps/map.pgm` (or a configured image format).
The robot must be publishing `/map` for this command to work.

## Nav2 parameters

`config/nav2_params.yaml` is deliberately a pointer/instructions file, not a
standalone full Nav2 parameter set. Start with the tested configuration shipped
by the installed Nav2/TurtleBot3 simulation. Copy and version that exact file
before changing parameters:

```bash
find /opt/ros/jazzy/share -path '*nav2*' -name 'nav2_params.yaml'
```

Do not pass this README-style starter file as `params_file`. A complete Nav2
parameter file contains parameters for multiple Nav2 lifecycle nodes and must
match the robot model and launch setup.

## Gazebo world

`worlds/obstacle_world.sdf` is a simple standalone Gazebo Harmonic example world.
It is provided as a starting point for experimentation. The reference Nav2
quickstart does not automatically load this file; integrating a custom world
requires matching the simulation launch, robot spawn, map, sensor topics,
frames, and Nav2 configuration.

## Evidence

Add your own real screenshots:
- `screenshots/gazebo.png`: robot visible in Gazebo
- `screenshots/rviz.png`: map, robot model, TF and costmaps visible in RViz2
- `screenshots/autonomous_navigation.png`: goal/path and robot navigating

Record a 1–2 minute demo and put its public URL in `demo/demo_link.txt`.

## Repository contents

- `launch/navigation.launch.py`: wrapper around the official Nav2 quickstart
- `config/nav2_params.yaml`: instructions for obtaining a matching full config
- `maps/map.yaml`: map metadata template; generate the corresponding PGM
- `worlds/obstacle_world.sdf`: standalone sample obstacle world

## Author

Ankit Kumar
