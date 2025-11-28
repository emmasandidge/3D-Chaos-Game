import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# initialize tetrahedron centered at (0,0,0)
vertices = np.array([
    [1,  1,  1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1,-1,  1]
], dtype=float)

# params for chaos game
r = 0.5 # ratio for tetrahedron
N = 20000 # number of points
x = np.array([0.0, 0.0, 0.0])  # starting point

points = []
labels = []

# chaos game iteration
for _ in range(N):
    # choose random vertex
    idx = np.random.randint(0,4)
    #v = vertices[np.random.randint(0, 4)]
    v = vertices[idx]
    # move a fraction r toward the vertex
    x = x + r * (v - x)
    # save x and label
    points.append(x.copy())
    labels.append(idx)

points = np.array(points)
labels = np.array(labels)

# define colors for plotting
colors = ['red', 'green', 'blue', 'magenta']
point_colors = [colors[i] for i in labels]

# plotting 3D fractal
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(points[:,0], points[:,1], points[:,2], c=point_colors, s=0.5)

# plot vertices
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], color='black', s=60)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()