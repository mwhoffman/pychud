import dchud
import numpy as np
import scipy.linalg

def test_dchud():
    p = 5
    A = np.random.rand(p, p)
    A = np.dot(A.T, A)
    x = np.random.rand(p)

    R, _ = scipy.linalg.cho_factor(A, lower=False)

    R = np.asfortranarray(R)
    x = np.asfortranarray(x)
    c = np.asfortranarray(np.empty(p))
    s = np.asfortranarray(np.empty(p))

    dchud.dchud(R, x, c, s)
    Rother, _ = scipy.linalg.cho_factor(A + np.outer(x,x), lower=False)

    i, j = np.tril_indices(R.shape[0],-1)
    R[i,j] = 0
    Rother[i,j] = 0

    assert np.allclose(np.dot(R.T,R), np.dot(Rother.T,Rother))

