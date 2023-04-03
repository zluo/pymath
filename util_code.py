import numpy as np
from matplotlib import pyplot as plt

def draw_arrow(plt, start, end, c='red'):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    plt.arrow(start[0], start[1], dx, dy, head_width=0.1, head_length=0.3, length_includes_head=True, color= c)

def show(plt):
    plt.grid()
    plt.show()

draw_vector = draw_arrow


def dino_vectors():
    _dino_vectors = np.array([(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1),(6,4)])
    return _dino_vectors





print('loading util code ...')
