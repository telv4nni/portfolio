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

     # if x^n
     elif re.match(r"x\^\d+", expression):
          parts = expression.split("^")
          x = parts[0]
          n = int(parts[1])
          return ixndx(x, n)

     # if 1/x
     elif re.match(r"1/x$", expression):
          return i1xdx('x')

     # if a^x
     elif re.match(r"\d+\^x", expression):
          parts = expression.split("^")
          a = parts[0]
          return iaxdx('x', a)

     # if e^x
     elif re.match(r"e\^x", expression):
          return iexdx('x')

     # if sinx
     elif re.match(r"sin\(?x\)?", expression):
          return isinxdx('x')

     # if cosx
     elif re.match(r"cos\(?x\)?", expression):
          return icosxdx('x')

     # if tgx
     elif re.match(r"tg\(?x\)?", expression):
          return itgxdx('x')

     # if ctx
     elif re.match(r"ctg\(?x\)?", expression):
          return ictgxdx('x')

     # if 1/cos^2(x)
     elif re.match(r"1/cos\^2\(?x\)?", expression):
          return i1cos2x('x')

     # if 1/sin^2(x)
     elif re.match(r"1/cos\^2\(?x\)?", expression):
          return i1sin2x('x')

     # if 1/(x^2 + a^2)
     elif re.match(r"1/x\^2\+\d+", expression):
          parts = expression.split("+")
          a = parts[1][0]
          return i1x2a2p('x', a)

     # if 1/(x^2 - a^2)
     elif re.match(r"1/x\^2\+\d+", expression):
          parts = expression.split("-")
          a = parts[1][0]
          return i1x2a2m('x', a)

     # if 1/sqrt(a^2 - x^2)
     elif re.match(r"1/sqrt\(\d+\^2-\^2\)", expression):
          parts = expression.split("(")
          a = parts[1][0]
          return i1sqrta2x2m('x', a)

     # if 1/sqrt(x^2 + q)
     elif re.match(r"1/sqrt\(x\^2\+\d+\)", expression):
          parts = expression.split("+")
          q = parts[1][0]
          return i1sqrtx2q('x', q)

     else:
          return "Formula not found."
