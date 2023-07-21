import numpy as np
from matplotlib import pyplot as plt

# dinosaur demo points
dino_vectors = np.array([(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1),(6,4)])

# rotate vectors
def rotate(vectors, angle=45, o=(0,0)):
    v = to_polar_vector(vectors - o)
    v = v + (0, angle*np.pi/180)
    return from_polar_vector(v)


def to_polar_vector(vectors):
    distance = np.sqrt(vectors[:, 0]**2 + vectors[:, 1]**2)
    angles = np.arctan2(vectors[:, 1], vectors[:, 0])*180/np.pi
    return np.stack((distance, angles), axis=-1)


def from_polar_vector(polar_vectors):
   xs = polar_vectors[:, 0]*np.sin(polar_vectors[:, 1]*np.pi/180.0)
   ys = polar_vectors[:, 0]*np.cos(polar_vectors[:, 1]*np.pi/180.0)
   return np.stack((xs, ys), axis=-1)





# plotting wrappers
def draw_vector(start, end, c='red'):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    plt.arrow(start[0], start[1], dx, dy, head_width=0.1, head_length=0.3, length_includes_head=True, color= c)

def show():
    plt.grid()
    plt.show()

def plot(vectors, c=None):
    plt.plot(vectors[:, 0], vectors[:, 1], color=c)

def scatter(vectors):
    plt.scatter(vectors[:, 0], vectors[:, 1])

print('loading util code ...')
