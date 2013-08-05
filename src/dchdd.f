      subroutine dchdd(r,ldr,p,x,c,s,info)
      integer ldr, p, info
      double precision r(ldr,p), x(p), s(p), c(p)
c
c     Given a cholesky decomposition A=R^T R of some matrix A, compute
c     the decomposition of A' = A - x^Tx as a function of R and the
c     vector x. The user is warned that a given downdating problem may
c     be impossible to accomplish or may produce inaccurate results.
c     for example, this can happen if x is near a vector whose removal
c     will reduce the rank of r.
c
c     Parameters:
c         r      double precision(ldr,p), where ldr .ge. p.
c                r contains the upper triangular matrix
c                that is to be downdated.  the part of  r
c                below the diagonal is not referenced.
c
c         ldr    integer.
c                ldr is the leading dimension fo the array r.
c
c         p      integer.
c                p is the order of the matrix r.
c
c         x      double precision(p).
c                x contains the row vector that is to
c                be removed from r.  x is not altered by dchdd.
c
c         c      double precision(p).
c                c contains the cosines of the transforming
c                rotations.
c
c         s      double precision(p).
c                s contains the sines of the transforming
c                rotations.
c
c         info   integer.
c                info is set as follows.
c
c                   info = 0  if the entire downdating
c                             was successful.
c
c                   info =-1  if r could not be downdated.
c                             in this case, all quantities
c                             are left unaltered.
c
c     linpack. this version dated 08/14/78 .
c     g.w. stewart, university of maryland, argonne national lab.
c
c     dchdd uses the following functions and subprograms.
c
c     fortran dabs
c     blas ddot, dnrm2
c
c     NOTE: we have to declare the return types of these two
c     subroutines. I have no idea why.
      double precision ddot, dnrm2
c
      integer i,ii,j
      double precision a,alpha,beta,norm
      double precision t,b,xx
c
c     solve the system trans(r)*a = x, placing the result
c     in the array s.
c
      info = 0
      s(1) = x(1)/r(1,1)
      if (p .lt. 2) go to 20
      do 10 j = 2, p
         s(j) = x(j) - ddot(j-1,r(1,j),1,s,1)
         s(j) = s(j)/r(j,j)
   10 continue
   20 continue
      norm = dnrm2(p,s,1)
      if (norm .lt. 1.0d0) go to 30
         info = -1
         go to 120
   30 continue
         alpha = dsqrt(1.0d0-norm**2)
c
c        determine the transformations.
c
         do 40 ii = 1, p
            i = p - ii + 1
            beta = alpha + dabs(s(i))
            a = alpha/beta
            b = s(i)/beta
            norm = dsqrt(a**2+b**2)
            c(i) = a/norm
            s(i) = b/norm
            alpha = beta*norm
   40    continue
c
c        apply the transformations to r.
c
         do 60 j = 1, p
            xx = 0.0d0
            do 50 ii = 1, j
               i = j - ii + 1
               t = c(i)*xx + s(i)*r(i,j)
               r(i,j) = c(i)*r(i,j) - s(i)*xx
               xx = t
   50       continue
   60    continue
  120 continue
      return
      end
