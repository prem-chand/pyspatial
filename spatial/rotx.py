import numpy as np


def rotx(theta):
    """
    rotx  spatial coordinate transform (X-axis rotation).
    rotx(theta) calculates the coordinate transform matrix from A to B
    coordinates for spatial motion vectors, where coordinate frame B is
    rotated by an angle theta (radians) relative to frame A about their
    common X axis.
    """
    if isinstance(theta, np.ndarray):
        theta = theta.item()

    c = np.cos(theta)
    s = np.sin(theta)

    X = np.array([[1,  0,  0,  0,  0,  0],
                  [0,  c,  s,  0,  0,  0],
                  [0, -s,  c,  0,  0,  0],
                  [0,  0,  0,  1,  0,  0],
                  [0,  0,  0,  0,  c,  s],
                  [0,  0,  0,  0, -s,  c]])
    return X
