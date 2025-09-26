import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TalkerNode(Node):

    def __init__(self):
    
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        timer_period = 1.0  
        self.timer_ = self.create_timer(timer_period, self.timer_callback)
        
        self.counter_ = 0

    def timer_callback(self):
    
        msg = String()
        msg.data = f"farmando aura {self.counter_}"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    talker_node = TalkerNode()
    rclpy.spin(talker_node)
    talker_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
