import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

# function to get random starting point
def random_point_dodeca(vertices):
    # get smallest convex shape containing vertices
    hull = ConvexHull(vertices)
    min_corner = vertices.min(axis=0)
    max_corner = vertices.max(axis=0)
    
    while True:
        p = np.random.uniform(min_corner, max_corner)
        # check if point is in dodeca using plane equations
        if all(np.dot(eq[:3], p) + eq[3] <= 1e-12 for eq in hull.equations):
            return p

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
x = random_point_dodeca(vertices) # starting point

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

# save figure
plt.savefig("/Users/emmasandidge/projects25/appliedLA_fall25/dodeca.png")
plt.show()