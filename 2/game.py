# Game.py
import re

# Read the file/puzzle
puzzle = open("puzzle.txt", "r")

class Game:
    def __init__(self, red, green, blue):
        self.puzzle = puzzle
        self.red = red
        self.green = green
        self.blue = blue
        self.bag = {"red": self.red, "green": self.green, "blue": self.blue}


    def print_bag(self):
        """
        Prints out content of the current bag
        """

        print(self.bag)

    def print_puzzle(self):
        """
        Prints out the rows in the file
        """

        for line in puzzle:
            print(line)

    def possible_ids(self):
        rows = self.puzzle
        possible_id_counter = 0

        for line in rows:
            id_counter = 0
            set_counter = 0

            line = re.split(';|:', line)
            number = line.pop(0)
            number = int(''.join(filter(lambda i: i.isdigit(), number)))
            row = dict(red=0, green=0, blue=0)

            for set in line:
                set_counter += 1  # Increase set_counter for each set
                set = set.replace(" ", "")
                set_list = set.strip().split(',')

                for color in set_list:
                    color_only = ''.join([char for char in color if char.isalpha()])
                    number_of_cubes = int(''.join(filter(lambda i: i.isdigit(), color)))
                    row[color_only] = row.get(color_only, 0) + number_of_cubes

                # Check if the entire set is approved
                set_approved = True  # Assume the set is approved until proven otherwise
                for key in row.keys():
                    if int(row[key]) > int(self.bag[key]):
                        set_approved = False  # If one color exceeds the bag's value, not approved
                        break

                if set_approved:
                    id_counter += 1  # If the entire set is approved, increase id_counter

                # Reset the colors for the next set
                row = dict(red=0, green=0, blue=0)

            # print(f"Comparison for game {number}: id_counter = {id_counter}, set_counter = {set_counter}")

            if id_counter == set_counter:
                # print(f"Game {number} is possible")
                possible_id_counter += int(number)
            # else:
                # print(f"Game {number} is NOT possible")

    def minmum(self):

        rows = self.puzzle
        minimum_numbers_multiplied = 1
        total = []

        for line in rows:
            minimum_numbers_multiplied = 1
            line = re.split(';|:', line)
            number = line.pop(0)
            number = int(''.join(filter(lambda i: i.isdigit(), number)))
            row = dict(red=0, green=0, blue=0)

            for set in line:
                set = set.replace(" ", "")
                set_list = set.strip().split(',')

                for color in set_list:
                    color_only = ''.join([char for char in color if char.isalpha()])
                    number_of_cubes = int(''.join(filter(lambda i: i.isdigit(), color)))
                    if number_of_cubes > row[color_only]:
                        row[color_only] = number_of_cubes
                    else:
                        row[color_only] = row.get(color_only, 0)

            for key in row.keys():
                minimum_numbers_multiplied = int(row[key]) *  minimum_numbers_multiplied

            total.append(minimum_numbers_multiplied)

        result = 0

        for number in total:
            result += number

        print(result)
