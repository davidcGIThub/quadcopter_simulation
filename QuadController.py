import utils
import numpy as np

class QuadController:
    def __init__(self,k):
        self.k = k
        

    def computeDesiredVelocities(self,xc,xd):
        alpha = np.linalg.solve(xc,xd)
        E = utils.logSE3(alpha)
        e = utils.se3toCartesian(E)
        Jl = utils.leftJacobianSE3(E[0:3,0:3],np.array([[E[0,3]],[E[1,3]],[E[2,3]]]))
        u = self.k*np.dot(Jl,e)
        return u

    def kinematicPropagation(self,V_body,xc,dt):
        currentRotation = xc[0:3,0:3]
        v_body = np.array([[V_body[0,0]],[V_body[1,0]],[V_body[2,0]]])
        w_body = np.array([[V_body[3,0]],[V_body[4,0]],[V_body[5,0]]])
        Rbody2local = np.transpose(currentRotation)
        v_local = np.dot(Rbody2local,v_body)
        w_local = np.dot(Rbody2local,w_body)
        translation = v_local*dt
        rotation = dt*utils.vectorToSkew(w_local) + np.eye(3)
        return [rotation,translation]