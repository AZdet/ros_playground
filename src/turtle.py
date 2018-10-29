#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

# Joystick package provides a topic to subscribe
# we have to receive joystick state and then change the movement of turtle accordingly. 

'''

'''

class Turtle_joy:
    def __init__(self):
        self.linear_joymap = 4
        self.angular_joymap = 5
        rospy.init_node('turtle_joy_py', anonymous=True) # must be placed first?
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        
    def callback(self, data):
        cmd = Twist()
        cmd.linear.x = data.axes[self.linear_joymap]
        cmd.angular.z = data.axes[self.angular_joymap]
        self.pub.publish(cmd)

    def listen(self):
        # rospy.init_node('turtle_joy_py', anonymous=True)
        rospy.Subscriber('joy', Joy, self.callback)
        rospy.spin()


    
if __name__ == '__main__':
    t = Turtle_joy()
    t.listen()