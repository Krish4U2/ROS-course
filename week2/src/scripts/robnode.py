#!/usr/bin/env python3
import rospy
#from scripts.radius import*
from week2.srv import data
from week2.msg import flo

def callback():
    rospy.loginfo(rospy.get_caller_id()+"I heard %s", data.data)
    # r = radfun.radius
    # print(r)

def angclient():
    rospy.wait_for_service('compute_ang_vel')
    try:
        pub = rospy.Publisher('cmd_vel', flo, queue_size=10)
        compute_ang_velocity = rospy.ServiceProxy('compute_ang_vel', data)
        resp1 = compute_ang_velocity
        # v = 0.1
        # w = compute_ang_velocity(callback.r, v)
        pub.publish(resp1)
        print(resp1)
        return resp1
        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)




def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber("radius", data, callback)
    print(angclient)
    rospy.spin()     