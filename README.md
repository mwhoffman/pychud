pychud
======

Python interface for the linpack `dchud` and `dchdd` functions for computing
rank one updates/downdates to the Cholesky factorization of some matrix. This is
really just some minor modifications of the Fortran code so that it can be
compiled using f2py.

Regardless, it can be built inplace using `python setup.py build_ext --inplace`
which should create `pychud.so`. From here you can run `nosetests` and if
everything passes just run 
    
    python setup.py install

and you should be good to go. This just creates a `pychud` package which
includes two functions
    
    R = pychud.dchud(R, x, overwrite_r=False)
    R, info = pychud.dchdd(R, x, overwrite_r=False)

for computing the update and downdate respectively. Note that for the
downdate, `info` will be zero the downdate is performed successfully and -1
otherwise. If `R` is a fortran-contiguous array and `overwrite_r` is `True`,
then the operations will be performed in place; otherwise a copy will be made.
Finally, see also `test.py`, which other than this README are the only real
documentation on these functions.

As an aside you can find the original, unmodified code at
http://www.netlib.org/linpack/dchud.f and http://www.netlib.org/linpack/dchdd.f.
As far as I can tell linpack is public domain... so go nuts?

