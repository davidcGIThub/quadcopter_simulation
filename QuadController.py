import utils
import numpy as np

class QuadController:
    def __init__(self,k):
        self.k = k
        

    def computeDesiredVelocity(self,xc,xd):
        alpha = np.linalg.solve(xc,xd)
        E = utils.logSE3(alpha)
        e = utils.se3toCartesian(E)
        Jl = utils.leftJacobianSE3(E[0:3,0:3],np.array([[E[0,3]],[E[1,3]],[E[2,3]]]))
        u = self.k*Jl*e
        return u