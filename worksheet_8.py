#  sagar aggarwal=========================
# QUESTION 1: POINT CLASS
# =========================

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

A = Point(1, 2)
B = Point(4, 6)
C = Point(3, 1)

distance = math.sqrt((B.x - A.x)**2 + (B.y - A.y)**2)
print("Distance:", distance)

mid_x = (A.x + B.x) / 2
mid_y = (A.y + B.y) / 2
print("Midpoint:", (mid_x, mid_y))

slope = (B.y - A.y) / (B.x - A.x)
intercept = A.y - slope * A.x
print("Line Equation: y =", slope, "x +", intercept)

a = slope
b = -1
c = intercept
d = (a*C.x + b*C.y + c) / (a*a + b*b)
x_ref = C.x - 2*a*d
y_ref = C.y - 2*b*d
print("Reflection of C:", (x_ref, y_ref))


# =========================
# QUESTION 2: VECTORS
# =========================

import numpy as np

A_vec = np.array([2, 3])
B_vec = np.array([4, 1])
C_vec = np.array([1, 5])

R = A_vec + B_vec + C_vec
print("Resultant Vector:", R)

print("Magnitude A:", np.linalg.norm(A_vec))
print("Magnitude B:", np.linalg.norm(B_vec))
print("Magnitude C:", np.linalg.norm(C_vec))

print("A·B:", np.dot(A_vec, B_vec))
print("A·C:", np.dot(A_vec, C_vec))
print("B·C:", np.dot(B_vec, C_vec))

def angle(u, v):
    return np.degrees(np.arccos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))))

print("Angle A-B:", angle(A_vec, B_vec))
print("Angle A-C:", angle(A_vec, C_vec))
print("Angle B-C:", angle(B_vec, C_vec))

proj = (np.dot(A_vec, B_vec) / np.dot(B_vec, B_vec)) * B_vec
print("Projection of A on B:", proj)


# =========================
# QUESTION 3: SEGMENT
# =========================

S = np.array([1, 1])
E = np.array([5, 4])
P = np.array([3, 2])

segment_length = np.linalg.norm(E - S)
print("Segment Length:", segment_length)

t = np.dot(P - S, E - S) / np.dot(E - S, E - S)
t = max(0, min(1, t))
closest = S + t * (E - S)
print("Closest Point:", closest)

distance_point = np.linalg.norm(P - closest)
print("Distance from Point to Segment:", distance_point)


# =========================
# QUESTION 4: LINE INTERSECTION
# =========================

a1, b1, c1 = 2, -1, 3
a2, b2, c2 = 1, 1, 7

det = a1*b2 - a2*b1

if det != 0:
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    print("Intersection Point:", (x, y))
else:
    print("Lines are parallel or coincident.")
