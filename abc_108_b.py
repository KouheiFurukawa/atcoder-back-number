from sys import stdin
import numpy as np

A = np.array([int(x) for x in stdin.readline().rstrip().split()])
B = np.reshape(A, (2, 2))
vector = np.array(B[1] - B[0])
print(
    str((B[1] - np.array([vector[1], -vector[0]]))[0]) + ' ' + str((B[1] - np.array([vector[1], -vector[0]]))[1])
    + ' ' + str((B[0] - np.array([vector[1], -vector[0]]))[0]) + ' ' + str((B[0] - np.array([vector[1], -vector[0]]))[1])
)

