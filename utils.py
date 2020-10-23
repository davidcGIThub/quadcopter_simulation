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
