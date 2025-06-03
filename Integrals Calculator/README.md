# Integral Calculus
#### Video Demo:  <[URL HERE](https://www.youtube.com/watch?v=D-wO7E12Kpc)>
#### Description:

This is Python-base application with Graphical Interface that calculates both definite and indefinite integrals of various mathematical functions. It uses CustomTkinter for the graphical interface and SymPy for symbolic mathematics. Additionally, the app can plot the integral functions using Matplotlib.
y
**Features:**
*Indefinite Integrals: Computes the indifinite integral of common mathematical *functions.
*Definite Integrals: Computes the definite integral of a given function within a specified limits.
*Graphical Interface: Uses CustomTKinter to add user-friendly interface.
*Graph Plotting: Displays the graph of the computed integral function using Matploblib library.
*Supports Pi and e as Limits: Can calculate integrals with Pi and e as a limit value.
*Processed functions:
```
sin(x), cos(x), tg(x), ctg(x), log(x), e^x or exp(x), x, x^n or x**n, 1/x, 1/(x**2 + a**2), 1/(x**2 - a**2), 1/sqrt(x**2 +q), 1/sqrt(a**2 - x**2)
```

**Libraries used:**
*CustomTKinter: For the GUI interface
*SymPy: For computing integrals
*Matplotlib: For showing graph of the integral
*Pillow: For handling image display to show formula of the integral

***integrals.py:***
It handles helper functions for the main file of the app, processing and computing entered data to help with overall clarity of the application. Here happens all the math magic.

**preprocess_expression(expression):**
Preprocess user input to make it compatible with SymPy library and adds brackets to user inputs to make it more user friendly. Inputs expression and returns modified expression.

**preprocess_limit(limit):**
Preprocess user input of limits to handle Pi and e as valid values and make it SymPy compatible. Inputs limit and returns corrected limit.

**integral_selector(expression, lower=None, upper=None):**
Inputs expression, preprocess it and then checks if it's in the list of valid functions for integration. Next function makes expression into SymPy expression. Now it's ready to calculate integral. First it checks if integral is definite (has limits) or not. Returns integrated expression.

**plot_integral(expression, lower=None, upper=None):**
Plot the graph of the integrated function and fill area under the curve between the limits for definite integrals. Firstly it preprocesses the expression to make it SymPy compatible and the tries to convert it into SymPy expression. Next it computes the integral and converts it to Python function. It's time for setting up the plotting for the graph and creating it. Check if integral is definite and fill area between limits if it is. Setup labels and title, show the graph.

***main.py***
It handles main frame of the application, operates GUI. First it set ups window for Graphical UI and creates image to be used later as integral formula.

**buttoncalculate(entry, lowerentry, upperentry):**
Inputs user added formula to integrate and limits after clicking the button. Gets their values. Decides if it's definite or indefinite integral and selects correct function to calculate. If it is definite integral it preprocesses limits to handle Pi and e. Calls function to make a plot. It updates labelresult to show result of the integration.

Afterwards is setup of the GUI elements. Frames, apptitle, labels, entrymessage, buttons, image, user prompts, input fields.

***backup.py***
Application originally was intended to not include SymPy library and make calculations from the start. However because I decided to include definite integrals as option, SymPy library was used to save a lot of time and my own sanity. Kept it to show progress of the application during creation. This is only one of the changes made to the project over time.

**Installation:**
1. To make sure that application works install mentioned before libraries:
```
pip install sympy customtkinter matplotlib pillow
```
2. It's advised to set up a virtual environment:
```
python -m venv myvenv
source myvenv/bin/activate # On windows, use myvenv/Scripts/activate
```

**Usage:**
1. Run the application:
python main.py
2. Enter your mathematical function in the input box.
3. Enter your limits (optional)
4. Click calculate, the program will compute the integral and plot the graph of entered function.
5. Done!

Application was made solely by ***Hubert Jasiński*** with help of ChatGPT.
