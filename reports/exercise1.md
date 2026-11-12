# Bug reports for exercise1.py

Line: 3
Problem: The condition checks if n % 2 == 1, which is true for odd numbers, not even numbers. It should check for equality with 0 to determine if a number is even.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function returns the sum of width and height, but it should return the product (width * height) to compute the area of a rectangle.
Example: rectangle_area(5, 3) returns 8, expected 15.
Fix: return width * height

Line: 13
Problem: The function adds 2 to n, but it should return twice the number, i.e., n * 2.
Example: double(3) returns 5, expected 6.
Fix: return n * 2
