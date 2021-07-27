#!/usr/bin/env python3
# from std_msgs import float64 
#import numpy as np
from pickle import TRUE
import rospy
from radius import radfun 
from week2.srv import data,dataResponse
# from week2.msg import flo

def compute(request):
    # v = 0.1 #assuemd value of linear velocity
    #v = request.v
    print("Server Ready!")
    #r = int(input("Enter the radius"))
    request.r = radfun.radius
    request.v = 0.1
    print(request.r*request.v)
    return dataResponse(request.v*request.r)    
 

if __name__ == "__main__":
    rospy.init_node('compute_ang_vel',anonymous = TRUE)
    # rospy.Subscriber("radius", flo, compute)
    print('Ready!')
    s = rospy.Service('computation', data, compute)
    rospy.spin()