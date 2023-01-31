import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import threading
#from https://stackoverflow.com/questions/24588406/creating-a-traffic-light-using-python


from tkinter import *

class TrafficLights:

    def __init__(self,name):

        window = Tk()
        window.title("Monitor "+name)

        frame = Frame(window)
        frame.pack()

        self.canvas = Canvas(window, width=120, height=340, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(10, 120, 110, 220, fill="white")
        self.oval_green = self.canvas.create_oval(10, 230, 110, 330, fill="white")

        # self.color.set('R')
        self.canvas.itemconfig(self.oval_yellow, fill="yellow")

        window.mainloop()

    def monitorCallback(self,data):
        print(data)
        colors = {"true":'G',"unknown":'Y',"false":'R'}
        truestr = "true"
        falsestr = "false"
        unknownstr = "unknown"
        if truestr in data.data:
            self.changeColor(colors[truestr])
        elif falsestr in data.data:
            self.changeColor(colors[falsestr])
        elif unknownstr in data.data:
            self.changeColor(colors[unknownstr])


    def changeColor(self,color):
        # color = 'R'#self.color.get()

        if color == 'R':
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'Y':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'G':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':

    process_thread = threading.Thread(target=main)
    process_thread.start()
    TrafficLights()