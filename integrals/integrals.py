import csv
import sys
import math

# Create Integrals Formulas for calculation

# Count integral x^n dx
def ixndx(x, n):
    x = x
    n = n
    # Check if inputs are numbers
    ## x and n are defined:
    if type(x) == int or type(x) == float:
        if type(n) == int or type(n) == float:
            upper = pow(x, (n+1))
            lower = n+1
            integral = upper/lower
            return integral
    ## x is defined and n is undefined
        else:
            upper = str(x) + "^" + n + "+1"
            lower = n + " + 1"
            integral = str(upper) + "/" + str(lower)
            return integral
    ## x is undefined and n is defined
    elif type(n) == int or type(n) == float:
            upper = "x^" + str(n + 1)
            lower = n+1
            integral = str(upper) + "/" + str(lower)
            return integral
