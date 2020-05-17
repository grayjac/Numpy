#!/usr/bin/env python3


# ME499-S20 Python Lab 6
# Programmer: Jacob Gray
# Last Edit: 5/16/2020


import numpy as np
from matplotlib import pyplot as plt
from numbers import Number


def numpy_close(array_a, array_b, tol=1e-8):
    """
    This function will return True if the arrays have the same shape, and the absolute difference of each
    corresponding pair of elements is less than tol.
    :param array_a: Numpy array.
    :param array_b: Numpy array.
    :param tol: Difference tolerance.
    :return: True or None
    """

    if array_a.shape == array_b.shape and np.all(np.absolute(array_a - array_b) < tol):
        return True
    else:
        return False


def simple_minimizer(func, start, end, num=100):
    """
    This function takes a function and returns the index and local minimum value of that function within the
    given start and end bounds.

    :param func: Reference 1-D function, should also work on numpy array.
    :param start: Starting bound which to search for a minimum (inclusive).
    :param end: Ending bound which to search for a minimum (inclusive).
    :param num: Number of spacings withing the bounds.
    :return: Even integer. Index (x-coord) and value of local min of func within given bounds.
    """

    if start >= end:
        return ValueError("Your start value should be greater than your end value")
    else:
        x_values = np.linspace(start, end, num)
        y_values = func(x_values)

        return x_values[np.argmin(y_values)], np.min(y_values)


def simulate_dice_rolls(num_rolls, iterations):
    """
    This function takes a number of dice rolls and number of iterations and returns 1-D Numpy array of length
    iterations, where each item is the sum of throwing a 6-sided die num_rolls times.
    :param num_rolls:
    :param iterations:
    :return:
    """

    iteration_array = np.random.randint(1 * num_rolls, (6 * num_rolls) + 1, size=iterations)

    plt.hist(iteration_array)
    plt.title('dice_{}_rolls{} Plot'.format(num_rolls, iterations))
    plt.ylabel('Number of instances')
    plt.xlabel('Sum of num_rolls')
    plt.savefig('dice_{}_rolls_{}'.format(num_rolls, iterations))

    return iteration_array


def is_transformation_matrix(np_array):
    """
    This function takes a 4x4 array and returns True if it's a valid transformation matrix, and False otherwise.
    :param np_array: 4x4 numpy array.
    :return: True or False.
    """

    rotation = np_array[0:3, 0:3]

    if not isinstance(np_array, np.ndarray) and np_array.shape == (4, 4):
        return TypeError("Must input a 4x4 Numpy array!")
    else:
        if np.all(np.equal(np.int_(rotation.T @ rotation), np.identity(3))):
            return True
        else:
            return False


def nearest_neighbors(np_array, point, dist):
    """
    Calculates and returns an MxD numpy array of all points within Euclidean distance "dist" of "point".
    :param np_array: NxD Numpy array.
    :param point: 1xD Numpy array.
    :param dist: Distance threshold of any positive number.
    :return: MxD Numpy array.
    """

    rows = np_array.reshape(1, np.size(np_array[0, :]), -1)  # Converting NxD array into N number of 1xD arrays
    distance = np.linalg.norm(point - rows)

    if not isinstance(dist, Number) and dist > 0:
        raise ValueError
    else:
        return


if __name__ == '__main__':
    array_a = np.array([3, 4])
    array_b = np.array([4, 3])
    tf_valid = np.array([
        [0, 0, -1, 4],
        [0, 1, 0, 2.4],
        [1, 0, 0, 3],
        [0, 0, 0, 1]
    ])

    tf_invalid = np.array([
        [1, 2, 3, 1],
        [0, 1, -3, 4],
        [0, 1, 1, 1],
        [-0.5, 4, 0, 2]
    ])

    test_array = np.array([[0.70711, 0.35698, 0.61038, 6.43467],
                           [0.70711, -0.35698, -0.61038, 6.43467],
                           [0., 0.86321, -0.50485, 4.],
                           [0., 0., 0., 1.]])

    np_array = np.arange(9).reshape(3, 3)
    print(np_array)
    rows = np_array.reshape(1, np.size(np_array[0, :]), -1)
    print(np_array[np_array[:, 0] > 3])
    print(np.all(np_array > 0.5, axis=1))
