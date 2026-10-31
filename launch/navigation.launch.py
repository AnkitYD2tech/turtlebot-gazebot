#!/usr/bin/env python3
"""Launch the official Nav2 TurtleBot3 simulation quickstart.

This wrapper intentionally delegates robot/world/Nav2 setup to the installed,
tested nav2_bringup launch file. It avoids duplicating upstream configuration.
"""
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    nav2_share = get_package_share_directory("nav2_bringup")
    upstream_launch = os.path.join(
        nav2_share, "launch", "tb3_simulation_launch.py"
    )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(upstream_launch),
            launch_arguments={
                "headless": "False",
            }.items(),
        )
    ])
