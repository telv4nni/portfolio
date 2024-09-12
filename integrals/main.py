import csv
import sys
import math
import integrals
from sympy import symbols

## TODO: add brackets when x is complex eg. x+1 -> (x+1)

def main():
    # Ask user for input
    integral = input("Enter function you want to integrate: ")
    final = integrals.integral_selector(integral)
    print(f"The integral of the expression is: {final}")
    # Select method

    # Calculate integral

    # Graphs

    # Step by step solution

main()
