"""
--- Day 1: Trebuchet?! ---
PART 1
"""

# Read the file/puzzle
puzzle = open("puzzle.txt", "r")

# List to hold lines values
values = []

# Calculator
calculator = 0

# Calculate Each line in puzzle
for line in puzzle:
    # get digits
    digits = ''.join(filter(lambda i: i.isdigit(), line))

    # get first digit and last digit
    first = digits[0]
    last = digits[-1]

    #add value to values
    sum_line = first + last
    values.append(sum_line)

# Calculate sum
for value in values:
    calculator = calculator + int(value)

print(f"the sum is: {calculator}")
