import utils
import numpy as np

class Quad3DModel:
    def __init__(self,ax,x0=0,y0=0,z0=0,psi0=0):
        self.translation = np.array([[x0],[y0],[z0]])
        self.rotation = utils.rotationZ(psi0)
        self.center, = ax.plot([],[],[],lw=.5,color='k' , marker = 'o')
        self.arm1, = ax.plot([], [], [], lw=2, color='k')
        self.arm2, = ax.plot([], [], [], lw=2, color='k')
        self.arm3, = ax.plot([], [], [], lw=2, color='k')
        self.arm4, = ax.plot([], [], [], lw=2, color='k')
        self.prop1, = ax.plot([], [], [], lw=2, color='b')
        self.prop2, = ax.plot([], [], [], lw=2, color='b')
        self.prop3, = ax.plot([], [], [], lw=2, color='r')
        self.prop4, = ax.plot([], [], [], lw=2, color='r')
        self.propRadius = 0.1
        self.armLength = 0.3
        self.propOutline = self.generateCircle(self.propRadius)
        self.prop1Center = np.array([[self.armLength],[self.armLength],[0]])/np.sqrt(2)
        self.prop2Center = np.array([[self.armLength],[-self.armLength],[0]])/np.sqrt(2)
        self.prop3Center = np.array([[-self.armLength],[self.armLength],[0]])/np.sqrt(2)
        self.prop4Center = np.array([[-self.armLength],[-self.armLength],[0]])/np.sqrt(2)

    def update(self, rotation,translation):
        self.rotation = np.dot(rotation,self.rotation)
        self.translation = translation + self.translation

    def draw(self):
        self.drawArms()
        self.drawProps()
        self.drawCenter()

    def drawCenter(self):
        self.center.set_xdata([self.translation[0,0]])
        self.center.set_ydata([self.translation[1,0]])
        self.center.set_3d_properties([self.translation[2,0]])

    def drawArms(self):
        point1arm1 = self.translation
        point2arm1 = np.dot(self.rotation,self.prop1Center) + self.translation
        self.arm1.set_data([point1arm1[0,0],point2arm1[0,0]] , [point1arm1[1,0],point2arm1[1,0]])
        self.arm1.set_3d_properties([point1arm1[2,0],point2arm1[2,0]])

        point1arm2 = self.translation
        point2arm2 = np.dot(self.rotation,self.prop2Center) + self.translation
        self.arm2.set_data([point1arm2[0,0],point2arm2[0,0]] , [point1arm2[1,0],point2arm2[1,0]])
        self.arm2.set_3d_properties([point1arm2[2,0],point2arm2[2,0]])

        point1arm3 = self.translation
        point2arm3 = np.dot(self.rotation,self.prop3Center) + self.translation
        self.arm3.set_data([point1arm3[0,0],point2arm3[0,0]] , [point1arm3[1,0],point2arm3[1,0]])
        self.arm3.set_3d_properties([point1arm3[2,0],point2arm3[2,0]])

        point1arm4 = self.translation
        point2arm4 = np.dot(self.rotation,self.prop4Center) + self.translation
        self.arm4.set_data([point1arm4[0,0],point2arm4[0,0]] , [point1arm4[1,0],point2arm4[1,0]])
        self.arm4.set_3d_properties([point1arm4[2,0],point2arm4[2,0]])

    def drawProps(self):
        rotatedPropOutline = np.dot(self.rotation,self.propOutline)
        prop1Outline =  np.dot(self.rotation,self.prop1Center) + self.translation + rotatedPropOutline
        prop2Outline =  np.dot(self.rotation,self.prop2Center) + self.translation + rotatedPropOutline
        prop3Outline =  np.dot(self.rotation,self.prop3Center) + self.translation + rotatedPropOutline
        prop4Outline =  np.dot(self.rotation,self.prop4Center) + self.translation + rotatedPropOutline
        self.prop1.set_data(prop1Outline[0,:],prop1Outline[1,:])
        self.prop1.set_3d_properties(prop1Outline[2,:])
        self.prop2.set_data(prop2Outline[0,:],prop2Outline[1,:])
        self.prop2.set_3d_properties(prop2Outline[2,:])
        self.prop3.set_data(prop3Outline[0,:],prop3Outline[1,:])
        self.prop3.set_3d_properties(prop3Outline[2,:])
        self.prop4.set_data(prop4Outline[0,:],prop4Outline[1,:])
        self.prop4.set_3d_properties(prop4Outline[2,:])


    def generateCircle(self,radius):
        circleResolution = 50
        twoPiRadianArray = np.linspace(-np.pi,np.pi,circleResolution)
        circleXdata = np.cos(twoPiRadianArray)*radius
        circleYdata = np.sin(twoPiRadianArray)*radius
        circleZdata = twoPiRadianArray * 0
        circleData = np.concatenate(([circleXdata],[circleYdata]),0)
        circleData = np.concatenate((circleData,[circleZdata]),0)
        return circleData
