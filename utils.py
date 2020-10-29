import numpy as np



def rotationX(phi):
    cphi = np.cos(phi)
    sphi = np.sin(phi)
    R = np.array([[1 , 0 , 0 ] , [0 , cphi , -sphi] , [0 , sphi , cphi] ])
    return R

def rotationY(theta):
    ctheta = np.cos(theta)
    stheta = np.sin(theta)
    R = np.array([ [ctheta , 0 , stheta] , [0 , 1 , 0 ] , [-stheta , 0 , ctheta ] ])
    return R

def rotationZ(psi):
    cpsi = np.cos(psi)
    spsi = np.sin(psi)
    R = np.array([ [cpsi , -spsi , 0] , [spsi , cpsi , 0 ] , [0 , 0 , 1] ])
    return R

def vectorToSkew(self,vector):
    vector = vector.flatten()
    skewMatrix = np.array([[0 , -vector[2] , vector[1]] , [-vector[2] , 0 , -vector[0]] , [-vector[1] , vector[0] , 0]])
    return skewMatrix

def skewToVector(self,skewMatrix):
    vector = np.array([ [skewMatrix[2,1]] , [skewMatrix[0,2]], [skewMatrix[1,0]]])
    return vector

def logRMatrix(self,R):
    theta = np.arccos((np.trace(R) - 1)/2)
    X = theta*(R-np.transpose(R))/(2*np.sin(theta))
    return X

def toSE3Matrix(R,t):
    A = np.concatenate((R,t),1)
    A = np.concatenate((A,[0,0,0,1]),0)
    return A

def SE3Transformation(R,t,points):
    A = np.concatenate((R,t),1)
    A = np.concatenate((A,[0,0,0,1]),0)
    bottomRow = np.ones(np.size(points[1]))
    pointsR4 = np.concatenate((points,bottomRow),0)
    newPointsR4 = np.dot(A,pointsR4)
    newPoints = newPointsR4[0:3,:]
    return newPoints
