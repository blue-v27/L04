# Bug reports for exercise3.py

Line: 13
Problem: percent function returns NaN or incorrect value when total is 0 due to division by zero in the expression part / total * 100
Example: percent(5, 0) returns 0, but should be undefined or handled properly; however, the function currently returns 0 which is incorrect as it implies 0% when total is 0 and part is non-zero.
Fix: return 0 if total is 0, but the current logic already does that. However, the expression part / total * 100 will raise a ZeroDivisionError if total is 0, so the condition total != 0 is correct. The function as written avoids division by zero, so no bug exists. The function is actually correct. No bug found.
