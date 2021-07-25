#!/usr/bin/env python3
import matplotlib.pyplot as plt
from pickle import TRUE
import rospy 
import numpy as np
from week2.srv import values, valuesResponse
  
class Unicycle:
    
    def __init__(self, x: float, y: float, theta: float):
        self.x = x
        self.y = y
        self.theta = theta
        

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]
    # def step(self, v: float, w: float):
    def calc_trajectory(self,request):
       v = request.v
       w = request.w
       for i in range(50):
            self.theta += w*(0.05)
            self.x += v*np.cos(self.theta)
            self.y += v*np.sin(self.theta)
            self.x_points.append(self.x)
            self.y_points.append(self.y)
        
       self.plot(v, w)
        
        #return x , y, theta
 
    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        print("Plotting..")
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show()
           
       #return valuesResponse(self.x_points, self.y_points)
       
if __name__ == "__main__":
   
    rospy.init_node('server',anonymous = TRUE)
    print('Ready!')
    obj = Unicycle(0,0,0)
    # obj.trajectory(1, 0.5)
    s = rospy.Service('trajectory', values, obj.calc_trajectory)
    rospy.spin()
# def trajectory(request):
#     x_points = []
#     y_points = []

#     v = request.v
#     w = request.w

#     for i in range(50):
#         theta += w*(0.05)
#         x += v*np.cos(theta)
#         y += v*np.sin(theta)

#         x_points.append(x)
#         y_points.append(y)
#         return x_points,y_points,theta  