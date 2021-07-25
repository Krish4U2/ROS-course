#!/usr/bin/env python3
import math
from pickle import TRUE
import rospy 
from week2.srv import data
from week2.msg import flo

def compute(r):
    v = 0.1 #assuemd value of linear velocity
    w = v*r
    print(w)
 

if __name__ == "__main__":
    rospy.init_node('compute_ang_vel',anonymous = TRUE)
    rospy.Subscriber("radius", flo, compute)
    print('Ready!')
    s = rospy.Service('computation', data, compute)
    rospy.spin()