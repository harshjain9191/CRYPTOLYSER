import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from itertools import count
import random


def plotLive():

    x_axis = range(1,31,1)
    plt.plot(x_axis, y_axis)
    index = count()
    def animate(i):
        y_axis.pop(0)
        y_axis.append(random.randint(1,4))
        time.sleep(1)
        plt.cla()
        plt.plot(x_axis, y_axis)



anim = FuncAnimation(plt.gcf(), animate, 3000)
plt.tight_layout()
plt.show()

