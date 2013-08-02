pychud
======

Python interface for the linpack `dchud` function for rank one updates to the
Cholesky factorization. This is really just some minor modifications of the
Fortran code so that it can be compiled using f2py.

Regardless, it can be built inplace using `python setup.py build_ext --inplace`
which should create `dchud.so`. From here you can run `nosetests` and if
everything passes just run 
    
    python setup.py install

and you should be good to go. This just creates a `dchud` package which includes
a function of the same name. See also `test.py`, which for the time being is the
only real documentation on this function.

As an aside you can find the original, unmodified code at
http://www.netlib.org/linpack/dchud.f, and as far as I can tell linpack is
public domain... so go nuts?

