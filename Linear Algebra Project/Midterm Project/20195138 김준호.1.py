import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import scipy.linalg as sl

A = np.matrix([[40,10,10,10,10,10,10,10,10,20],[40,0,0,0,0,0,0,0,0,20],
             [40,0,0,0,0,0,0,0,0,20],[40,0,0,0,0,0,0,0,0,20],
             [40,0,0,0,0,0,0,0,0,20],[40,0,0,0,0,0,0,0,0,20],
             [40,0,0,0,0,0,0,0,0,20],[40,0,0,0,0,0,0,0,0,20],
             [40,0,0,0,0,0,0,0,0,20],[40,30,30,30,30,30,30,30,30,20]])
plt.imshow(A)
plt.colorbar()
plt.show()

