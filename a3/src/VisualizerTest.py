# import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import index

def f(x, y):
    return x**2 + y**2

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# plt.ion()
fig, ax = plt.subplots()

plt.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin="lower", cmap="viridis")
plt.colorbar(label="f(x, y)")
plt.title("Heatmap of f(x, y)")
# plt.ioff()
# time.sleep(2)

# Keep track of points
points = []
scat = ax.scatter([], [], color='red', s=50)

def update(_):
    # Add one random point
    points.append([np.random.uniform(-5, 5), np.random.uniform(-5, 5)])
    scat.set_offsets(points)
    return scat,

# Animate every 5000 ms (5 seconds)
ani = FuncAnimation(fig, update, interval=100)  # refresh every 0.1 second

plt.show()

# http://www.geatbx.com/docu/fcnindex-01.html#P89_3085