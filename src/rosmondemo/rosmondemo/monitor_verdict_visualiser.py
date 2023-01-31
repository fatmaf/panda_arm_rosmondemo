import rclpy
from rclpy.node import Node
import rosmondemo.TrafficLight as tl

from std_msgs.msg import String

class MonitorVerdictVisualiser(Node):

    def __init__(self,monname,topicname):
        super().__init__('monitor_verdict_visualiser')
        self.visualiser = tl.TrafficLights(monname)

        self.get_logger().info('Creating subscription for '+topicname)
        self.subscription = self.create_subscription(String,topicname,self.callback_test,10)
        self.subscription
        # self.get_logger().info(self.subscription)

    def callback_test(self,data):
        self.get_logger().info("in callback")
        self.get_logger().info(data)
def main(args=None):
    rclpy.init(args=args)

    visualiser = MonitorVerdictVisualiser("panda_arm_movement","/joint_pos_monitor/monitor_verdict")

    rclpy.spin(visualiser)


    visualiser.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
