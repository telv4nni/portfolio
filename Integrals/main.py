import math
import integrals
import customtkinter as tk
from PIL import Image

# Set GUI
tk.set_appearance_mode("Dark")
tk.set_default_color_theme("green")

app = tk.CTk()
app.geometry("700x550")
app.title("Integral calculator")

# Create image
imageintegral = Image.open("img/integral2.png")
ctkimage = tk.CTkImage(light_image=imageintegral, dark_image=imageintegral, size=(300,100))

# Calculate integral on click
def buttoncalculate(entry, lowerentry, upperentry):
    # Get inputs
    integral = entry.get()
    lowerlimit = lowerentry.get()
    upperlimit = upperentry.get()

    # Decide if integral is definite or not
    if lowerlimit and upperlimit:
        try:
            # Preprocess limit to handle 'pi' and 'e'
            lowerlimit = integrals.preprocess_limit(lowerlimit)
            upperlimit = integrals.preprocess_limit(upperlimit)
            # Convert to float if limit is a number and not symbol
            if isinstance(lowerlimit, str):
                lowerlimit = float(lowerlimit)
            if isinstance(upperlimit, str):
                upperlimit = float(upperlimit)
            # Enter preprocessed limits to integral selector and plot
            final = integrals.integral_selector(integral, lowerlimit, upperlimit)
            integrals.plot_integral(integral, lowerlimit, upperlimit)
        except ValueError:
            final = "Invalid limits"
    # If there are no limits, calculate integral and make plot
    else:
        final = integrals.integral_selector(integral)
        integrals.plot_integral(integral)

    # Update label with the result    
    labelresult.configure(text=f"The integral of {integral} is: {final}")


# FRAME
mainframe = tk.CTkFrame(master=app)
mainframe.pack(fill="both", expand=True)

#### LEFT SIDE FRAME
leftframe = tk.CTkFrame(master=mainframe)
leftframe.pack(pady=30, padx=10, fill="both", expand=True, side="left")

# APP TITLE
labelapptitle = tk.CTkLabel(master=leftframe, text="Integral calculus", font= ("Oswald", 26, "italic"), text_color="green", corner_radius=10)
labelapptitle.pack(pady=12, padx=10)

# ENTRY MESSAGE
labelwelcome = tk.CTkLabel(master=leftframe, 
                           text='''Welcome to my integral calculus. \n\n\nFew things to get started:\n
1. If you want to calculate indefinite integral just enter your function in the first box.\n
2. If you want to calculate definite integral please use optional boxes to insert upper and lower boundary.\n
3. Processed functions are:\n sin(x), cos(x), tg(x), ctg(x), log(x), e^x or exp(x), x, x^n or x**n, 1/x,, 1/(x**2 + a**2), 1/(x**2 - a**2), 1/sqrt(x**2 +q), 1/sqrt(a**2 - x**2).\n
4. You can use basic mathematical operations on the functions you wish to integrate.\n
5. You can also use 'pi' and 'e' in your limits for integral. ''',
                           anchor='w', justify="left", wraplength=300
                           )
labelwelcome.pack(pady=12, padx=10, anchor ='w')

#### RIGHT SIDE FRAME
rightframe = tk.CTkFrame(master=mainframe)
rightframe.pack(pady=30, padx=10, fill="both", expand=True, side="right")

# CREATE FUNCTION IMAGE
image_label = tk.CTkLabel(master=rightframe, image=ctkimage, text="")
image_label.pack(pady=20, padx=20)

# ASK FOR USER PROMPT
labelinput = tk.CTkLabel(master=rightframe, text="Enter function [f(x)] you want to integrate: ")
labelinput.pack(pady=12, padx=10)

# USER PROMPT BOX
entry1 = tk.CTkEntry(master=rightframe, placeholder_text="Enter function")
entry1.pack(pady=12, padx=12)

# ADD INPUT FIELDS FOR DEFINITE INTEGRAL LIMITS
label_lower = tk.CTkLabel(master=rightframe, text="Lower limit [a] (optional):")
label_lower.pack(pady=5, padx=10)

lowerentry = tk.CTkEntry(master=rightframe, placeholder_text="Enter lower limit")
lowerentry.pack(pady=5, padx=12)

label_upper = tk.CTkLabel(master=rightframe, text="Upper limit [b] (optional):")
label_upper.pack(pady=5, padx=10)

upperentry = tk.CTkEntry(master=rightframe, placeholder_text="Enter upper limit")
upperentry.pack(pady=5, padx=12)

# CALCULATE BUTTON
buttoncalc = tk.CTkButton(master=rightframe, text = "Calculate", command =lambda: buttoncalculate(entry1, lowerentry, upperentry))
buttoncalc.pack(pady=10, padx=10)

# RESULT
labelresult = tk.CTkLabel(master=rightframe, text="")
labelresult.pack(pady=12, padx=10)

app.mainloop()
