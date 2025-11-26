from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import index

def visualize(bounds: list, objfunc: Callable) -> None:
    """Visualize SGA.
    """
    x = np.linspace(bounds[0], bounds[1], 400)
    y = np.linspace(bounds[0], bounds[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = objfunc(X, Y)

    fig, ax = plt.subplots()

    plt.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin="lower", cmap="viridis")
    plt.colorbar(label="f(x, y)")
    plt.title("Heatmap of f(x, y)")

    scat = ax.scatter([], [], color='red', s=50)

    def update(_):
        points = [[ind["x"], ind["y"]] for ind in index.index["pop"]]
        print(points)
        scat.set_offsets(points)
        return scat,

    ani = FuncAnimation(fig, update, interval=100)  # animate refresh every 0.1 second

    # Start SGA
    index.index["lock"].set()
    
    plt.show()

# http://www.geatbx.com/docu/fcnindex-01.html#P89_3085