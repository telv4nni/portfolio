import csv
import sys
import math
import integrals
import customtkinter as tk

# Set GUI
tk.set_appearance_mode("System")
tk.set_default_color_theme("green")

app = tk.CTk()
app.geometry("600x300")

def button():
        print("button pressed")

def main():

    # Ask user for input
    integral = input("Enter function you want to integrate: ")

    # Select method and calculate
    final = integrals.integral_selector(integral)

    # Print integral
    print(f"The integral of the expression is: {final}")

    # Graphs

    # Step by step solution
app.mainloop()
#main()
