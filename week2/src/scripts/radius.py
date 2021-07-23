#!/usr/bin/env python3

import rospy
from week2.msg import flo

def radfun():
    pub = rospy.Publisher('radius', flo, queue_size=10)
    rospy.init_node('rpub', anonymous=True)
    rate = rospy.Rate(10) 
    print("Radius Entered")   
    while not rospy.is_shutdown():
        
        radius = 0.9
        #rospy.loginfo(radius)
        pub.publish(radius)
        rate.sleep()
  
if __name__ == '__main__':
    try:
        radfun()
    except rospy.ROSInterruptException:
        pass
