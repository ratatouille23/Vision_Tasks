#!/usr/bin/env python3

import rospy

from ackermann_msgs.msg import AckermannDriveStamped

def talker():
    rospy.init_node("talker")

    pub = rospy.Publisher("drive", AckermannDriveStamped, queue_size=1)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        v = rospy.get_param("v")
        d = rospy.get_param("d")

        msg = AckermannDriveStamped()

        msg.drive.speed = v
        msg.drive.steering_angle = d

        pub.publish(msg)

        rospy.loginfo(msg)

        rate.sleep()

if __name__ == '__main__' :
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    