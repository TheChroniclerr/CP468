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
    # X, Y = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-1, 3, 200))
    Z = objfunc(X, Y)
    # Z = np.minimum(Z, 1000000000)  # everything above 500 is capped

    fig, ax = plt.subplots()

    plt.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin="lower", cmap="viridis")
    # plt.imshow(np.log1p(Z), extent=(-2, 2, -1, 3), origin='lower', cmap='hot')
    plt.colorbar(label="f(x, y)")
    plt.title("Heatmap of f(x, y)")

    scat = ax.scatter([], [], color='red', s=50)

    def update(_):
        points = [[ind["x"], ind["y"]] for ind in index.index["pop"]]
        # print(points)
        scat.set_offsets(points)
        return scat,

    ani = FuncAnimation(fig, update, interval=50)  # animate refresh every 0.1 second

    # Start SGA
    index.index["lock"].set()
    
    plt.show()

# http://www.geatbx.com/docu/fcnindex-01.html#P89_3085