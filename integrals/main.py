import csv
import sys
import math
import integrals
import customtkinter as tk

def main():

    # Ask user for input
    integral = input("Enter function you want to integrate: ")

    # Select method and calculate
    final = integrals.integral_selector(integral)

    # Print integral
    print(f"The integral of the expression is: {final}")

    # Graphs

    # Step by step solution

main()
