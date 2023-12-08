"""
Carson Rohan
AOC 2023
Day 3: Gear Ratios
"""

import os

FILE_NAME = 'd3i.txt'

def main():

	with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)) as input:
		file_input = input.readlines()

		get_part_numbers(file_input)

		return 0

def get_part_numbers(input):
	part_numbers = []

	for i, line in enumerate(input[1:-1]):
		last_line = i - 1
		next_line = i + 1

		for j, char in enumerate(line):

			if 33 <= ord(char) <= 45 or ord(char) == 47 or 58 <= ord(char) <= 64:
				return

				

	# print(list(map(lambda line:
	# 			   list(map(lambda char:
	# 						char if 33 <= ord(char) <= 45 or ord(char) == 47 or 58 <= ord(char) <= 64 else 0
	# 						, line))
	# 			   , input[1:])))

	return 0


def part2():
	return 0

if __name__ == '__main__':
	main()