import pychud
import numpy as np
import numpy.testing as nt
import scipy.linalg


def check_chol(R1, R2):
    # set the lower triangle of R1 and R2 to zero.
    i, j = np.tril_indices(R1.shape[0], -1)
    R1[i,j] = 0
    R2[i,j] = 0

    # rather than checking that the cholesky is close we're going to check
    # whether the corresponding matrix is close. This is to account for sign
    # differences.
    nt.assert_allclose(np.dot(R1.T, R1), np.dot(R2.T, R2))


class TestChol:
    def setUp(self):
        p = 100
        A = np.random.rand(p, p)
        self.A = np.dot(A.T, A)
        self.x = np.random.rand(p)

    def test_dchud(self):
        # get chol before/after update.
        R1, _ = scipy.linalg.cho_factor(self.A, lower=False)
        R2, _ = scipy.linalg.cho_factor(self.A + np.outer(self.x, self.x), lower=False)

        # update on R1.
        R1 = pychud.dchud(R1, self.x)

        # check the cholesky factors.
        check_chol(R1, R2)

    def test_dchdd(self):
        # get chol before/after update.
        R1, _ = scipy.linalg.cho_factor(self.A, lower=False)
        R2, _ = scipy.linalg.cho_factor(self.A + np.outer(self.x, self.x), lower=False)

        # downdate R2.
        R2, info = pychud.dchdd(R2, self.x)

        # check the cholesky factors.
        check_chol(R1, R2)

