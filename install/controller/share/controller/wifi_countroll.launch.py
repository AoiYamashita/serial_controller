import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    serial = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'serial',
            output = 'screen',
            )
    web = launch_ros.actions.Node(
            package = 'rosbridge_server',
            executable = 'rosbridge_websocket.py',
            parameters=[{'port': 9091}],
            output = 'screen',
            )
    return launch.LaunchDescription([web,serial])
