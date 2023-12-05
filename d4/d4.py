"""
Carson Rohan
AOC 2023
Day 4: Scratchcards
"""

from os import path

FILE_NAME = 'd4.txt'


def main():

	with open(path.join(path.dirname(path.abspath(__file__)), FILE_NAME)) as input:
		file_input = input.readlines()

		print(get_all_card_scores(file_input))
		print(get_total_cards(file_input))

		return 0


def get_all_card_scores(cards: list):
	total_score = 0

	for card in cards:
		winning_numbers = get_winning_numbers(card)
		card_numbers = get_card_numbers(card)

		card_score = 0
		for number in card_numbers:

			if number in winning_numbers:

				if card_score == 0:
					card_score += 1
					continue

				card_score <<= 1

		total_score += card_score

	return total_score


def get_total_cards(cards: list):
	cards_dict = {1: 0}

	for card in cards:
		card_idx = get_card_index(card)
		winning_numbers = get_winning_numbers(card)
		card_numbers = get_card_numbers(card)

		card_score = 0
		add_cards(card_idx, cards_dict, card_score)

		for copies in range(cards_dict.get(card_idx, 0) + 1):

			if copies > 0:
				add_cards(card_idx, cards_dict, card_score)
				continue

			for number in card_numbers:

				if number in winning_numbers:
					card_score += 1

			add_cards(card_idx, cards_dict, card_score)

	count = 0
	for val in cards_dict.values(): count += val + 1

	return count


def add_cards(card_idx, cards, score):

	if score == 0:
		cards[card_idx] = cards.get(card_idx, 0)

	for i in range(score):
		cards[card_idx + i + 1] = cards.get(card_idx + i + 1, 0) + 1


def get_card_index(input_line: str):
	game = 'Card '
	colon_idx = input_line.index(':')
	game_number_idx = input_line.index(game) + len(game)
	card_idx = input_line[game_number_idx:colon_idx]

	return int(card_idx)


def get_winning_numbers(input_line: str):
	return list(filter(lambda s: s != '', input_line[input_line.index(':') + 2:input_line.index('|') - 1].split(' ')))


def get_card_numbers(input_line: str):
	return list(filter(lambda s: s != '', input_line[input_line.index('|') + 2:].strip().split(' ')))


if __name__ == '__main__':
	main()