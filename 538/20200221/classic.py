from fractions import Fraction

num_flips = 100
threshold = 2 # For any score strictly below the threshold, coin B (multiplier 2) will be used; otherwise coin A (multiplier 1) will be used

state = {0: Fraction(1, 1)}

def feed_forward(state):
	new_state = {}
	for score in state.keys():
		score_prob = state[score]
		
		if score < threshold:
			multiplier = 2
		else:
			multiplier = 1
		
		new_score_lower = score - multiplier
		new_score_upper = score + multiplier
		
		if new_score_lower in new_state:
			new_state[new_score_lower] += Fraction(1, 2) * score_prob
		else:
			new_state[new_score_lower] = Fraction(1, 2) * score_prob
			
		if new_score_upper in new_state:
			new_state[new_score_upper] += Fraction(1, 2) * score_prob
		else:
			new_state[new_score_upper] = Fraction(1, 2) * score_prob
		
	return new_state

for i in range(num_flips):
	state = feed_forward(state)

win_prob = sum([state[score] for score in state.keys() if score > 0])
print(win_prob)
print(float(win_prob))
