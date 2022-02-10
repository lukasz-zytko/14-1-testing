def sqr(x):
   """Return the square of x
   >>> sqr(0)
   0
   >>> sqr(1)
   1
   >>> sqr(-2)
   4
   >>> sqr(2)
   4
   """

   return x ** 2

if __name__ == '__main__':
   import doctest
   doctest.testmod()