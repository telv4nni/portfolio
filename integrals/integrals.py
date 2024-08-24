import csv
import sys
import math

# Create Integrals Formulas for calculation

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
def icosxdc(x):
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
def i1x2-a2(x, a):
     integral = 
