import pytest
from src.main.assignment_1 import bisection_method  # Update this line based on your function names

def test_bisection_method():
    result = bisection_method(1, 3, 0.0001)
    assert abs(result - 2) < 0.0001  # Adjust expected value and tolerance as needed
