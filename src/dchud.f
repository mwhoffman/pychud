      subroutine dchud(r,ldr,p,x,c,s)
      integer ldr, p
      double precision r(ldr,p), x(p), s(p), c(p)
c
c     Given a cholesky decomposition A=R^T R of some matrix A, compute
c     the decomposition of A' = A + x^Tx as a function of R and the
c     vector x.
c
c     Parameters:
c         r     double precision(ldr,p), denoting the upper triangular
c               cholesky decomposition of the matrix A. after completing
c               this function call the matrix will be overwritten with
c               the updated cholesky.
c
c         ldr   integer, leading dimension of r.
c
c         p     integer, order of the matrix r.
c
c         x     double precision(p), vector used for the rank one
c               update.
c
c         c     double precision(p), contains the cosines of the
c               transforming rotations.
c
c         s     double precision(p), contains the sines of the
c               transforming rotations.
c
c     linpack. this version dated 08/14/78 .
c     g.w. stewart, university of maryland, argonne national lab.
c
c     modified by m.w. hoffman. 2013/02/11
c     got rid of the extra generalization to update extra vectors z.
c     also modified the function call to make it easier to call from
c     python with f2py.
c
c     dchud uses the following functions and subroutines.
c     extended blas: drotg
c
      integer i,j,jm1
      double precision t,xj
c
c     update r.
c
      do 30 j = 1, p
         xj = x(j)
c
c        apply the previous rotations.
c
         jm1 = j - 1
         if (jm1 .lt. 1) go to 20
         do 10 i = 1, jm1
            t = c(i)*r(i,j) + s(i)*xj
            xj = c(i)*xj - s(i)*r(i,j)
            r(i,j) = t
   10    continue
   20    continue
c
c        compute the next rotation.
c
         call drotg(r(j,j),xj,c(j),s(j))
   30 continue
      return
      end
