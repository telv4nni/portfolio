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
          upper = "x^" + str(n + 1)
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
     ## x is defined
     if type(x) == int or type(x) == float:
          integral = (pow(x, 2))/2
          return integral
     ## x is undefined
     else:
          integral = str(x) + "^2 * 1/2"
          return integral

# Count integral 1/x dx
def i1xdx(x):
     ## x is defined
     if type(x) == int or type(x) == float:
          integral = math.log(x)
          return integral
     ## x is undefined
     else:
          integral = f"ln|{x}|"
          return integral

# Count integral ax dx
# def iaxdx(x, a):
#      ## x and a are defined
#      if type(x) == int or type(x) == float:
#           if type(a) == int or type(a) == float:
