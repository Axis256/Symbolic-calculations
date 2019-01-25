from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def plot(expr, x, y, var1, var2):
    z = expr.substitute(x, y, var1, var2)
    ax = plt.axes(projection='3d')
    ax.contour3D(x, y, z, 40, cmap='binary')
    plt.show()
