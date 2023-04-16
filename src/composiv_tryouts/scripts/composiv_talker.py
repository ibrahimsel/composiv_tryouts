#!/usr/bin/python3
import rospy
from std_msgs.msg import String

class ComposivTalker(object):
    def __init__(self):
        self.composiv_publisher = rospy.Publisher('composiv', String, queue_size=10)

        # We'll use a rate of 1 Hz to publish 1 messages at a second
        self.rate = rospy.Rate(1)

        while not rospy.is_shutdown():
            self.message = f'Time is: {rospy.Time.now()}'
            self.composiv_publisher.publish(self.message)
            rospy.loginfo(f'I just published a message!: {self.message}')
            # Stop the program for the duration of our chosen rate
            self.rate.sleep()


if __name__ == '__main__':
    rospy.init_node('composiv_talker_node')
    ct = ComposivTalker()
    rospy.spin()
