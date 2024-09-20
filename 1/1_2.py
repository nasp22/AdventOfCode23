"""
--- Day 1: Trebuchet?! ---
PART 2
"""

# Read the file/puzzle
# puzzle = open("puzzle.txt", "r")
puzzle = open("puzzle.txt", "r")

# List to hold lines values
values = []

# The alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# spelled numbers
spelled_numbers = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"

# Calculator
calculator = 0

# To digits
written_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def convert_written_number(word):
    return written_to_digit.get(word.lower(), "")

def find_min_max(dict1, dict2):
    combined_dict = {**dict1, **dict2}  # Slå ihop båda dictionaries

    # Skapa en lista med alla index
    all_indices = []
    for key, value in combined_dict.items():
        if isinstance(value, list):  # Om värdet är en lista
            all_indices.extend(value)  # Lägg till alla index i listan
        else:
            all_indices.append(value)  # Lägg till värdet om det inte är en lista

    # Hitta max och min
    maximum = max(all_indices)
    minimum = min(all_indices)

    # Hitta nycklarna (siffrorna) för minsta och största indexet
    first = last = None
    for key, value in combined_dict.items():
        if isinstance(value, list):
            if minimum in value:
                first = key
            if maximum in value:
                last = key
        else:
            if value == minimum:
                first = key
            if value == maximum:
                last = key

    # Omvandla nycklarna (siffrorna) om de är skrivna siffror
    if not first.isdigit():
        first = convert_written_number(first)
    if not last.isdigit():
        last = convert_written_number(last)

    return str(first), str(last)


# Calculate Each line in puzzle
sum_digits={}
sum_spelled_digits={}


for line in puzzle:

    # To dict with row and index value
    digits = ','.join(filter(lambda i: i.isdigit(), line))
    digits_list = digits.split(",")

    digits_dict = {}
    for index, digit in enumerate(line):
       if digit in digits_list:
           if digit not in digits_dict:
              digits_dict[digit] = [index]  # Om siffran inte finns, skapa en lista
           else:
             digits_dict[digit].append(index)  # Lägg till nya indexet till listan

    # print(digits_dict)

    spelled_digits_dict = {}

    for number in spelled_numbers:
        start = 0
        while start < len(line):
            index = line.find(number, start)  # Hitta index för skrivna siffror
            if index == -1:  # Om inget hittas, bryt loopen
                break
            if number not in spelled_digits_dict:
                spelled_digits_dict[number] = [index]  # Skapa en lista om nyckeln inte finns
            else:
                spelled_digits_dict[number].append(index)  # Lägg till det nya indexet
            start = index + len(number)  # Fortsätt leta efter nästa förekomst

    # print(spelled_digits_dict)

    first, last = find_min_max(digits_dict, spelled_digits_dict)

    # add value to values list
    sum_line = first + last
    values.append(sum_line)

# Calculate sum
for value in values:
    calculator = calculator + int(value)

print(f"the sum is: {calculator}")
