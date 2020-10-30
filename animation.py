"""
A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from Quad3DGraphics import Quad3DGraphics
import utils
from QuadController import QuadController



# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)
quad = Quad3DGraphics(ax)
kl = .5
ka = .2
controller = QuadController(kl,ka)

#target
xd = 2
yd = 3
zd = 4
psid = np.pi
target = Quad3DGraphics(ax,True,xd,yd,zd,psid)

def update_line(num,quad,controller,target,dt):
    xc = quad.getTransformation()
    xd = target.getTransformation()
    V_body = controller.computeDesiredVelocities(xc,xd)
    [rotation,translation] = controller.kinematicPropagation(V_body,xc,dt)
    quad.update(rotation,translation)
    quad.draw()
    target.draw()


# Setting the axes properties
ax.set_xlim3d([-5.0, 5.0])
ax.set_xlabel('X')

ax.set_ylim3d([-5.0, 5.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 10.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')


# Creating the Animation object
delayBetweenFrames_ms = 50
dt = delayBetweenFrames_ms / 1000
frames = 25
line_ani = animation.FuncAnimation(fig, update_line, fargs=[quad,controller,target,dt] , interval=delayBetweenFrames_ms, blit=False)

plt.show()