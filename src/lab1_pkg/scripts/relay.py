#!/usr/bin/env python3

import rospy

from ackermann_msgs.msg import AckermannDriveStamped


def callback(msg):
    msg.drive.speed *= 3
    msg.drive.steering_angle *=3
    pub.publish(msg)


def relay():
    rospy.init_node("relay")

    sub = rospy.Subscriber("drive", AckermannDriveStamped, callback)
    


    

if __name__ == '__main__' :
    try:
        pub = rospy.Publisher("drive_relay", AckermannDriveStamped, queue_size=1)
        relay()
    except rospy.ROSInterruptException:
        pass
    