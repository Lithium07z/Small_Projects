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
a1, a2, a3, a4, a5, a6 = (0,1,1.5), (-0.58,-0.8,1.5), (0.95,0.3,1.5), (-0.95,0.3,1.5), (0.58,-0.8,1.5), (0,1,1.5) # 2층 별무늬 

b1, b2, b3, b4, b5, b6 = (0,1,1.5), (0,0.5,2.0), (-0.29,-0.4,2.0), (-0.58,-0.8,1.5), (-0.29,-0.4,2.0), (0.475,0.15,2.0)
b7, b8, b9, b10, b11, b12 = (0.95,0.3,1.5), (0.475,0.15,2.0), (-0.475,0.15,2.0), (-0.95,0.3,1.5), (-0.475,0.15,2.0), (0.29,-0.4,2.0)
b13, b14, b15 = (0.58,-0.8,1.5), (0.29,-0.4,2.0), (0,0.5,2.0) # 2층 ~ 3층 점 이어주기 + 3층 별무늬 

c1, c2, c3, c4, c5, c6 = (0,0.5,2.0), (0,0.25,2.5), (-0.145,-0.2,2.5), (-0.29,-0.4,2.0), (-0.145,-0.2,2.5), (0.2375,0.075,2.5)
c7, c8, c9, c10, c11, c12 = (0.475,0.15,2.0), (0.2375,0.075,2.5), (-0.2375,0.075,2.5), (-0.475,0.15,2.0), (-0.2375,0.075,2.5), (0.145,-0.2,2.5)
c13, c14, c15 = (0.29,-0.4,2.0), (0.145,-0.2,2.5), (0,0.25,2.5) # 3층 ~ 4층 점 이어주기 + 4층 별무늬 

d1, d2, d3, d4, d5, d6 = (0,0.25,2.5), (0,0,3.0), (-0.145,-0.2,2.5), (0,0,3.0), (0.2375,0.075,2.5), (0,0,3.0)
d7, d8, d9 = (-0.2375,0.075,2.5), (0,0,3.0), (0.145,-0.2,2.5)

e1, e2, e3, e4, e5, e6 = (0,1,1.5), (0,2,0), (-1.9,0.6,0), (-0.95,0.3,1.5), (-1.9,0.6,0), (-1.16,-1.6,0)
e7, e8, e9, e10, e11, e12 = (-0.58,-0.8,1.5), (-1.16,-1.6,0), (1.16,-1.6,0), (0.58,-0.8,1.5), (1.16,-1.6,0), (1.9,0.6,0)
e13, e14, e15 = (0.95,0.3,1.5), (1.9,0.6,0), (0,2,0)

ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([0,6])

# matrix with row vectors of points
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d') # Axe3D object

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

# scaling transformation matrix
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d') # Axe3D object
sx=1/2
sy=1/3
sz=1/4
T_s = np.array([[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]])

AT_s = T_s @ Anew.T
AT=AT_s[:-1,:].T

BT_s = T_s @ Bnew.T
BT=BT_s[:-1,:].T

CT_s = T_s @ Cnew.T
CT=CT_s[:-1,:].T

DT_s = T_s @ Dnew.T
DT=DT_s[:-1,:].T

ET_s= T_s @ Enew.T
ET=ET_s[:-1,:].T


ax.plot(AT[:,0], AT[:,1], AT[:,2], color='r',alpha=0.6, marker='o')
ax.plot(BT[:,0], BT[:,1], BT[:,2], color='r',alpha=0.6, marker='o')
ax.plot(CT[:,0], CT[:,1], CT[:,2], color='r',alpha=0.6, marker='o')
ax.plot(DT[:,0], DT[:,1], DT[:,2], color='r',alpha=0.6, marker='o')
ax.plot(ET[:,0], ET[:,1], ET[:,2], color='r',alpha=0.6, marker='o')

# overall scaling transformation matrix
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d') # Axe3D object

sall=2
T_sall = np.array([[sall, 0, 0, 0], [0, sall, 0, 0], [0, 0, sall, 0], [0, 0, 0, 1]])

AT_a = T_sall @ Anew.T
ATa=AT_a[:-1,:].T

BT_a = T_sall @ Bnew.T
BTa=BT_a[:-1,:].T

CT_a = T_sall @ Cnew.T
CTa=CT_a[:-1,:].T

DT_a = T_sall @ Dnew.T
DTa=DT_a[:-1,:].T

ET_a= T_sall @ Enew.T
ETa=ET_a[:-1,:].T

ax.plot(ATa[:,0], ATa[:,1], ATa[:,2], color='g',alpha=0.6, marker='o')
ax.plot(BTa[:,0], BTa[:,1], BTa[:,2], color='g',alpha=0.6, marker='o')
ax.plot(CTa[:,0], CTa[:,1], CTa[:,2], color='g',alpha=0.6, marker='o')
ax.plot(DTa[:,0], DTa[:,1], DTa[:,2], color='g',alpha=0.6, marker='o')
ax.plot(ETa[:,0], ETa[:,1], ETa[:,2], color='g',alpha=0.6, marker='o')

# rotational in z
fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d') # Axe3D object

theta=np.pi/2
cs=np.cos(theta)
ss=np.sin(theta)

T_rz = np.array([[cs, ss, 0, 0], [-ss, cs, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
T_rx = np.array([[1, 0, 0, 0],[0, cs, ss, 0], [0, -ss, cs, 0], [0, 0, 0, 1]])
T_ry = np.array([[cs, 0 -ss, 0], [0, 1, 0, 0], [ss, 0, cs, 0], [0, 0, 0, 1]])

AT_rz = T_rz @ Anew.T
ATrz=AT_rz[:-1,:].T

BT_rz = T_rz @ Bnew.T
BTrz=BT_rz[:-1,:].T

CT_rz = T_rz @ Cnew.T
CTrz=CT_rz[:-1,:].T

DT_rz = T_rz @ Dnew.T
DTrz=DT_rz[:-1,:].T

ET_rz = T_rz @ Enew.T
ETrz=ET_rz[:-1,:].T

ax.plot(ATrz[:,0], ATrz[:,1], ATrz[:,2], color='b',alpha=0.6, marker='o')
ax.plot(BTrz[:,0], BTrz[:,1], BTrz[:,2], color='b',alpha=0.6, marker='o')
ax.plot(CTrz[:,0], CTrz[:,1], CTrz[:,2], color='b',alpha=0.6, marker='o')
ax.plot(DTrz[:,0], DTrz[:,1], DTrz[:,2], color='b',alpha=0.6, marker='o')
ax.plot(ETrz[:,0], ETrz[:,1], ETrz[:,2], color='b',alpha=0.6, marker='o')


# shearing
fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d') # Axe3D object

b= -0.85
c= 0.25
d= -0.75
f= 0.7
g= 0.5
i= 1
T_sh = np.array([[1, d, g, 0], [b, 1, i, 0], [c, f, 1, 0], [0, 0, 0, 1]])

AT_sh = T_sh @ Anew.T
ATsh=AT_sh[:-1,:].T

BT_sh = T_sh @ Bnew.T
BTsh=BT_sh[:-1,:].T

CT_sh = T_sh @ Cnew.T
CTsh=CT_sh[:-1,:].T

DT_sh = T_sh @ Dnew.T
DTsh=DT_sh[:-1,:].T

ET_sh = T_sh @ Enew.T
ETsh=ET_sh[:-1,:].T


ax.plot(ATsh[:,0], ATsh[:,1], ATsh[:,2], color='c',alpha=0.6, marker='o')
ax.plot(BTsh[:,0], BTsh[:,1], BTsh[:,2], color='c',alpha=0.6, marker='o')
ax.plot(CTsh[:,0], CTsh[:,1], CTsh[:,2], color='c',alpha=0.6, marker='o')
ax.plot(DTsh[:,0], DTsh[:,1], DTsh[:,2], color='c',alpha=0.6, marker='o')
ax.plot(ETsh[:,0], ETsh[:,1], ETsh[:,2], color='c',alpha=0.6, marker='o')

plt.show()
