import numpy as np
from pandas import array


def sorting(myarray: array) -> array:
    return np.sort(myarray)


print(sorting(np.array([2, 5, 2, 6, 78, 5, 3, 3, 5, 7, 5, 23, 2, 5, 7])))
