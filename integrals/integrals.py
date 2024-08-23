import csv
import sys
import random
import math

# Create Integrals Formulas for calculation

# Count integral x^n dx
def ixndx(x, power):
    x = x
    n = power
    upper = pow(x, (n+1))
    lower = n+1
    integral = string(upper + "/" + lower)

    return integral

