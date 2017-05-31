# See this paper:

N. Halko, P.G. Martinsson and J.A. Tropp, _Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions_, 2009
    https://arxiv.org/abs/0909.4061

# Basic idea:

The goal is to compute a low-rank approximation of input matrix A:
* **A** ~= **B C**,
where **A** has dimensions _m_ by _n_, **B** _m_ by _k_, **C** _k_ by _n_, and where k is the _numerical rank_ of **A**.

##### Two overarching steps:

1. Compute an approximate basis for the range of input matrix **A**. In other words, calculate a matrix **Q** such that:
     * **Q** has orthonormal columns.
     * **A** ~= **Q Q* A**
2. Use **Q** to help compute a standard factorization (QR, SVD, etc.) of **A**.

### Some details:

##### On step 2:
Say you want to create an approximate SVD of **A** using **Q** from step 1. More specifically, we need to compute matrices **U** and **V** with orthonormal columns and a nonnegative, diagonal matrix **s** such that **A** ~= **U s V***. This can be done in 3 steps:

1. Form **B** = **Q*** **A**, which yields the low-rank factorization **A** ~= **Q B**.
2. Compute an SVD of the small matrix: **B** = **Ua s V***.
3. Set **U** = **Q Ua**.

##### Problem formulations:
_Fixed-precision approximations:_
* Suppose we are given matrix **A** and a positive error tolerance _e_. We seek a matrix **Q** with _k = k(e)_ columns such that:
    * || **A** - **Q Q* A** || <= _e_, where || denotes the L2 operator norm.

_Fixed-rank approximations:_
* Suppose _k_ is specified in advance, and an oversampling parameter _p_ is also given. We seek to construct a matrix Q with _k + p_ orthonormal columns such that:
  * || **A** - **Q Q* A** || ~= min || **A - X**, where **X** is subject to the restraint: rank(**X**) <= _k_.
