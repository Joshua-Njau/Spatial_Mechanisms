'''
conventions used:
    t - translation
    c - coincide
    R - rotation
    P - plane
    r - reverse
'''

import numpy as np

np.set_printoptions(suppress=True, precision=9)

theta = np.deg2rad(30)
cos, sin = np.cos(theta), np.sin(theta)

M = np.array([
    [0, 2, 2, 0],
    [0, 0, 2, 2],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
])

#point1 and point2 are points on the vector about which rotaion is to occur
point1 = np.array([
    [0],
    [2],
    [2],
    [1]
])
point2 = np.array([
    [1],
    [4],
    [6],
    [1]
])

#Translation matrix to make point 1 coincide with origin
t_matrix = np.array([
    [1, 0, 0, -point1[0, 0]], 
    [0, 1, 0, -point1[1, 0]], 
    [0, 0, 1, -point1[2, 0]], 
    [0, 0, 0, 1]
])

t_matrix_r = np.linalg.inv(t_matrix)

#Causing one point to coincide with origin
origin = t_matrix@point1
#Translating 2nd part by same magnitude
hang = t_matrix@point2

'''There are 12 possible ways the 7-step method can be done.
We shall have 3 outlined here'''
class Method1:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotate(self):
        #rotation for vector to lie on xy plane
        #have it about the x axis
        cos1 = hang[1, 0]/np.sqrt(np.square(hang[1, 0])+np.square(hang[2, 0]))
        sin1 = hang[2, 0]/np.sqrt(np.square(hang[1, 0])+np.square(hang[2, 0]))

        #rotation is in clockwise direction
        P_align = np.array([
            [1, 0, 0, 0],
            [0, cos1, sin1, 0],
            [0, -sin1, cos1, 0],
            [0, 0, 0, 1]
        ])

        #have vector coincide with y axis
        #rotates about z axis
        cos2 = np.sqrt(np.square(hang[1, 0])+np.square(hang[2, 0]))/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0])+np.square(hang[2, 0]))
        sin2 = hang[0, 0]/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0])+np.square(hang[2, 0]))

        R_c = np.array([
            [cos2, -sin2, 0, 0],
            [sin2, cos2, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        #rotate about y axis
        Ry = np.array([
            [cos, 0, sin, 0],
            [0, 1, 0, 0],
            [-sin, 0, cos, 0],
            [0, 0, 0, 1]
        ])

        #reversing (cos remains same, sin change sign)
        R_c_r = np.linalg.inv(R_c)

        P_align_r = np.linalg.inv(P_align)

        return t_matrix_r@P_align_r@R_c_r@Ry@R_c@P_align@t_matrix@self.matrix

class Method2:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotate(self):
        #rotation for vector to lie on xz plane
        #have it about the z axis
        cos1 = hang[0, 0]/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0]))
        sin1 = hang[1, 0]/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0]))

        #rotation is in clockwise direction
        P_align = np.array([
            [cos1, sin1, 0, 0],
            [-sin1, cos1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        #have vector coincide with x axis
        #rotates about y axis
        cos2 = np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0]))/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0])+np.square(hang[2, 0]))
        sin2 = hang[2, 0]/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0])+np.square(hang[2, 0]))

        R_c = np.array([
            [cos2, 0, sin2, 0],
            [0, 1, 0, 0],
            [-sin2, 0, cos2, 0],
            [0, 0, 0, 1]
        ])

        #rotate about x axis
        Rx = np.array([
            [1, 0, 0, 0],
            [0, cos, -sin, 0],
            [0, sin, cos, 0],
            [0, 0, 0, 1]
        ])

        #reversing (cos remains same, sin change sign)
        R_c_r = np.linalg.inv(R_c)

        P_align_r = np.linalg.inv(P_aign)

        return t_matrix_r@P_align_r@R_c_r@Rx@R_c@P_align@t_matrix@self.matrix

class Method3:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotate(self):    
        #rotation for vector to lie on yz plane
        #have it about the y axis
        cos1 = hang[2, 0]/np.sqrt(np.square(hang[0, 0])+np.square(hang[2, 0]))
        sin1 = hang[0, 0]/np.sqrt(np.square(hang[0, 0])+np.square(hang[2, 0]))

        #rotation is in clockwise direction
        P_align = np.array([
            [cos1, 0, -sin1, 0],
            [0, 1, 0, 0],
            [sin1, 0, cos1, 0],
            [0, 0, 0, 1]
        ])

        #have vector coincide with z axis
        #rotates about x axis
        cos2 = np.sqrt(np.square(hang[0, 0])+np.square(hang[2, 0]))/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0])+np.square(hang[2, 0]))
        sin2 = hang[1, 0]/np.sqrt(np.square(hang[0, 0])+np.square(hang[1, 0])+np.square(hang[2, 0]))

        R_c = np.array([
            [1, 0, 0, 0],
            [0, cos2, -sin2, 0],
            [0, sin2, cos2, 0],
            [0, 0, 0, 1]
        ])

        #rotate about z axis
        Rz = np.array([
            [cos, -sin, 0, 0],
            [sin, cos, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        #reversing (cos remains same, sin change sign)
        R_c_r = np.linalg.inv(R_c)

        P_align_r = np.linalg.inv(P_align)

        return t_matrix_r@P_align_r@R_c_r@Rz@R_c@P_align@t_matrix@self.matrix

first = Method1(M)
print(first.rotate())
first1 = Method2(M)
print(first.rotate())
first2 = Method3(M)
print(first.rotate())