import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# function to get random starting point
def random_point_tetra(vertices):
    s, t, u = np.random.rand(3)
    if s + t + u > 1:
        s, t, u = 1 - s, 1 - t, 1 - u  # reflect into tetrahedron
    v0, v1, v2, v3 = vertices
    point = v0 + s*(v1 - v0) + t*(v2 - v0) + u*(v3 - v0)
    return point

# build vertices for tetrahedron centered at (0,0,0)
def build_vertices():
    vertices = np.array([
        [1,  1,  1],
        [1, -1, -1],
        [-1, 1, -1],
        [-1,-1,  1]
    ], dtype=float)

    return vertices

# chaos game iteration
def chaos_iter(r, N, x, vertices):

    points = []
    labels = []

    # chaos game iteration
    for _ in range(N):
        # choose random vertex
        idx = np.random.randint(0,4)
        v = vertices[idx]
        # move a fraction r toward the vertex
        x = x + r * (v - x)
        # save x and label
        points.append(x.copy())
        labels.append(idx)

    points = np.array(points)
    labels = np.array(labels)

    return points, labels

# main function
def main():
    # params for chaos game
    r = 0.5 # ratio for tetrahedron
    N = 20000 # number of points
    vertices = build_vertices()
    x = random_point_tetra(vertices) # random starting point

    points, labels = chaos_iter(r, N, x, vertices)

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

    plt.savefig("/Users/emmasandidge/projects25/3D-Chaos-Game/fractal_images/tetra.png")
    plt.show()

if __name__=='__main__':
    main()