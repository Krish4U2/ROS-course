
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        for _ in range(n):  
            self.theta += w*(self.dt) 
            self.x += v*np.cos(self.theta)
            self.y += v*np.sin(self.theta)
            self.x_points.append(self.x)
            self.y_points.append(self.y)
      
        self.plot(v, w)
        
        #return x , y, theta
 
    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show()
       

if __name__ == "__main__":
    print("Unicycle Model Assignment")

    # make an object of the robot and plot various trajectories
    obj1 = Unicycle(0, 0, 0, 0.1)
    obj2 = Unicycle(0, 0, 1.57, 0.2)
    obj3 = Unicycle(0, 0, 0.77, 0.05)

    obj1.step(1, 0.5, 25)
    obj2.step(0.5, 1, 10)
    obj3.step(5, 4, 50)
