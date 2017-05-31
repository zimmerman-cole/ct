# See this paper:

N. Halko, P.G. Martinsson and J.A. Tropp, _Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions_, 2009
    https://arxiv.org/abs/0909.4061

# Basic Idea:

1. Compute an approximate basis for the range of input matrix **A**. In other words, calculate a matrix **Q** such that:
     * **Q** has orthonormal columns.
     * **A** ~= **Q** **Q*** **A**
2. Use **Q** to help compute a standard factorization (QR, SVD, etc.) of **A**.
