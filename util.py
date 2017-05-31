import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import Image
import os


# Given:
#   (m x n) matrix A
#   A's (m x l) range approximator Q
# Returns:
#   || A - QQ*A || / || A ||
def deviation(A, Q):
    Q = np.matrix(Q)
    return la.norm(A - np.dot(np.dot(Q, Q.H), A)) / la.norm(A)

# Returns:
#   A test image as a numpy matrix.
def get_img(choice=None):
    imgs = [name for name in os.listdir(os.curdir + '/images')]

    img = Image.open('images/4.jpg')
    img.load()
    r_d = np.asarray(img, dtype='int32')

    # convert each entry from [r, g, b] to single integer
    mat = [[ (r_d[r][c][0] << 16) + (r_d[r][c][1] << 8) + r_d[r][c][2] for c in range(len(r_d[0])) ] for r in range(len(r_d))]
    return np.matrix(mat), r_d


def show_images(A, Q):
    f = plt.figure()
    plt.imshow(A)
    f.show()

    g = plt.figure()
    plt.imshow(Q)
    g.show()

    #raw_input()

# Avg. value in array
def avg(A):
    A = np.array(A)
    t = [i for i in np.ndarray.flatten(A)]
    return sum(t) / len(t)

# Change vector B to be orthoganal to vector A (via Gram-Schmidt)
def orthog(A, B):
    pass
