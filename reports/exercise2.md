# Bug reports for exercise2.py

Line: 12
Problem: clamp function does not handle the case where x is exactly equal to low or high correctly due to redundant min/max usage, but more critically, the docstring implies it returns x within [low, high], which is correct, so no bug in logic.
Example: clamp(3, 1, 5) returns 3, which is correct; however, if x is less than low, it returns low, and if greater than high, it returns high — this is correct per specification.
Fix: No fix needed. The function is logically correct.
