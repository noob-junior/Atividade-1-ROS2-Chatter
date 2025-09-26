import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hg_/ros2_ws/src/Atividade-1-ROS2-Chatter/install/my_chatter_pkg'
