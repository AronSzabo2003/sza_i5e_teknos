#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class HeartDraw(Node):
    def __init__(self):
        super().__init__('szivrajz')
        self.publisher_ = self.create_publisher(Twist, '/turtlesim1/turtle1/cmd_vel', 10)

        self.steps = [
            (0.0, math.radians(120), 1.0),  # 90°-os balra fordulás (kezdés)
            (2.0, 0.0, 1.0),          # Egyenes felfelé
            (0.0, -math.radians(300), 0.5), # Jobbra fordulás 140°
            (1.0, 0.0, 1.0),          # Jobbra egyenes
            
            (0.0,math.radians(120), 0.5), # Jobbra fordulás 90°
            (1.0, 0.0, 1.0),          # Lefelé egyenes
            (0.0, -math.radians(320), 0.5), # Jobbra fordulás 90°
            (2.0, 0.0, 1.0),          # Lefelé befejezés
            (0.0, 0.0, 1.0)           # Leállás
        ]

        self.current_step = 0
        self.timer = self.create_timer(0.1, self.loop)

        self.get_logger().info("Szögletes szív rajzolása indul.")

    def publish_message(self, fwd, turn):
        """Sebesség és fordulás elküldése a teknősnek"""
        message = Twist()
        message.linear.x = fwd
        message.angular.z = turn
        self.publisher_.publish(message)
        self.get_logger().info(f"Sebesség: {fwd:.1f}, Fordulás: {turn:.1f}")

    def loop(self):
        """A mozgási lépések végrehajtása időzítve"""
        if self.current_step < len(self.steps):
            fwd, turn, duration = self.steps[self.current_step]
            self.publish_message(fwd, turn)
            self.current_step += 1
            self.timer.cancel()
            self.timer = self.create_timer(duration, self.loop)  
        else:
            self.get_logger().info("Szögletes szív kész. Leállítás.")
            self.publish_message(0.0, 0.0)  
            self.timer.cancel()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = HeartDraw()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass  
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
