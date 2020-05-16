#!/usr/bin/env python3


# ME499-S20 Python Lab 6
# Programmer: Jacob Gray
# Last Edit: 5/16/2020


import numpy as np


def numpy_close(array_a, array_b, tol=1e-8):
    """
    This function will return True if the arrays have the same shape, and the absolute difference of each
    corresponding pair of elements is less than tol.
    :param array_a: Numpy array.
    :param array_b: Numpy array.
    :param tol: Difference tolerance.
    :return: True or None
    """

    if array_a.size == array_b.size and (np.absolute(array_a - array_b) < tol).all():
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

    if start > end:
        return ValueError
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

    return np.random.uniform(1*num_rolls, 6*num_rolls, size=(1, iterations))


if __name__ == '__main__':
    array_a = np.array([3, 4])
    array_b = np.array([4, 3])
    print(numpy_close(array_a, array_b))

    # my_func = lambda x: x ** 2
    # print(simple_minimizer(my_func, -1.75, 2.25, num=5))  # Should return (0.25, 0.0625)
