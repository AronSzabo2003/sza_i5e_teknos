import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class HeartDraw(Node):
    def __init__(self):
        super().__init__('szivrajz')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.steps = [
            (2.0, math.pi / 4, 1.5),
            (0.0, -math.pi / 2, 1.0),
            (2.0, -math.pi / 4, 1.5),
            (2.0, math.pi / 4, 1.5),
            (0.0, -math.pi / 2, 1.0),
            (2.0, -math.pi / 4, 1.5),
            (2.0, 0.0, 2.0),
        ]
        self.current_step = 0
        self.timer = self.create_timer(2.0, self.loop)  # 2 másodperces ciklus

        self.get_logger().info("Drawing a heart shape in turtlesim.")

    def publish_message(self, fwd, turn):
        message = Twist()
        message.linear.x = fwd
        message.angular.z = turn
        self.get_logger().info(f"Moving - Speed: {message.linear.x:.1f}, Turn: {message.angular.z:.1f}")
        self.publisher_.publish(message)

    def loop(self):
        if self.current_step < len(self.steps):
            fwd, turn, duration = self.steps[self.current_step]
            self.publish_message(fwd, turn)
            self.current_step += 1
        else:
            self.get_logger().info("Heart drawing finished. Stopping.")
            self.timer.cancel()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = HeartDraw()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
