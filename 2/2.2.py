"""
--- Day 2: Cube Conundrum ---
PART 1

Trying to it more object-oriented in this part
"""

from game import Game


if __name__ == "__main__":

    # Create new Game (red, green, blue)
    game = Game(12, 13, 14)

    # # Print current bag
    # game.print_bag()

    # # Print puzzle rows
    # game.print_puzzle()

    # Print pssible ids
    # game.possible_ids()

    # part 2, minimum
    game.minmum()
