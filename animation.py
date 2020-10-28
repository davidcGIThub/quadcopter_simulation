"""
A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from Quad3DModel import Quad3DModel
import utils



# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)
quad = Quad3DModel(ax)


def update_line(num,quad):
    translation = np.array([[0],[0],[0]])
    rotation = utils.rotationY(0.1)
    quad.update(rotation,translation)
    quad.draw()


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
line_ani = animation.FuncAnimation(fig, update_line, fargs=[quad] , interval=delayBetweenFrames, blit=False)

plt.show()