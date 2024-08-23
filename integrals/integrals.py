import csv
import sys
import math

# Create Integrals Formulas for calculation

# Count integral x^n dx
def ixndx(x, n):
    x = x
    n = n
    upper = pow(x, (n+1))
    lower = n+1
    integral = str(upper) + "/" + str(lower)
    return integral
