import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

list_var_points = (1, 5, 4, 9, 8, 2, 6, 5, 2, 1, 9, 7, 10)

fig, ax = plt.subplots()
xfixdata, yfixdata = 14, 8
xdata, ydata = 5, None
ln, = plt.plot([], [], 'ro-', animated=True)
plt.plot([xfixdata], [yfixdata], 'bo', ms=10)

def init():
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    return ln,

def update(frame):
    ydata = list_var_points[frame]
    ln.set_data([xfixdata,xdata], [yfixdata,ydata])
    return ln,          


ani = FuncAnimation(fig, update, frames=range(len(list_var_points)),
            init_func=init, blit=True)
plt.show()