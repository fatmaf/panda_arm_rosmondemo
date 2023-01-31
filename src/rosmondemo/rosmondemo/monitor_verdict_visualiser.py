import rclpy
from rclpy.node import Node
import rosmondemo.TrafficLight as tl

from std_msgs.msg import String

class MonitorVerdictVisualiser(Node):

    def __init__(self,monname,topicname):
        super().__init__('monitor_verdict_visualiser')
        self.visualiser = tl.TrafficLights(monname)

        self.subscription = self.create_subscription(String,topicname,self.visualiser.changeColor,10)

def main(args=None):
    rclpy.init(args=args)

    visualiser = MonitorVerdictVisualiser("panda_arm_movement","/arm_prop_monitor/monitor_verdict")

    rclpy.spin(visualiser)


    visualiser.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
