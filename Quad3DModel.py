import utils
class Quad3DModel:
    def __init__(self,ax,x0=0,y0=0,z0=0,psi0=0):
        self.translation = np.array([[x0],[y0],[z0]])
        self.rotation = utils.rotationZ(psi0)
        self.arm1, = ax.plot([], [], [], lw=2, color='b')
        self.arm2 = ax.plot([], [], [], lw=2, color='b')
        self.arm3 = ax.plot([], [], [], lw=2, color='r')
        self.arm4 = ax.plot([], [], [], lw=2, color='r')
        self.center = ax.plot([],[],[],lw=2,color='b' , marker = 'o')
        self.prop1 = ax.plot([], [], [], lw=2, color='b')
        self.prop2 = ax.plot([], [], [], lw=2, color='b')
        self.prop3 = ax.plot([], [], [], lw=2, color='r')
        self.prop4 = ax.plot([], [], [], lw=2, color='r')
        self.propRadius = 0.1
        self.armLength = 0.3
        self.propOutline = self.generateCircle(self.propRadius,0,0)

    def drawCenter(self):
        target.set_xdata([self.translation[0]])
        target.set_ydata([self.translation[1]])
        target.set_3d_properties([self.translation[2]])

    def drawArms(self):
        
    def drawProps(self):

    def generateCircle(self,radius,x,y):
        circleResolution = 50
        twoPiRadianArray = np.linspace(-np.pi,np.pi,circleResolution)
        circleXdata = np.cos(twoPiRadianArray)*radius
        circleYdata = np.sin(twoPiRadianArray)*radius
        circleZdata = twoPiRadianArray * 0
        circleData = np.concatenate((circleXdata,circleYdata),0)
        circleData = np.concatenate((circleData,circleZdata),0)
        return circleData

        #blah

    def 
