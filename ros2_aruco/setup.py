from setuptools import setup
from glob import glob
import os

package_name = 'ros2_aruco'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        # 필수 패키지 인덱스 및 메타데이터
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # launch 폴더 설치 경로에 포함
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nathan Sprague',
    maintainer_email='nathan.r.sprague@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aruco_node = ros2_aruco.aruco_node:main',
            'aruco_raspicam2 = ros2_aruco.aruco_raspicam2:main',
            'aruco_usbcam = ros2_aruco.aruco_usbcam:main',
            'aruco_generate_marker = ros2_aruco.aruco_generate_marker:main',
            'img_compressed2raw = ros2_aruco.img_compressed2raw:main',
        ],
    },
)

