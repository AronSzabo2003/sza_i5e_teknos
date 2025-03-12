from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_name = 'sza_i5e_teknos'
    script_path = os.path.join(get_package_share_directory(package_name), '..', 'lib', package_name, 'szivrajz.py')

    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),      
        Node(
            package=package_name,
            executable='szivrajz.py',  # Python fájlneve pontosan!
            name='szivrajz',
            output='screen'
        ),
    ])
