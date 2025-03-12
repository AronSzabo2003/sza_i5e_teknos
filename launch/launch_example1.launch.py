from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),      
        Node(
             package='sza_i5e_teknos',
             executable='szivrajz',
             name='szivrajz',
             output='screen',

         ),
    ])