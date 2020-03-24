class Number:
	def __init__(self, n):
		if type(n) != int: raise ValueError('n must be an integer.')
		if n < 0: raise ValueError('n must be non-negative.')
		self.n = n
		
		self.word_l_20 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
					5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
					10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
					15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
		self.word_l_100 = {0: 'zero', 10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty',
					 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
		
		self.letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
						'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
						'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 0}
	
	def to_word(self, n_alternate = None):
		if n_alternate == None:
			n = self.n
		else:
			n = n_alternate
		
		if n < 20:
			return self.word_l_20[n]
		elif n < 100:
			tens_digit = int(n / 10)
			remainder = n % 10
			if remainder == 0:
				return self.word_l_100[tens_digit * 10]
			else:
				return self.word_l_100[tens_digit * 10] + ' ' + self.to_word(remainder)
		elif n < 1000:
			hundreds_digit = int(n / 100)
			remainder = n % 100
			if remainder == 0:
				return self.word_l_20[hundreds_digit] + ' hundred'
			else:
				return self.word_l_20[hundreds_digit] + ' hundred ' + self.to_word(remainder)
		elif n < 1000000:
			thousands_digits = int(n / 1000)
			remainder = n % 1000
			if remainder == 0:
				return self.to_word(thousands_digits) + ' thousand'
			else:
				return self.to_word(thousands_digits) + ' thousand ' + self.to_word(remainder)
		elif n < 1000000000:
			millions_digits = int(n / 1000000)
			remainder = n % 1000000
			if remainder == 0:
				return self.to_word(millions_digits) + ' million'
			else:
				return self.to_word(millions_digits) + ' million ' + self.to_word(remainder)
		else:
			raise NotImplementedError('n must be less than 1 billion to translate to words.')
	
	def score_word(self):
		return sum([self.letter_values[c] for c in self.to_word()])

n_max = 0
for i in range(1, 10000000):
	n = Number(i)
	if n.score_word() > i:
		n_max = i
