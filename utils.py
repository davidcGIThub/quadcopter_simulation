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

def vectorToSkew(vector):
    vector = vector.flatten()
    skewMatrix = np.array([[0 , -vector[2] , vector[1]] , [-vector[2] , 0 , -vector[0]] , [-vector[1] , vector[0] , 0]])
    return skewMatrix

def skewToVector(skewMatrix):
    vector = np.array([ [skewMatrix[2,1]] , [skewMatrix[0,2]], [skewMatrix[1,0]]])
    return vector

def logSO3(R):
    theta = np.arccos((np.trace(R) - 1)/2)
    X = theta*(R-np.transpose(R))/(2*np.sin(theta))
    return X

def logSE3(R,t):
    theta = np.arccos((np.trace(R) - 1)/2)
    w_skew = theta*(R-np.transpose(R))/(2*np.sin(theta))
    w_skew_squared = np.dot(w_skew , w_skew)
    V = np.eye(3) + np.dot( (1-np.cos(theta))/(theta*theta) , w_skew) + \
        np.dot( (theta - np.sin(theta))/(theta*theta*theta)  , w_skew_squared)
    t_ = np.linalg.solve(V,t)
    X = np.concatenate((w_skew,t_),1)
    X = np.concatenate((X,np.array([[0,0,0,0]])) , 0)
    return X

def SE3toVector(T):
    w = skewToVector(T[0:3,0:3])
    t = T[0:3,3]
    t = np.transpose(t[None,:])
    return np.concatenate((t,w),0)

    
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

def leftJacobianSO3
