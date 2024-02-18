import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
import serial

class serial_indep(Node):
    def __init__(self):
        self.writer = serial.Serial("/dev/ttyACM0",115200,timeout=0.1)
        super().__init__("serial_indep")
        self.subscription = self.create_subscription(Int8,"Serial_data",self.cb,10)
    def cb(self,data):
        a = 'n'
        if(data.data== 0):
            a = 'w'
        elif(data.data == 1):
            a = 'a'
        elif(data.data == 2):
            a = 's'
        elif(data.data == 3):
            a = 'd'
        else:
            return
        self.writer.write(a.encode())
        self.get_logger().info("send: %c" % a)

def main():
    rclpy.init()
    serialIndep = serial_indep()
    rclpy.spin(serialIndep)
