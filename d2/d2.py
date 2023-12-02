"""
Carson Rohan
AOC 2023
Day 2: Cube Conundrum
"""

from os import path
from functools import reduce

FILE_NAME = 'd2i.txt'
CUBE_CONSTRAINTS = {'red': 12, 'green': 13, 'blue': 14}


def main():
    with open(path.join(path.dirname(path.abspath(__file__)), FILE_NAME)) as input:
        file_input = input.readlines()

        # part 1
        print(sum_valid_games(file_input))
        # part 2
        print(sum_cube_power_for_highest_reveals(file_input))

        return 0


def sum_valid_games(input):
    valid_game_sum = 0

    for line in input:
        game_num = get_game_number(line)
        record = get_game_record(line)

        if (validate_record(record)):
            valid_game_sum += game_num

    return valid_game_sum


def sum_cube_power_for_highest_reveals(input):
    total_cube_power = 0

    for line in input:
        record = get_game_record(line)
        reveal = highest_reveal_in_record(record)

        total_cube_power += reduce(lambda value, next_value: value * next_value, reveal.values())

    return total_cube_power


def get_game_number(input_line: str):
    game = 'Game '
    colon_idx = input_line.index(':')
    game_number_idx = input_line.index(game) + len(game)
    game_num = input_line[game_number_idx:colon_idx]

    return int(game_num)


def get_game_record(input_line: str):
    game_record = []
    game_record_idx = input_line.index(':') + 1
    game_record_string = input_line[game_record_idx:].strip()
    game_sets = game_record_string.split(';')

    for set in game_sets:
        reveal_list = {}
        reveals = set.split(',')

        for reveal in reveals:
            reveal = reveal.strip()
            num = reveal[0:reveal.index(' ')]
            color = reveal[2:]
            reveal_list.update({color.strip(): int(num)})

        game_record.append(reveal_list)

    return game_record


def validate_reveal(reveals: dict):

    for key, value in reveals.items():

        if key in CUBE_CONSTRAINTS.keys():

            if value > CUBE_CONSTRAINTS[key]:
                return False

    return True


def validate_record(record: list):

    for reveals in record:

        if (not validate_reveal(reveals)):
            return False

    return True

def compare_reveals(reveals: dict):

    for key, value in reveals.items():

        if key in CUBE_CONSTRAINTS.keys():

            if value > CUBE_CONSTRAINTS[key]:
                return False

    return True

def highest_reveal_in_record(record: list):
    highest_reveal = {'red': 0, 'green': 0, 'blue': 0}

    for reveals in record:

        for key, value in reveals.items():

            if (key in highest_reveal.keys()):

                if (value > highest_reveal[key]):
                    highest_reveal[key] = value

    return highest_reveal


if __name__ == '__main__':
    main()
