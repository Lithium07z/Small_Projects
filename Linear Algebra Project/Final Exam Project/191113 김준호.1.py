# matplotlib color code: color='#eeefff' or, r, g, b, k, y, m ,c, y

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import string
import turtle as t

# 3D figure 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # Axe3D object

# points a, b and, c
a1, a2, a3, a4, a5, a6 = (0,1,0.2), (-0.58,-0.8,0.2), (0.95,0.3,0.2), (-0.95,0.3,0.2), (0.58,-0.8,0.2), (0,1,0.2) # 2층 별무늬 

b1, b2, b3, b4, b5, b6 = (0,1,0.2), (0,0.5,0.4), (-0.29,-0.4,0.4), (-0.58,-0.8,0.2), (-0.29,-0.4,0.4), (0.475,0.15,0.4)
b7, b8, b9, b10, b11, b12 = (0.95,0.3,0.2), (0.475,0.15,0.4), (-0.475,0.15,0.4), (-0.95,0.3,0.2), (-0.475,0.15,0.4), (0.29,-0.4,0.4)
b13, b14, b15 = (0.58,-0.8,0.2), (0.29,-0.4,0.4), (0,0.5,0.4) # 2층 ~ 3층 점 이어주기 + 3층 별무늬 

c1, c2, c3, c4, c5, c6 = (0,0.5,0.4), (0,0.25,0.6), (-0.145,-0.2,0.6), (-0.29,-0.4,0.4), (-0.145,-0.2,0.6), (0.2375,0.075,0.6)
c7, c8, c9, c10, c11, c12 = (0.475,0.15,0.4), (0.2375,0.075,0.6), (-0.2375,0.075,0.6), (-0.475,0.15,0.4), (-0.2375,0.075,0.6), (0.145,-0.2,0.6)
c13, c14, c15 = (0.29,-0.4,0.4), (0.145,-0.2,0.6), (0,0.25,0.6) # 3층 ~ 4층 점 이어주기 + 4층 별무늬 

d1, d2, d3, d4, d5, d6 = (0,0.25,0.6), (0,0,0.8), (-0.145,-0.2,0.6), (0,0,0.8), (0.2375,0.075,0.6), (0,0,0.8)
d7, d8, d9 = (-0.2375,0.075,0.6), (0,0,0.8), (0.145,-0.2,0.6)

e1, e2, e3, e4, e5, e6 = (0,1,0.2), (0,2,0), (-1.9,0.6,0), (-0.95,0.3,0.2), (-1.9,0.6,0), (-1.16,-1.6,0)
e7, e8, e9, e10, e11, e12 = (-0.58,-0.8,0.2), (-1.16,-1.6,0), (1.16,-1.6,0), (0.58,-0.8,0.2), (1.16,-1.6,0), (1.9,0.6,0)
e13, e14, e15 = (0.95,0.3,0.2), (1.9,0.6,0), (0,2,0)


# matrix with row vectors of points
A = np.array([a1, a2, a3, a4, a5, a6])
Anew=np.zeros((A.shape[0],A.shape[1]+1))
AT=np.zeros((A.shape[0],A.shape[1]))
Ac=np.ones((1,A.shape[0]))
Anew[:,:-1]=A
Anew[:,-1]=Ac

B = np.array([b1, b2, b3, b4, b5, b6,
              b7, b8, b9, b10, b11, b12,
              b13, b14, b15])
Bnew=np.zeros((B.shape[0],B.shape[1]+1))
BT=np.zeros((B.shape[0],B.shape[1]))
Bc=np.ones((1,B.shape[0]))
Bnew[:,:-1]=B
Bnew[:,-1]=Bc

C = np.array([c1, c2, c3, c4, c5, c6,
              c7, c8, c9, c10, c11, c12,
              c13, c14, c15])
Cnew=np.zeros((C.shape[0],C.shape[1]+1))
CT=np.zeros((C.shape[0],C.shape[1]))
Cc=np.ones((1,C.shape[0]))
Cnew[:,:-1]=C
Cnew[:,-1]=Cc

D = np.array([d1, d2, d3, d4, d5, d6,
              d7, d8, d9])
Dnew=np.zeros((D.shape[0],D.shape[1]+1))
DT=np.zeros((D.shape[0],D.shape[1]))
Dc=np.ones((1,D.shape[0]))
Dnew[:,:-1]=D
Dnew[:,-1]=Dc

E = np.array([e1, e2, e3, e4, e5, e6,
              e7, e8, e9, e10, e11, e12,
              e13, e14, e15])
Enew=np.zeros((E.shape[0],E.shape[1]+1))
ET=np.zeros((E.shape[0],E.shape[1]))
Ec=np.ones((1,E.shape[0]))
Enew[:,:-1]=E
Enew[:,-1]=Ec

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6, marker='o')
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6, marker='o')
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6, marker='o')
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6, marker='o')
ax.plot(E[:,0], E[:,1], E[:,2], color='k', alpha=0.6, marker='o')

plt.show()
