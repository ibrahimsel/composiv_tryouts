#!/usr/bin/python3
import rospy
from std_msgs.msg import String

class ComposivListener():
    def __init__(self):
        self.composiv_listener = rospy.Subscriber('composiv', String, self.composiv_callback)

    # This function gets triggered everytime it receives a message from 'composiv' topic
    def composiv_callback(self, data):
        rospy.loginfo(data)

if __name__ == '__main__':
    rospy.init_node('composiv_listener_node')
    ct = ComposivListener()
    rospy.spin()
