# Curve Fitting

import numpy as np
import pandas as pd

from scipy.optimize import curve_fit

import matplotlib.pyplot as plt


# Program ---------------------------------------------------------------

print("\n ****  Curve Fitting  ****\n")

np.random.seed(27)
Size= 100

x_data = np.linspace(-10, 10, num= Size)


def Equation(x, a, b, c):

    # for the example, it is EQUAL to Quadratic
    Equation = (a*x)**2 + b*x + c
    return Equation
 

y_data = Equation(x_data, 1.5, 10, -10)
y_noise = 10 * np.random.normal(size= Size)
y_data = y_data + y_noise


# Fitting

def LinearCurve(x, a, b):

    Linear = a*x + b
    return Linear


Lin_Coef, Lin_Cov = curve_fit(LinearCurve, x_data, y_data)

Lin_A = Lin_Coef[0]
Lin_B = Lin_Coef[1]

Lin_Prev = LinearCurve(x_data, Lin_A, Lin_B)
Lin_Corr = np.corrcoef(y_data, Lin_Prev)[0,1]

print(f" >    Linear Corr: {Lin_Corr:.6f}")


def QuadraticCurve(x, a, b, c):

    Quadratic = (a*x)**2 + b*x + c
    return Quadratic


Quad_Coef, Quad_Cov = curve_fit(QuadraticCurve, x_data, y_data)

Quad_A = Quad_Coef[0]
Quad_B = Quad_Coef[1]
Quad_C = Quad_Coef[2]

Quad_Prev = QuadraticCurve(x_data, Quad_A, Quad_B, Quad_C)
Quad_Corr = np.corrcoef(y_data, Quad_Prev)[0,1]

print(f" > Quadratic Corr: {Quad_Corr:.6f}")


fig = plt.figure(figsize= (8, 4.5))

Title = "Curve Fitting - Simple Quadratic"
plt.suptitle(Title, fontsize= 14)

plt.scatter(x_data, y_data, color= "cornflowerblue", edgecolor= "white", label= "Data", zorder= 10)

plt.plot(x_data, Lin_Prev, color= "navy", label= "Linear", zorder= 11)
plt.plot(x_data, Quad_Prev, color= "darkred", label= "Quadratic", zorder= 12)

plt.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)

Box_Text = f"Correlation:\nLinear= {Lin_Corr:.4f}\nQuadratic= {Quad_Corr:.4f}"
Box_Props = dict(boxstyle= "round", edgecolor= "lightgrey", facecolor= "white", alpha= 1)

plt.text(10.6, -40, Box_Text, fontsize= 9, ha= "right", bbox= Box_Props)
plt.legend(loc= "best", fontsize= 9, framealpha= 1)


# Closing

#plt.savefig(Title, dpi= 240)
plt.show()

print(" * \n")
