import numpy as np

mat = np.array([[2,-5,-11,0],[-9,4,6,13],[4,7,12,-2]])
print(mat)
mat1 = np.array([[1,2],[3,4]])
mat.transpose()
print(mat1)

A = np.array([[1,2],[3,4]])
A.trace() #5

B = np.array([[1,2],[3,4]])
C = np.array([[5,6],[7,8]])
print(B@C)