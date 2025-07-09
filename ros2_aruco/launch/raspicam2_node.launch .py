from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='opencv',
            executable='img_compressed2raw',
            name='img_compressed2raw',
            output='screen',
        ),

        Node(
            package='ros2_aruco',
            executable='aruco_raspicam2',
            name='aruco_raspicam2',
            output='screen',
        ),
    ])

