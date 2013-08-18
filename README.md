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


More on installation...
========================

Installation of this package seems to be vaguely broken at the moment. The
current `setup.py` should work on linux machines using anaconda with the
accelerate package installed (for MKL). Without accelerate you may have to
remove the line that talks about this as I'm not sure `get_info` really throws
an exception the way its documentation says it's supposed to.

On OSX there is a way to get this working, but it's a pain right now. I'll add
more documentation on this at some later date, but for the time being it
involves using `install_name_tool` and some other magic. Even better I'll try to
get the setup script to actually work, but for the time-being I'm giving up.
