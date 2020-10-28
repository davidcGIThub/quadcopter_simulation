"""
A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation



# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)
line1, = ax.plot([], [], [], lw=2, color='b')
target1, = ax.plot([],[],[],lw=2,color='r' , marker = 'o')
circle1, = ax.plot([],[],[],lw=2,color='g')
radius = 1
circleResolution = 50
twoPiRadianArray = np.linspace(-np.pi,np.pi,circleResolution)
circleXdata = np.cos(twoPiRadianArray)*radius
circleYdata = np.sin(twoPiRadianArray)*radius
circleZdata = np.sin(twoPiRadianArray*5)/2


def update_line(num,line,target,circle):
    target.set_xdata([2])
    target.set_ydata([3])
    target.set_3d_properties([1])
    line.set_data([0,1],[0,0])
    line.set_3d_properties([0,0])
    circle.set_data(circleXdata,circleYdata)
    circle.set_3d_properties(circleZdata)


# Setting the axes properties
ax.set_xlim3d([-5.0, 5.0])
ax.set_xlabel('X')

ax.set_ylim3d([-5.0, 5.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-5.0, 5.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')


# Creating the Animation object
delayBetweenFrames = 50
frames = 25
line_ani = animation.FuncAnimation(fig, update_line, fargs=[line1,target1,circle1] , interval=delayBetweenFrames, blit=False)

plt.show()