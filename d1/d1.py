"""
Carson Rohan
AOC 2023
Day 1: Trebuchet?!
"""

import os
from typing import List, Dict

FILE_NAME = 'd1i.txt'

digitWords = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
              'eight': '8', 'nine': '9'}

def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
        fileInput = input.readlines()

        print(calibrate_integers_only(fileInput))
        print(calibrate_digits_and_words(fileInput))

        return 0


def calibrate_integers_only(input: List[str]):
    calibrationSum = 0

    for value in input:
        digits = ''.join(list(map(str, filter(lambda calVal: calVal.isdigit(), value))))
        calibrationSum += int(digits[0]) * 10 + int(digits[-1])

    return calibrationSum


def calibrate_digits_and_words(input):
    calibrationSum = 0

    for value in input:
        wordsInfo = get_words_info(value)
        numberLocations = list(wordsInfo.keys()) + get_digit_locations(value)
        numberLocations.sort()
        front = value[numberLocations[0]] if value[numberLocations[0]].isdigit() else wordsInfo[numberLocations[0]]
        back = value[numberLocations[-1]] if value[numberLocations[-1]].isdigit() else wordsInfo[
            numberLocations[-1]]

        calibrationSum += int(front) * 10 + int(back)

    return calibrationSum


def get_next_indices(lst, target_value):
    indices = []
    current_index = -1

    while True:
        try:
            current_index = lst.index(target_value, current_index + 1)
            indices.append(current_index)
        except ValueError:
            break

    return indices


def get_digit_locations(calibrationValue):
    locations = []

    f = list(filter(lambda value: value.isdigit(), calibrationValue))

    for i in f:
        locations += get_next_indices(calibrationValue, i)

    return locations


def get_words_info(calibrationValue):
    locations = {}

    for key, value in digitWords.items():

        if key in calibrationValue:

            indices = get_next_indices(calibrationValue, key)

            for index in indices:
                locations.update({index: value})

    return locations


if __name__ == '__main__':
    main()
