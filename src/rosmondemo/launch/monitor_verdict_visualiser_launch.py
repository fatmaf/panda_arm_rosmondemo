from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rosmondemo',
            namespace='rosmondemo',
            executable='monitor_verdict_visualiser',
            name='visualiser'
        )
    ])