#!/usr/bin/env python3


# Programmer: Jacob Gray
# Last Edit: 5/16/2020


import numpy as np

tf_valid = np.array([
    [0, 0, -1, 4],
    [0, 1, 0, 2.4],
    [1, 0, 0, 3],
    [0, 0, 0, 1]
])

array_b = np.array([4, 5, 6])

array_c = ([[1, 4, 3], [1, 5, 5]])  # 2-D array

zero_array = np.zeros((10, 2))  # 10-row 2-column array of all zeros

identity_array = np.identity(5)  # A 5-row 5-column identity matrix

np.random.uniform(5, 10, size=(100, 3))  # Returns a uniform 100-row 3-column array of values 5-10

np.linspace(0, 1, 100)  # Returns an array of 100 instances of values from 0-1 evenly spaced. Endpoint inclusive.

array = np.array([[1, -1], [2, -2], [3, -3]])
first_column = array[:, 0]
second_column = array[:, 1]
first_row = array[0, :]
second_row = array[1, :]

print(tf_valid[0, :])
print(np.shape(tf_valid))
