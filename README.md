pychud
======

Python interface for the linpack dchud function for rank one updates to
the Cholesky factorization. This actually isn't "really" a python
interface, as I've just modified the Fortran code so this can be
compiled using f2py and then called from python.

Regardless it can be compiled using 
    
    f2py2.7 -lblas -c -m dchud dchud.f

which should create dchud.so. From there just follow the example in
test.py.

As an aside you can find the original, unmodified dchud at
http://www.netlib.org/linpack/dchud.f, and as far as I can tell linpack
is public domain... so go nuts?

