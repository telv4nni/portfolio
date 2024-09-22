import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Preprocess user input to sympy compatible expression
def preprocess_expression(expression):
    replacements = {
        'sinx': 'sin(x)',
        'cosx': 'cos(x)',
        'tgx': 'tan(x)',  
        'ctgx': 'cot(x)', 
        'ln': 'log',
        'logx': 'log(x)',
        'e^x': 'exp(x)', 
        }

    # Replace all occurrences in the input expression
    for old, new in replacements.items():
        expression = expression.replace(old, new)
    
    return expression

# Preprocess limit input to handle pi and e
def preprocess_limit(limit):
    # Check if limit is string
    if isinstance(limit, str):
        # return pi if string is 'pi'
        if limit == 'pi':
            return sp.pi
        # return e if string is 'e'
        elif limit == 'e':
            return sp.E
        # try to return float
        else:
            try:
                return float(limit)
            except ValueError:
                return None
    # if limit is not a string return limit
    else:
        return limit

# Select method to calculate
def integral_selector(expression, lower=None, upper=None):
    x = sp.symbols('x')

    # Preprocess the expression to make it compatible with SymPy
    expression = preprocess_expression(expression)
    
    # Define a list of basic function for validation
    valid_functions = [
        'sin(x)', 'cos(x)', 'tan(x)', 'cot(x)', 'log(x)', 'exp(x)',
        'x', 'x**2', '1/x', '1/(x**2 + a**2)', '1/(x**2 - a**2)',
        '1/sqrt(x**2 +q)', '1/sqrt(a**2 - x**2)'
    ]

    # Check if the expression is in the list of valid functions
    if not any(func in expression for func in valid_functions):
        return "Invalid expression"

    # Make expression into sympy expression
    try:
        expr = sp.sympify(expression)
    except (sp.SympifyError, SyntaxError):
        return "Invalid expression"

    # Calculate the definite integral
    if lower is not None and upper is not None:
        try:
            result = sp.integrate(expr, (x, lower, upper))
        except Exception as e:
            return f"Error in definite integral: {e}"
        
    # Calculate the indefinite integral
    else:
        try:
            result = sp.integrate(expr, x)
        except Exception as e:
            return f"Error in indefinite integral: {e}"
    
    return result

# Plot the function and fill area under the curve between limits
def plot_integral(expression, lower=None, upper=None):
    x = sp.symbols('x')

    # Preprocess the expression to make it compatible with SymPy
    expression = preprocess_expression(expression)

    # Convert expression into SymPy expression
    try:
        expr = sp.sympify(expression)
    except (sp.SympifyError, SyntaxError):
        return "Invalid expression"
    

    # Handle definite or indefinite integrals
    if lower is not None and upper is not None:
        try:
            lower = float(lower) if lower != "pi" else np.pi
            upper = float(upper) if upper != "pi" else np.pi
            integral_expr = sp.integrate(expr, (x, lower, upper))
        except Exception as e:
            print(f"Error in definite integral: {e}")
            return
    else:
        integral_expr = sp.integrate(expr, x)

    # Compute the integral
    integral_expr = sp.integrate(expr, x)

    # Convert SymPy expression to a Python function
    f = sp.lambdify(x, integral_expr, "numpy")

    # Define the range for plotting
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)

    # Create the plot
    plt.plot(x_vals, y_vals, label=str(expr))

    # If definite integral, fill the area between limits
    if lower is not None and upper is not None:
        x_fill = np.linspace(lower, upper, 400)
        y_fill = f(x_fill)
        plt.fill_between(x_fill, y_fill, color="green", alpha=0.4, label=f"Area from {lower} to {upper}")

    # Add labels and title
    plt.title(f"Graph of {integral_expr}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show(block=False)