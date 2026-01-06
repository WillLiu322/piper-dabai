import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wzb/ros2ws/moveit_ws/install/moveit_configs_utils'
