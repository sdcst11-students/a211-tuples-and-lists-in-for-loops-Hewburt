#! python3
"""
###### Task 2
Ask the user to enter a name.
Check the name against a tuple that contains a series of names to see if it is a match. Use a for loop this time instead of a single if with multiple
logical operators
(2 points)

inputs:
str name

outputs:
"That name is in the list"
"That name is not in the list"

example:
Enter a name: Grace
That name is not on the list

example:
Enter a name: Lebron
That name is on the list
"""


name_list = ("John", "Jane", "Alice", "Bob", "Charlie")
user_input = input("Enter a name: ")
name_found = False
for name in name_list:
    if user_input == name:
        name_found = True
        break
if name_found:
    print("That name is on the list")
else:
    print("That name is not on the list")
