import numpy as np

f = open('data/poker.txt', 'r')

def card_number(s):
	try:
		return int(s)
	except ValueError:
		if s == 'T':
			return 10
		elif s == 'J':
			return 11
		elif s == 'Q':
			return 12
		elif s == 'K':
			return 13
		elif s == 'A':
			return 14
		else:
			raise ValueError('card value ' + s + ' not recognized.')

def duplicity(l):
	l_copy = list(l)
	result = {}
	while len(l_copy) > 0:
		e = l_copy[0]
		initial_len = len(l_copy)
		l_copy = list(filter(lambda e1: e1 != e, l_copy))
		result[e] = initial_len - len(l_copy)
	return result

def categorize_hand(hand):
	#Scores hand returning a number
	#0 - High card
	#1 - One pair
	#2 - Two pairs
	#3 - Three of a kind
	#4 - Straight
	#5 - Flush
	#6 - Full house
	#7 - Four of a kind
	#8 - Straight flush
	#9 - Royal flush
	
	values = [card_number(card[0]) for card in hand]
	suits = [card[1] for card in hand]
	hand_duplicity = duplicity(values)
	
	ordered_values = sorted(values)
	
	if len(set(suits)) == 1 and all([diff == 1 for diff in np.diff(ordered_values)]):
		# Straight flushes
		if ordered_values == [10, 11, 12, 13, 14]:
			return {'name': 'royal flush', 'values': ordered_values[::-1], 'break_values': [], 'score': 9}
		else:
			return {'name': 'straight flush', 'values': ordered_values[::-1], 'break_values': [ordered_values[-1]], 'score': 8}
	elif max(hand_duplicity.values()) == 4:
		# Four of a kind
		four_of_a_kind_value = [k for k, v in hand_duplicity.items() if v == 4][0]
		other_value = [k for k, v in hand_duplicity.items() if v == 1][0]
		return {'name': 'four of a kind', 'values': ordered_values[::-1], 'break_values': [four_of_a_kind_value, other_value], 'score': 7}
	elif sorted(hand_duplicity.values()) == [2, 3]:
		# Full house
		three_of_a_kind_value = [k for k, v in hand_duplicity.items() if v == 3][0]
		pair_value = [k for k, v in hand_duplicity.items() if v == 2][0]
		return {'name': 'full house', 'values': ordered_values[::-1], 'break_values': [three_of_a_kind_value, pair_value], 'score': 6}
	elif len(set(suits)) == 1:
		# Flush
		return {'name': 'flush', 'values': ordered_values[::-1], 'break_values': ordered_values[::-1], 'score': 5}
	elif all([diff == 1 for diff in np.diff(ordered_values)]):
		# Straight
		return {'name': 'straight', 'values': ordered_values[::-1], 'break_values': [ordered_values[-1]], 'score': 4}
	elif max(hand_duplicity.values()) == 3:
		# Three of a kind
		three_of_a_kind_value = [k for k, v in hand_duplicity.items() if v == 3][0]
		other_values = sorted([k for k, v in hand_duplicity.items() if v != 3])[::-1]
		return {'name': 'three of a kind', 'values': ordered_values[::-1], 'break_values': [three_of_a_kind_value] + other_values, 'score': 3}
	elif sorted(hand_duplicity.values()) == [1, 2, 2]:
		# Two pairs
		pair_values = [k for k, v in hand_duplicity.items() if v == 2]
		high_pair_value = max(pair_values)
		low_pair_value = min(pair_values)
		other_value = [k for k, v in hand_duplicity.items() if v == 1][0]
		return {'name': 'two pairs', 'values': ordered_values[::-1], 'break_values': [high_pair_value, low_pair_value, other_value], 'score': 2}
	elif sorted(hand_duplicity.values()) == [1, 1, 1, 2]:
		# One pair
		pair_value = [k for k, v in hand_duplicity.items() if v == 2][0]
		other_values = sorted([k for k, v in hand_duplicity.items() if v == 1])[::-1]
		return {'name': 'one pair', 'values': ordered_values[::-1], 'break_values': [pair_value] + other_values, 'score': 1}
	else:
		# High card
		return {'name': 'high card', 'values': ordered_values[::-1], 'break_values': ordered_values[::-1], 'score': 0}

def break_tie(d1, d2):
	# Returns number of player that won; 1 for player 1 (d1), 2 for player 2 (d2), 0 for tie
	if d1['name'] != d2['name']: raise ValueError('hands must be of same type, otherwise no tie to break.')
	
	break_difference = np.array(d1['break_values']) - np.array(d2['break_values'])
	difference_eval = sum(13**np.arange(len(break_difference), 0, -1) * break_difference)
	
	if difference_eval > 0:
		return 1
	elif difference_eval < 0:
		return 2
	else:
		return 0

def determine_winner(hand1, hand2):
	cat_hand1 = categorize_hand(hand1)
	cat_hand2 = categorize_hand(hand2)
	
	if cat_hand1['score'] > cat_hand2['score']:
		return 1
	elif cat_hand1['score'] < cat_hand2['score']:
		return 2
	else:
		return break_tie(cat_hand1, cat_hand2)


#testing = True
#while testing:
#	line = f.readline().strip()
#	cards = line.split(' ')
#	
#	hand1 = cards[:5]
#	hand2 = cards[5:]
#
#	print(hand1, categorize_hand(hand1)['name'], hand2, categorize_hand(hand2)['name'], determine_winner(hand1, hand2))
#
#	if input('type stop to stop: ') == 'stop':
#		testing = False

count = 0
for line in f:
	cards = line.split(' ')
	hand1 = cards[:5]
	hand2 = cards[5:]
	
	if determine_winner(hand1, hand2) == 1: count += 1
	
print(count)
