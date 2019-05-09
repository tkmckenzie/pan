import re

f = open('data/p079_keylog.txt', 'r')
attempts = [line.strip() for line in f]
f.close()

attempts = list(set(attempts))
digits = sorted(set(list(''.join(attempts))))

# Start by finding numbers before and after each digit
pos_dict = {digit: {'before': set(), 'after': set()} for digit in digits}

digit = digits[0]

for digit in digits:
	attempts_filter = list(filter(lambda attempt: digit in attempt, attempts))
	attempt = attempts_filter[0]
	for attempt in attempts_filter:
		re_results = [m.start() for m in re.finditer(digit, attempt)]
		for index in re_results:
			pos_dict[digit]['before'].update(attempt[:index])
			pos_dict[digit]['after'].update(attempt[index+1:])
			
