from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_aruco',
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
        Node(
    package='rqt_image_view',
    executable='rqt_image_view',
    name='rqt_image_view',
    output='screen',
    parameters=[{'image_transport': 'compressed'}],
    remappings=[('image', '/camera/image')]
)
    ])

