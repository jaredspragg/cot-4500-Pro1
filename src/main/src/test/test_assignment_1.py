# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:30:21 2025

@author: jared
"""

from assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson

# Test for Approximation Algorithm
print("Testing Approximation Algorithm:")
approximation_algorithm(tol=1e-6, x0=1.5)  # Example from assignment_1.py

# Test for Bisection Method
print("\nTesting Bisection Method:")
def f(x):
    return x**2 - 2  # Function to find the square root of 2
bisection_method(f, 1, 2, tol=1e-6)  # Example from assignment_1.py

# Test for Fixed Point Iteration
print("\nTesting Fixed Point Iteration:")
def g(x):
    return (x + 2/x) / 2  # Iterative method to find square root of 2
fixed_point_iteration(g, 1.5, tol=1e-6)  # Example from assignment_1.py

# Test for Newton-Raphson Method
print("\nTesting Newton-Raphson Method:")
def f_newton(x):
    return x**2 - 2  # Function to find the square root of 2

def df_newton(x):
    return 2*x  # Derivative of the function

newton_raphson(f_newton, df_newton, 1.5, tol=1e-6)  # Example from assignment_1.py
