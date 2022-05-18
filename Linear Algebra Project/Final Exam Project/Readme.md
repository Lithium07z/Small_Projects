# 기말고사 프로젝트 : 파이썬을 이용하여 변환행렬 이용해보기

1. 변환행렬 참고사이트 <br>
https://alyssaq.github.io/2015/visualising-matrices-and-affine-transformations-with-python/  <br>
https://www.youtube.com/watch?v=WKkY_WNCj_Q  <br>
https://stackabuse.com/affine-image-transformations-in-python-with-numpy-pillow-and-opencv/  <br>

2. 아래 코드를 실행해 본 다음 간단한 도형에 대하여 3차원 변환 행렬을 실행해 보시오. <br>

// matplotlib color code: color='#eeefff' or, r, g, b, k, y, m ,c, y <br>

import matplotlib.pyplot as plt <br>
from mpl_toolkits.mplot3d import Axes3D <br>
import numpy as np <br>
import string <br>
import turtle as t <br>

// 3D figure <br>
fig = plt.figure() <br>
ax = fig.add_subplot(111, projection='3d') # Axe3D object <br>

// points a, b and, c <br>
a1, a2, a3, a4, a5 = (0,0,1), (2,0,1), (2,3,1), (0,3,1), (0,0,1) <br>
b1, b2, b3, b4, b5 = (0,0,0), (2,0,0), (2,3,0), (0,3,0), (0,0,0) <br>
c1, c2, c3, c4, c5 = (0,0,1), (2,0,1), (2,0,0), (0,0,0), (0,0,1) <br>
d1, d2, d3, d4, d5 = (2,3,1), (0,3,1), (0,3,0), (2,3,0), (2,3,1) <br>

// matrix with row vectors of points <br>
A = np.array([a1, a2, a3, a4, a5]) <br>
Anew=np.zeros((A.shape[0],A.shape[1]+1)) <br>
AT=np.zeros((A.shape[0],A.shape[1])) <br>
Ac=np.ones((1,A.shape[0])) <br>
Anew[:,:-1]=A <br>
Anew[:,-1]=Ac <br>

B = np.array([b1, b2, b3, b4, b5]) <br>
Bnew=np.zeros((B.shape[0],B.shape[1]+1)) <br>
BT=np.zeros((B.shape[0],B.shape[1])) <br>
Bc=np.ones((1,B.shape[0])) <br>
Bnew[:,:-1]=B <br>
Bnew[:,-1]=Bc <br>

C = np.array([c1, c2, c3, c4, c5]) <br>
Cnew=np.zeros((C.shape[0],C.shape[1]+1)) <br>
CT=np.zeros((C.shape[0],C.shape[1])) <br>
Cc=np.ones((1,C.shape[0])) <br>
Cnew[:,:-1]=C <br>
Cnew[:,-1]=Cc <br>

D = np.array([d1, d2, d3, d4, d5]) <br>
Dnew=np.zeros((D.shape[0],D.shape[1]+1)) <br>
DT=np.zeros((D.shape[0],D.shape[1])) <br>
Dc=np.ones((1,D.shape[0])) <br>
Dnew[:,:-1]=D <br>
Dnew[:,-1]=Dc <br>

ax.plot(A[:,0], A[:,1], A[:,2], color='k', alpha=0.6, marker='o') <br>
ax.plot(B[:,0], B[:,1], B[:,2], color='k', alpha=0.6, marker='o') <br>
ax.plot(C[:,0], C[:,1], C[:,2], color='k', alpha=0.6, marker='o') <br>
ax.plot(D[:,0], D[:,1], D[:,2], color='k', alpha=0.6, marker='o') <br>


// scaling transformation matrix <br>
sx=1/2 <br>
sy=1/3 <br>
sz=1 <br>
T_s = np.array([[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]]) <br>

AT_s = T_s @ Anew.T <br>
AT=AT_s[:-1,:].T <br>

BT_s = T_s @ Bnew.T <br>
BT=BT_s[:-1,:].T <br>

CT_s = T_s @ Cnew.T <br>
CT=CT_s[:-1,:].T <br>

DT_s = T_s @ Dnew.T <br>
DT=DT_s[:-1,:].T <br>


ax.plot(AT[:,0], AT[:,1], AT[:,2], color='r',alpha=0.6, marker='o') <br>
ax.plot(BT[:,0], BT[:,1], BT[:,2], color='r',alpha=0.6, marker='o') <br>
ax.plot(CT[:,0], CT[:,1], CT[:,2], color='r',alpha=0.6, marker='o') <br>
ax.plot(DT[:,0], DT[:,1], DT[:,2], color='r',alpha=0.6, marker='o') <br>


// overall scaling transformation matrix <br>
sall=2 <br>
T_sall = np.array([[sall, 0, 0, 0], [0, sall, 0, 0], [0, 0, sall, 0], [0, 0, 0, 1]]) <br>

AT_a = T_sall @ Anew.T <br>
ATa=AT_a[:-1,:].T <br>

BT_a = T_sall @ Bnew.T <br>
BTa=BT_a[:-1,:].T <br>

CT_a = T_sall @ Cnew.T <br>
CTa=CT_a[:-1,:].T <br>

DT_a = T_sall @ Dnew.T <br>
DTa=DT_a[:-1,:].T <br>


ax.plot(ATa[:,0], ATa[:,1], ATa[:,2], color='g',alpha=0.6, marker='o') <br>
ax.plot(BTa[:,0], BTa[:,1], BTa[:,2], color='g',alpha=0.6, marker='o') <br>
ax.plot(CTa[:,0], CTa[:,1], CTa[:,2], color='g',alpha=0.6, marker='o') <br>
ax.plot(DTa[:,0], DTa[:,1], DTa[:,2], color='g',alpha=0.6, marker='o') <br>


// rotational in z <br>
theta=np.pi*2/3 <br>
cs=np.cos(theta) <br>
ss=np.sin(theta) <br>

T_rz = np.array([[cs, ss, 0, 0], [-ss, cs, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) <br>
T_rx = np.array([[1, 0, 0, 0],[0, cs, ss, 0], [0, -ss, cs, 0], [0, 0, 0, 1]]) <br>
T_ry = np.array([[cs, 0 -ss, 0], [0, 1, 0, 0], [ss, 0, cs, 0], [0, 0, 0, 1]]) <br>

AT_rz = T_rz @ Anew.T <br>
ATrz=AT_rz[:-1,:].T <br>

BT_rz = T_rz @ Bnew.T <br>
BTrz=BT_rz[:-1,:].T <br>

CT_rz = T_rz @ Cnew.T <br>
CTrz=CT_rz[:-1,:].T <br>

DT_rz = T_rz @ Dnew.T <br>
DTrz=DT_rz[:-1,:].T <br>

ax.plot(ATrz[:,0], ATrz[:,1], ATrz[:,2], color='b',alpha=0.6, marker='o') <br>
ax.plot(BTrz[:,0], BTrz[:,1], BTrz[:,2], color='b',alpha=0.6, marker='o') <br>
ax.plot(CTrz[:,0], CTrz[:,1], CTrz[:,2], color='b',alpha=0.6, marker='o') <br>
ax.plot(DTrz[:,0], DTrz[:,1], DTrz[:,2], color='b',alpha=0.6, marker='o') <br>


// shearing <br>
b= -0.85 <br>
c= 0.25 <br>
d= -0.75 <br>
f= 0.7 <br>
g= 0.5 <br>
i= 1 <br>
T_sh = np.array([[1, d, g, 0], [b, 1, i, 0], [c, f, 1, 0], [0, 0, 0, 1]]) <br>

AT_sh = T_sh @ Anew.T <br>
ATsh=AT_sh[:-1,:].T <br>

BT_sh = T_sh @ Bnew.T <br>
BTsh=BT_sh[:-1,:].T <br>

CT_sh = T_sh @ Cnew.T <br>
CTsh=CT_sh[:-1,:].T <br>

DT_sh = T_sh @ Dnew.T <br>
DTsh=DT_sh[:-1,:].T <br>

ax.plot(ATsh[:,0], ATsh[:,1], ATsh[:,2], color='c',alpha=0.6, marker='o') <br>
ax.plot(BTsh[:,0], BTsh[:,1], BTsh[:,2], color='c',alpha=0.6, marker='o') <br>
ax.plot(CTsh[:,0], CTsh[:,1], CTsh[:,2], color='c',alpha=0.6, marker='o') <br>
ax.plot(DTsh[:,0], DTsh[:,1], DTsh[:,2], color='c',alpha=0.6, marker='o') <br>

plt.show() 
