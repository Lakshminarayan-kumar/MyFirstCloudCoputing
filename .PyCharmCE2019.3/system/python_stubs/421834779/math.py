# encoding: utf-8
# module math
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/math.so
# by generator 1.147
"""
This module is always available.  It provides access to the
mathematical functions defined by the C standard.
"""
# no imports

# Variables with simple values
e = 2.718281828459045

pi = 3.141592653589793

# functions

def acos(x): # real signature unknown; restored from __doc__
    """
    acos(x)
    
    Return the arc cosine (measured in radians) of x.
    """
    pass

def acosh(x): # real signature unknown; restored from __doc__
    """
    acosh(x)
    
    Return the hyperbolic arc cosine (measured in radians) of x.
    """
    pass

def asin(x): # real signature unknown; restored from __doc__
    """
    asin(x)
    
    Return the arc sine (measured in radians) of x.
    """
    pass

def asinh(x): # real signature unknown; restored from __doc__
    """
    asinh(x)
    
    Return the hyperbolic arc sine (measured in radians) of x.
    """
    pass

def atan(x): # real signature unknown; restored from __doc__
    """
    atan(x)
    
    Return the arc tangent (measured in radians) of x.
    """
    pass

def atan2(y, x): # real signature unknown; restored from __doc__
    """
    atan2(y, x)
    
    Return the arc tangent (measured in radians) of y/x.
    Unlike atan(y/x), the signs of both x and y are considered.
    """
    pass

def atanh(x): # real signature unknown; restored from __doc__
    """
    atanh(x)
    
    Return the hyperbolic arc tangent (measured in radians) of x.
    """
    pass

def ceil(x): # real signature unknown; restored from __doc__
    """
    ceil(x)
    
    Return the ceiling of x as a float.
    This is the smallest integral value >= x.
    """
    pass

def copysign(x, y): # real signature unknown; restored from __doc__
    """
    copysign(x, y)
    
    Return x with the sign of y.
    """
    pass

def cos(x): # real signature unknown; restored from __doc__
    """
    cos(x)
    
    Return the cosine of x (measured in radians).
    """
    pass

def cosh(x): # real signature unknown; restored from __doc__
    """
    cosh(x)
    
    Return the hyperbolic cosine of x.
    """
    pass

def degrees(x): # real signature unknown; restored from __doc__
    """
    degrees(x)
    
    Convert angle x from radians to degrees.
    """
    pass

def erf(x): # real signature unknown; restored from __doc__
    """
    erf(x)
    
    Error function at x.
    """
    pass

def erfc(x): # real signature unknown; restored from __doc__
    """
    erfc(x)
    
    Complementary error function at x.
    """
    pass

def exp(x): # real signature unknown; restored from __doc__
    """
    exp(x)
    
    Return e raised to the power of x.
    """
    pass

def expm1(x): # real signature unknown; restored from __doc__
    """
    expm1(x)
    
    Return exp(x)-1.
    This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    """
    pass

def fabs(x): # real signature unknown; restored from __doc__
    """
    fabs(x)
    
    Return the absolute value of the float x.
    """
    pass

def factorial(x): # real signature unknown; restored from __doc__
    """
    factorial(x) -> Integral
    
    Find x!. Raise a ValueError if x is negative or non-integral.
    """
    pass

def floor(x): # real signature unknown; restored from __doc__
    """
    floor(x)
    
    Return the floor of x as a float.
    This is the largest integral value <= x.
    """
    pass

def fmod(x, y): # real signature unknown; restored from __doc__
    """
    fmod(x, y)
    
    Return fmod(x, y), according to platform C.  x % y may differ.
    """
    pass

def frexp(x): # real signature unknown; restored from __doc__
    """
    frexp(x)
    
    Return the mantissa and exponent of x, as pair (m, e).
    m is a float and e is an int, such that x = m * 2.**e.
    If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    """
    pass

def fsum(iterable): # real signature unknown; restored from __doc__
    """
    fsum(iterable)
    
    Return an accurate floating point sum of values in the iterable.
    Assumes IEEE-754 floating point arithmetic.
    """
    pass

def gamma(x): # real signature unknown; restored from __doc__
    """
    gamma(x)
    
    Gamma function at x.
    """
    pass

def hypot(x, y): # real signature unknown; restored from __doc__
    """
    hypot(x, y)
    
    Return the Euclidean distance, sqrt(x*x + y*y).
    """
    pass

def isinf(x): # real signature unknown; restored from __doc__
    """
    isinf(x) -> bool
    
    Check if float x is infinite (positive or negative).
    """
    return False

def isnan(x): # real signature unknown; restored from __doc__
    """
    isnan(x) -> bool
    
    Check if float x is not a number (NaN).
    """
    return False

def ldexp(x, i): # real signature unknown; restored from __doc__
    """
    ldexp(x, i)
    
    Return x * (2**i).
    """
    pass

def lgamma(x): # real signature unknown; restored from __doc__
    """
    lgamma(x)
    
    Natural logarithm of absolute value of Gamma function at x.
    """
    pass

def log(x, base=None): # real signature unknown; restored from __doc__
    """
    log(x[, base])
    
    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.
    """
    pass

def log10(x): # real signature unknown; restored from __doc__
    """
    log10(x)
    
    Return the base 10 logarithm of x.
    """
    pass

def log1p(x): # real signature unknown; restored from __doc__
    """
    log1p(x)
    
    Return the natural logarithm of 1+x (base e).
    The result is computed in a way which is accurate for x near zero.
    """
    pass

def modf(x): # real signature unknown; restored from __doc__
    """
    modf(x)
    
    Return the fractional and integer parts of x.  Both results carry the sign
    of x and are floats.
    """
    pass

def pow(x, y): # real signature unknown; restored from __doc__
    """
    pow(x, y)
    
    Return x**y (x to the power of y).
    """
    pass

def radians(x): # real signature unknown; restored from __doc__
    """
    radians(x)
    
    Convert angle x from degrees to radians.
    """
    pass

def sin(x): # real signature unknown; restored from __doc__
    """
    sin(x)
    
    Return the sine of x (measured in radians).
    """
    pass

def sinh(x): # real signature unknown; restored from __doc__
    """
    sinh(x)
    
    Return the hyperbolic sine of x.
    """
    pass

def sqrt(x): # real signature unknown; restored from __doc__
    """
    sqrt(x)
    
    Return the square root of x.
    """
    pass

def tan(x): # real signature unknown; restored from __doc__
    """
    tan(x)
    
    Return the tangent of x (measured in radians).
    """
    pass

def tanh(x): # real signature unknown; restored from __doc__
    """
    tanh(x)
    
    Return the hyperbolic tangent of x.
    """
    pass

def trunc(x): # real signature unknown; restored from __doc__
    """
    trunc(x:Real) -> Integral
    
    Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.
    """
    pass

# no classes
