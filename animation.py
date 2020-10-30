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
controller = QuadController(.5)

#target
xd = 2
yd = 3
zd = 2
psid = np.pi/2
desiredRotation = utils.rotationZ(psid)
desiredTranslation = np.array([[xd],[yd],[zd]])
temp = np.concatenate((desiredRotation,desiredTranslation),1)
desiredTransformation = np.concatenate((temp,np.array([[0,0,0,1]])))
target = Quad3DGraphics(ax,True,xd,yd,zd,psid)


def update_line(num,quad,controller,target):
    xc = quad.getTransformation()
    xd = target.getTransformation()
    V_body = controller.computeDesiredVelocities(xc,xd)
    v_body = np.array([V_body[0,0]],V_body[1,0],V_body[2,0])
    w_body = np.array([V_body[3,0]],V_body[4,0],V_body[5,0])
    Rbody2local = np.transpose(xc.getRotation())
    v_local = np.dot(Rbody2local,v_body)
    w_local = np.dot(Rbody2local,w_body)

    translation = np.array([[0],[0],[.1]])
    rotation = utils.rotationY(0.1)
    quad.update(rotation,translation)
    quad.draw()
    target.draw()


# Setting the axes properties
ax.set_xlim3d([-5.0, 5.0])
ax.set_xlabel('X')

ax.set_ylim3d([-5.0, 5.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-5.0, 5.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')


# Creating the Animation object
delayBetweenFrames_ms = 50
dt = delayBetweenFrames_ms / 1000
frames = 25
line_ani = animation.FuncAnimation(fig, update_line, fargs=[quad,controller,target,dt] , interval=delayBetweenFrames_ms, blit=False)

plt.show()