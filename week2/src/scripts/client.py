#!/usr/bin/env python3

import sys
import rospy
from week2.srv import *

def plotter(v: float, w: float):

       rospy.wait_for_service('trajectory')

       try:
              trajectory = rospy.ServiceProxy('trajectory', values)
              response = trajectory(v, w)
              xp = response
              yp = response
              

       except rospy.ServiceException as e:
              print("Service call failed: %s"%e)

if __name__ == "__main__":        
       if len(sys.argv) == 3:
           v = float(sys.argv[1])
           w = float(sys.argv[2])
           print("v = ", v)
           print("W = ", w) 
           plotter(v, w)