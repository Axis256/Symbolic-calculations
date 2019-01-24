from expression import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np


def plot(expr, X, Y, var1, var2):
    Z = expr.substitute(X, Y, var1, var2)
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 40, cmap='binary')
    plt.show()
