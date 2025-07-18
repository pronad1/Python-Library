import numpy as np
from numpy.linalg import norm
#
# vector_row = np.array([[1, -5, 3, 2, 4]])
# vector_column = np.array([[1],
#                           [2],
#                           [3],
#                           [4]])
# print(vector_row.shape)
# print(vector_column.shape)
#
# new_vector=vector_row.T
# print(new_vector)
# norm_1=norm(new_vector,1)
# norm_2=norm(new_vector,2)
# norm_inf=norm(new_vector,np.inf)
# print('L_1 is : %.1F'%norm_1)
# print('L_2 is : %.1F'%norm_2)
# print('L_3 is : %.1F'%norm_inf)
#
#
# #  compute the angle between the vector
#
# from numpy import arccos, dot
# v=np.array([[10,9,3]])
# w=np.array([[2,5,12]])
# theta=\
#     arccos(dot(v,w.T)/(norm(v)*norm(w)))
# print('Angle between the vector v and w is :- ',theta)
#
#
# # compute the cross product of v and w
# print('Cross product between vector v and w is :- ',np.cross(v,w))
#
# # compute the matrix product of P and Q. Show that the product of Q and P will product an error
# p=np.array([[1,4],[2,5],[3,6]])
# q=np.array([[2,4,6,9],[3,5,7,8]])
# print(p)
# print(q)
# print(np.dot(p,q))
# np.dot(q,p)

# use the np.eye function to produce a 4 x 4 identity matrix, I. Multiply M by I to show that the result is M.
from numpy.linalg import det
m=np.array([[0,2,1,3],
             [3,2,8,1],
             [1,0,0,3],
             [0,3,2,1]])
print('M:\n',m,'\n')
print('Determinant: %.1f'%det(m))
I=np.eye(4)
print('I:\n',I,'\n')
print('M*I:\n',np.dot(m,I))



# The matrix M has a nonzero determinant. Compute the inverse of M. Show that the matrix
# P=[[0,1,0],[0,0,0],[1,0,1]] has a determinant value of 0 and therefore has no inverse

from numpy.linalg import inv

print('Inv M:\n', inv(m))
p=np.array([[0,1,0],
            [0,0,0],
            [1,0,1]])
print('det(p):\n',det(p))



# Matrix A=[[1,1,0],[0,1,0],[1,0,1]]
# , compute the condition number and rank for this matrix. If y=[[1],[2],[1]]
# , get the augmented matrix [A, y].

from numpy.linalg import \
    cond, matrix_rank
a= np.array([[1,1,0],
             [0,1,0],
             [1,0,1]])
print('Condition number:\n',cond(a))
print('Rank:\n',matrix_rank(a))
y=np.array([[1],[2],[1]])
ay=np.concatenate((a,y),axis=1)
print('Augmented matrix:\n',ay)



