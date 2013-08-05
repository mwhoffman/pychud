import dchud
import numpy as np
import numpy.testing as nt
import scipy.linalg


def test_dchud():
    n = 100     # number of random matrices to test.
    p = 100     # size of the matrices.

    for i in xrange(n):
        # get a random symmetric matrix A of size p and a random vector x so
        # that we can use x to do a rank-1 update of A.
        A = np.random.rand(p, p)
        A = np.dot(A.T, A)
        x = np.random.rand(p)

        # get an upper-triangular cholesky of A and the cholesky of its rank one
        # update. note that the scipy version of cho_factor doesn't touch the
        # opposite triangle, which is why for doing products later we'll have to
        # zero these out.
        R1, _ = scipy.linalg.cho_factor(A, lower=False)
        R2, _ = scipy.linalg.cho_factor(A + np.outer(x,x), lower=False)

        # perform the update on R1.
        R1 = dchud.dchud(R1, x)

        # note that for both of these the lower triangle is arbitrarily
        # initialized.  so if we want the *real* cholesky we should zero these
        # components out.
        i, j = np.tril_indices(R1.shape[0], -1)
        R1[i,j] = 0
        R2[i,j] = 0

        # rather than checking that the cholesky is close we're going to check
        # whether the corresponding matrix is close. This is because the two
        # methods of computing the cholesky can differ on signs.
        nt.assert_allclose(np.dot(R1.T, R1), np.dot(R2.T, R2))

