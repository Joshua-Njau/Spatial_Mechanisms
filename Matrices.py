'''
conventions used:
    c - cosine
    s - sine
    t - translation
    x, y, z - operations about x, y and axis respectively
    cx, cy, cz - coincide with x, y and z axis respectively
    xy, xz, yz - operation for xy, xz and yz plane respectively
    R - rotation
    P - plane

'''

import numpy as np

theta = 45
c, s = np.cos(theta), np.sin(theta)
method = 1

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

step1 = np.array([
    [-point1[0, 0]],
    [-point1[1, 0]],
    [-point1[2, 0]],
    [0]
])

t_matrix = np.array([
    [1, 0, 0, point1[0, 0]],
    [0, 1, 0, point1[1, 0]],
    [0, 0, 1, point1[2, 0]],
    [0, 0, 0, 1]
])

#Causing one point to coincide with origin
origin = point1 + step1
#Translating 2nd part by same magnitude
hang = point2 + step1

print(origin)
print(hang)

match method:
    case 1:
#rotation for vector to lie on xy plane
#have it about the x axis
        c_x = hang[1, 0]/numpy.sqrt(numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))
        s_x = hang[2, 0]/numpy.sqrt(numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))

        P_xy = np.array([
            [1, 0, 0, 0],
            [0, c_x, -s_x, 0],
            [0, s_x, c_x, 0],
            [0, 0, 0, 1]
        ])
        #have vector coincide with y axis
        #rotates about z axis
        c_cz = hang[1, 0]/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))
        s_cz = numpy.sqrt(numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))

        R_cz = np.array([
            [c_cz, -s_cz, 0, 0],
            [s_cz, c_cz, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        #rotate about y axis
        Ry = np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ])

        #reversing (cos remains same, sin change sign)
        R_cz_r = np.array([
            [c_cz, s_cz, 0, 0],
            [-s_cz, c_cz, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        P_xy_r = np.array([
            [1, 0, 0, 0],
            [0, c_x, s_x, 0],
            [0, -s_x, c_x, 0],
            [0, 0, 0, 1]
        ])
    
    case 2:
        #rotation for vector to lie on xz plane
        #have it about the z axis
        c_z = hang[0, 0]/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0]))
        s_z = hang[1, 0]/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0]))

        P_xz = np.array([
            [c_z, -s_z, 0, 0],
            [s_z, c_z, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        #have vector coincide with x axis
        #rotates about y axis
        c_cy = hang[2, 0]/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))
        s_cy = numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0]))/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))

        R_cy = np.array([
            [c_cy, 0, s_cy, 0],
            [0, 1, 0, 0],
            [-s_cy, 0, c_cy, 0],
            [0, 0, 0, 1]
        ])

        #rotate about x axis
        Rx = np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ])
       
        #reversing (cos remains same, sin change sign)
        R_cy_r = np.array([
            [c_cy, 0, -s_cy, 0],
            [0, 1, 0, 0],
            [s_cy, 0, c_cy, 0],
            [0, 0, 0, 1]
        ])

        P_xz_r = np.array([
            [c_z, s_z, 0, 0],
            [-s_z, c_z, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    
    case 3:
        #rotation for vector to lie on yz plane
        #have it about the y axis
        c_y = hang[2, 0]/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[2, 0]))
        s_y = hang[0, 0]/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[2, 0]))

        P_yz = np.array([
            [c_y, 0, s_y, 0],
            [0, 1, 0, 0],
            [-s_y, 0, c_y, 0],
            [0, 0, 0, 1]
        ])

        #have vector coincide with z axis
        #rotates about x axis
        c_cx = hang[1, 0]/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))
        s_cx = numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[2, 0]))/numpy.sqrt(numpy.square(hang[0, 0])+numpy.square(hang[1, 0])+numpy.square(hang[2, 0]))

        R_cx = np.array([
            [1, 0, 0, 0],
            [0, c_cx, -s_cx, 0],
            [0, s_cx, c_cx, 0],
            [0, 0, 0, 1]
        ])

        #rotate about z axis
        Rz = np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        #reversing (cos remains same, sin change sign)
        R_cx_r = np.array([
            [1, 0, 0, 0],
            [0, c_cx, s_cx, 0],
            [0, -s_cx, c_cx, 0],
            [0, 0, 0, 1]
        ])

        P_yz_r = np.array([
            [c_y, 0, -s_y, 0],
            [0, 1, 0, 0],
            [s_y, 0, c_y, 0],
            [0, 0, 0, 1]
        ])

