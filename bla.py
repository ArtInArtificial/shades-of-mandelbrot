import random as rd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from math import sqrt

sin60 = sqrt(3)/2

xdata = [0, 0.5, 1, 0]
ydata = [0, sin60, 0, 0]

def break_line(pos, xdata, ydata):
    """
    Breaks a line and form the next spike in a Koch iteration
    the line is represented by its ends x/ydata[pos,pos+1]
    """
    x0 = xdata[pos]
    x1 = xdata[pos+1]
    y0 = ydata[pos]
    y1 = ydata[pos+1]
    xvec = x1 - x0
    yvec = y1 - y0

    xdata.insert(pos+1, x0 + xvec/3)
    ydata.insert(pos+1, y0 + yvec/3)

    xdata.insert(pos+2, x0 + xvec/2 - yvec*sin60/3)
    ydata.insert(pos+2, y0 + xvec*sin60/3 + yvec/2)

    xdata.insert(pos+3, x0 + 2*xvec/3)
    ydata.insert(pos+3, y0 + 2*yvec/3)


def koch_iteration(xdata, ydata):
    """
    Breaks the (n-1) lines in a xdata of length n by calling break_line()
    """
    pos = 0
    while pos < len(xdata) - 1:
        break_line(pos, xdata, ydata)
        pos += 4

fig, ax = plt.subplots()
ax.axis('equal')
ax.axis('off')
ax.axes.set_xlim(-0.5,1.5)
ax.axes.set_ylim(-1, 1)
fig.tight_layout()
plt.savefig("frame_0.png", dpi = 500, format="png")
for i in range(1,9):
    koch_iteration(xdata, ydata)
    ax.plot(xdata, ydata)
plt.show()