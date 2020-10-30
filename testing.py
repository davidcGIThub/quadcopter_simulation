import numpy as np 
from scipy.linalg import logm, expm
import utils

phi = np.pi/4
theta = np.pi/3
psi = -np.pi/6
R = np.dot(np.dot(utils.rotationX(phi),utils.rotationY(theta)) , utils.rotationZ(psi))
print("R: " , R)
A = utils.logSO3(R)
B = logm(R)

print("A: " , A)
print("B: " , B)

t = np.array([[1],[-.5],[1]])
T = np.concatenate( (np.concatenate((R,t),1) , np.array([[0,0,0,1]])) , 0)
C = utils.logSE3_(R,t)
D = logm(T)
F = utils.SE3toEul(D)

JSO3l = utils.leftJacobianSO3(R)
JSO3r = utils.rightJacobianS03(R)
JSE3 = utils.leftJacobianSE3(R,t)

print("C: " , C)
print("D: " , D)
print("F: " , F)
print("JSO3l: ", JSO3l)
print("JSO3r", JSO3r )
print("JSE3: ", JSE3)

G = utils.SO3toEuler(R)
print("G: " , G)