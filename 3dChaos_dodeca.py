import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# golden ratio
phi = 0.5 * (1 + np.sqrt(5))

# initialize dodecahedron centered at (0,0,0)
vertices = np.array([
    # cube vertices w/ +/- 1
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [-1, 1, 1],
    [-1, -1, 1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1,-1, -1],
    # remaining 12 vertices
    [ 0,  1/phi,  phi],
    [ 0,  1/phi, -phi],
    [ 0, -1/phi,  phi],
    [ 0, -1/phi, -phi],
    [ 1/phi,  phi,  0],
    [ 1/phi, -phi,  0],
    [-1/phi,  phi,  0],
    [-1/phi, -phi,  0],
    [ phi,  0,  1/phi],
    [ phi,  0, -1/phi],
    [-phi,  0,  1/phi],
    [-phi,  0, -1/phi]
], dtype=float)

# params for chaos game
r = 0.72 # ratio for dodecahedron
N = 30000 # number of points
x = np.array([0.0, 0.0, 0.0])  # starting point

points = []
labels = []

# chaos game iteration
for _ in range(N):
    # choose random vertex
    idx = np.random.randint(0,20)
    v = vertices[idx]
    # move a fraction r toward the vertex
    x = x + r * (v - x)
    # save x and label
    points.append(x.copy())
    labels.append(idx)

points = np.array(points)
labels = np.array(labels)

# define colors for plotting
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown', 'pink',        
    'lime', 'teal', 'navy', 'maroon', 'gold', 'violet', 'gray', 'olive', 'deeppink']

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