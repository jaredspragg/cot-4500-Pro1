import math

def approximation_algorithm(tol=1e-6, x0=1.5):
    iter_count = 0
    x = x0
    diff = x0
    print(f"{iter_count}: {x}")
    
    while diff >= tol:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iter_count}: {x}")
        diff = abs(x - y)
    
    print(f"\nConvergence after {iter_count} iterations")

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None
    
    i = 0
    while abs(b - a) > tol and i < max_iter:
        i += 1
        p = (a + b) / 2
        if f(a) * f(p) < 0:
            b = p
        else:
            a = p
    
    print(f"Root found at: {p}")
    return p

def fixed_point_iteration(g, p0, tol=1e-6, max_iter=100):
    i = 1
    while i <= max_iter:
        p = g(p0)
        if abs(p - p0) < tol:
            print(f"Fixed point found at: {p}")
            return p
        i += 1
        p0 = p
    print("FAILURE: Did not converge")
    return None

def newton_raphson(f, df, p0, tol=1e-6, max_iter=100):
    i = 1
    while i <= max_iter:
        if df(p0) == 0:
            print("FAILURE: Derivative is zero")
            return None
        p_next = p0 - f(p0) / df(p0)
        if abs(p_next - p0) < tol:
            print(f"Root found at: {p_next}")
            return p_next
        i += 1
        p0 = p_next
    print("FAILURE: Max iterations reached")
    return None

# Example usage (Replace with actual functions as needed)
def example_function(x):
    return x**2 - 2

def example_derivative(x):
    return 2*x

def example_g(x):
    return (x + 2/x) / 2

if __name__ == "__main__":
    print("Approximation Algorithm:")
    approximation_algorithm()
    
    print("\nBisection Method:")
    bisection_method(example_function, 1, 2)
    
    print("\nFixed Point Iteration:")
    fixed_point_iteration(example_g, 1.5)
    
    print("\nNewton-Raphson Method:")
    newton_raphson(example_function, example_derivative, 1.5)
