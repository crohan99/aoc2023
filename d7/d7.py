"""
Carson Rohan
AOC 2023
Day 7: Name_of_puzzle
"""

from os import path
from functools import reduce

FILE_NAME = 'd7.txt'


def main():

	with open(path.join(path.dirname(path.abspath(__file__)), FILE_NAME)) as file_input:
		puzzle_input = file_input.readlines()

		print(play_camel_cards(puzzle_input))

		return 0


def play_camel_cards(hands: list):
	# merge sort
	if len(hands) > 1:
		mid = len(hands) // 2
		left_array = hands[:mid]
		right_array = hands[mid:]

		play_camel_cards(left_array)
		play_camel_cards(right_array)

		i = j = k = 0

		while i < len(left_array) and j < len(right_array):
			left_hand = get_hand(left_array[i])
			right_hand = get_hand(right_array[j])

			if compare_hands(left_hand, right_hand) == 0 or compare_hands(left_hand, right_hand) == 1:
				hands[k] = left_array[i]
				i += 1
			else:
				hands[k] = right_array[j]
				j += 1
			k += 1

		while i < len(left_array):
			hands[k] = left_array[i]
			i += 1
			k += 1

		while j < len(right_array):
			hands[k] = right_array[j]
			j += 1
			k += 1

	print(hands)

	total = 0
	for index, hand in enumerate(hands):
		total += int(get_bid(hand)) * (index + 1)

	return total


def get_hand(line: str):
	return line.split(' ')[0].strip()


def get_bid(line: str):
	return line.split(' ')[1].strip()


def compare_hands(hand1: str, hand2: str):
	score1 = score2 = 0

	if hand1 == hand2:
		return 0

	for card in hand1:
		score1 += score_card(hand1, card)

	for card in hand2:
		score2 += score_card(hand2, card)

	if score1 > score2: return 1
	if score1 < score2: return -1

	return compare_high_cards(hand1, hand2)


def score_card(hand, card):

	if hand.count(card) == 1:
		return 1

	if hand.count(card) == 2:
		return 2

	if hand.count(card) == 3:
		return 3

	if hand.count(card) == 4:
		return 4

	if hand.count(card) == 5:
		return 5


def compare_high_cards(hand1, hand2):
	face_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

	for card1 in hand1:
		for card2 in hand2:
			if card1 in face_cards.keys():
				card1 = face_cards.get(card1)

			if card2 in face_cards.keys():
				card2 = face_cards.get(card2)

			if int(card1) > int(card2):
				return 1
			if int(card1) < int(card2):
				return -1
			continue

	return 0


def part2():
	return 0


if __name__ == '__main__':
	main()
