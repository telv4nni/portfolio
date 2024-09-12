import csv
import sys
import math
import re

##### Create Integrals Formulas for calculation (16 formulas)

# Count integral a dx
def iadx():
     integral = "x + C"
     return integral

# Count integral x^n dx
def ixndx(x, n):
    # Check if inputs are numbers
    ## n is defined
    if type(n) == int or type(n) == float:
          upper = f"{x}^{n+1}"
          lower = n+1
          integral = str(upper) + "/" + str(lower)
          return integral
    ## n is undefined
    else:
          upper = str(x) + "^" + str(n) + "+1"
          lower = str(n) + "+1"
          integral = str(upper) + "/" + str(lower)
          return integral

# Count integral x dx
def ixdx(x):
     integral = str(x) + "^2 * 1/2"
     return integral

# Count integral 1/x dx
def i1xdx(x):
     integral = f"ln|{x}|"
     return integral

# Count integral a^x dx
def iaxdx(x, a):
     integral = f"({a}^{x})/ln{a}"
     return integral

# Count integral e^x dx
def iexdx(x):
     integral = f"e^{x}"
     return integral

# Count integral sinx dx
def isinxdx(x):
     integral = f"-cos{x}"
     return integral

# Count integral cosx dx
def icosxdx(x):
     integral = f"sin{x}"
     return integral

# Count integral tgx dx
def itgxdx(x):
     integral = f"-ln|cos{x}|"
     return integral

# Count integral ctgx dx
def ictgxdx(x):
     integral = f"ln|sin{x}|"
     return integral

# Count integral 1/cos^2(x) dx
def i1cos2x(x):
     integral = f"tg{x}"
     return integral

# Count integral 1/sin^2(x) dx
def i1sin2x(x):
     integral = f"-ctg{x}"
     return integral

# Count integral 1/(x^2 - a^2) dx
def i1x2a2p(x, a):
     integral = f"((1/{a})*arctg({x}/{a}))"
     return integral

# Count integral 1/(x^2 + a^2) dx
def i1x2a2m(x, a):
     integral = f"(1/2*{a})*ln|({x}-{a})/({x}+{a})|"
     return integral

# Count integral 1/sqrt(a^2 - x^2) dx
def i1sqrta2x2m(x, a):
     integral = f"arcsin({x}/{a})"
     return integral

# Count integral 1/sqrt(x^2 + q) dx
def i1sqrtx2q(x, q):
     integral = f"ln|{x}+sqrt({x}^2+{q})|"
     return integral

#### Integral selector
def integral_selector(expression):

     if expression == "x":
          return ixdx('x')

     # if expression is number
     elif expression.isdigit():
          return iadx()

     # if expression is power of x (eg. x^n)
     elif re.match(r"x/^/d+", expression):
          parts = expression.split("^")
          x = parts[0]
          n = int(parts[1])
          return ixndx(x, n)

     elif "/x" in expression and not "/x^" in expression:
          return i1xdx('x')

     elif "^x" in expression and "e" not in expression:
          parts = expression.split("^")
          x = parts[1]
          a = parts[0]
          return iaxdx(x, a)

     elif "e^" in expression:
          return iexdx('x')

     elif "sinx" in expression:
          return isinxdx('x')

     elif "cosx" in expression:
          return icosxdx('x')

     elif "tgx" in expression:
          return itgxdx('x')

     elif "ctgx" in expression:
          return ictgxdx('x')

     elif "1/cos^2" in expression:
          return i1cos2x('x')

     elif "1/sin^2" in expression:
          return i1sin2x('x')

     elif "1/x^2+" in expression:
          parts = expression.split("+")
          a = parts[1][0]
          return i1x2a2p('x', a)

     elif "1/x^2-" in expression:
          parts = expression.split("-")
          a = parts[1][0]
          return i1x2a2m('x', a)

     elif "1/sqrt(x^2" in expression:
          parts = expression.split("+")
          q = parts[1][0]
          return i1sqrtx2q('x', q)

     elif "1/sqrt" in expression and not "1/sqrt(x^2" in expression:
          parts = expression.split("(")
          a = parts[1][0]
          return i1sqrta2x2m('x', a)

     else:
          return "Formula not found."
