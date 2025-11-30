from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.animation import FuncAnimation
import index

def visualize(bounds: tuple[float, float], objfunc: Callable) -> None:
    """Visualize SGA.
    """
    x = np.linspace(bounds[0], bounds[1], 400)
    y = np.linspace(bounds[0], bounds[1], 400)
    
    X, Y = np.meshgrid(x, y)
    # X, Y = np.meshgrid(np.linspace(-2, 2, 200), np.linspace(-1, 3, 200))
    Z = objfunc(X, Y)
    # Z = np.minimum(Z, 1000000000)  # everything above 500 is capped


    fig, ax = plt.subplots()

    img = ax.imshow(
        Z,
        extent=[x.min(), x.max(), y.min(), y.max()],
        origin="lower",
        cmap="viridis",     # "viridis", "hot"
        norm=LogNorm(vmin=max(Z.min(), 1e-8), vmax=Z.max())   # avoid log(0), scale heatmap logarithmatically
    )
    
    # Contour lines
    # levels = 20
    # levels = np.logspace(np.log10(Z.min()), np.log10(Z.max()), 8)   # int determines the number of contour lines
    # ax.contour(
    #     X, Y, Z,
    #     levels=levels,        # number of contour levels (set it to 'levels' for logarithmatic contours)
    #     colors='white',       # or 'black', depending on visibility
    #     linewidths=0.5
    # )

    fig.colorbar(img, ax=ax, label="f(x, y)")
    ax.set_title("Heatmap of f(x, y)")

    scat = ax.scatter([], [], c='red', s=50)
    def update(_):
        pts = np.array([[ind["x"], ind["y"]] for ind in index.index["pop"]], float)
        if pts.size == 0:
            return scat,
        scat.set_offsets(pts)
        return scat,

    ani = FuncAnimation(fig, update, interval=50)  # animate refresh every 0.05 second

    # Start SGA
    index.index["lock"].set()
    
    plt.show()

# http://www.geatbx.com/docu/fcnindex-01.html#P89_3085