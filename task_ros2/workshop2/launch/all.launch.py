import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # Path to parameter file
    pkg_share = get_package_share_directory('workshop2')

    # 1. go_to_goal launch file
    go_to_goal_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'go_to_goal.launch.py')
        )
    )

    # 2. turtlesim_node launch file
    turtlesim_node_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'turtlesim_node.launch.py')
        )
    )

    # 3. activator launch file
    activator_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'activator.launch.py')
        )
    )

    return LaunchDescription([
        go_to_goal_launch,
        turtlesim_node_launch,
    ])