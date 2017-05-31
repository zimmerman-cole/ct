import numpy as np
import numpy.linalg as la
import util

# Methods for finding low-rank approximation of matrices

# Everything here is based on pseudocode from
# "Finding structure with randomness: Probabilistic algorithms for
# constructing approximate matrix decompositions"
#       by N. Halko, P.G. Martinsson, and J.A. Tropp
# https://arxiv.org/pdf/0909.4061.pdf

# Given:
#   (m x n) matrix A,
#   target rank k,
#   oversampling parameter p.
# Returns:
#   an (m x (k + p)) matrix Q whose columns are orthonormal and whose range
#   approximates the range of A.
def fixed_rank(A, k, p):
    pass


# 4.1: RANDOMIZED RANGE FINDER
# Given:
#   (m x n) matrix A,
#   integer l
# Returns:
#   (m x l) matrix Q whose range approximates the range of A.
# See page 22 for pseudocode.
def rand_range_finder(A, l):
    m = len(A)
    n = len(A.T)

    om = np.random.randn(m, l)
    y = np.dot(A, om)
    q, _ = la.qr(y)

    return np.matrix(q)


# 4.2: ADAPTIVE RANDOMIZED RANGE FINDER
# Given:
#   m x n matrix A,
#   tolerance e (default: 5% of ||A||),
#   integer r (default: 10)
# Output:
#   An orthonormal matrix Q such that
#       || (I - QQ*)A || <= e
#   with probability at least 1 - min{m,n}10^-r.
def adap_rand_range_finder(A, e=None, r=None):
    m = len(A)
    n = len(A.T)
    if e == None:
        e = 0.05 * la.norm(A)
    if r == None:
        r = 10

    y = [np.dot(A, np.random.randn(n)).reshape(m, 1) for i in range(r)]
    Q = np.matrix(np.zeros((m, 1)))
    print(Q.shape, y[0].shape)
    Q[:, 0] = y[0]
    j = 0

    tolerance = e / (10*np.sqrt(2/np.pi))
    try:
        while max([la.norm(y[i]) for i in range(j+1, j+r)]) > tolerance:
            j += 1
            print('J: ============')
            print(j, util.deviation(A, Q))
            print(util.avg(A), util.avg(Q))

            y[j] = np.dot(np.identity(m) - np.dot(Q, Q.H), y[j])
            q = y[j] / la.norm(y[j])
            Q = np.append(Q, q, axis=1)

            y.append(np.dot(np.identity(m) - np.dot(Q, Q.H), np.dot(A, np.random.randn(n)) ).reshape(m, 1) )

            for i in range(j+1, j+r):
                y[i] = y[i] - (np.inner(q, y[i])/np.inner(q,q))*q


            if j > n:
                if np.inner(y[0], y[1]) == 0:
                    print('YES')
                else:
                    print('NO')
                raise

    except IndexError:
        print(j)
        raise

    return Q
