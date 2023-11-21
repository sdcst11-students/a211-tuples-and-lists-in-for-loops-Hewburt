#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""

import math
number_list = [2, -5, 7, -8, 10, 16, -3]
for number in number_list:
    if number > 0:
        square_root_value = math.sqrt(number)
        print(f"The square root of {number} is {square_root_value}")
