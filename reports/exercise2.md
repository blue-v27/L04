# Bug reports for exercise2.py

Line: 12
Problem: clamp function incorrectly limits x to low when it should clamp between low and high.
Example: clamp(3, 1, 5) returns 1, but should return 3; clamp(0, 1, 5) returns 1, which is wrong.
Fix: return max(low, min(x, high))
