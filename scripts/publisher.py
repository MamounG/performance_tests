#!/usr/bin/env python
import rospy
from performance_tests.msg import SuperAwesome
import sys


def talker():
    freq = "10"
    nbTests = "50"
    if (len(sys.argv) > 3 or len(sys.argv) <= 0):
        rospy.loginfo("FAIL")
        rospy.loginfo("usage: rosrun performance_tests publisher.py [rate] [nbTests]")
    elif (len(sys.argv) == 1):
        rospy.loginfo("no rate nor nbTests defined, using default rate: [%s] hz and default nbTests: [%s]" % freq, nbTests)
    elif len(sys.argv) == 2:
        rospy.loginfo("no nbTests defined, using default nbTests: [%s]" % nbTests)
        freq = sys.argv[1]
    else:
        freq = sys.argv[1]
        nbTests = sys.argv[2]
    iRate = int(freq)
    iNbTests = int(nbTests)
    pub = rospy.Publisher('SuperTopic', SuperAwesome, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(iRate) 
    count = 0
    while not rospy.is_shutdown() and count < iNbTests:
        msg = "nb %s" % count #rospy.get_time()
        #rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
        count += 1
        
    EndMsg = "FIN|Python|"+freq
    #rospy.loginfo(EndMsg)
    pub.publish(EndMsg)
    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
