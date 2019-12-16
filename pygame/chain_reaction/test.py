class Test:
	a = 2
	b = 3 * a
	
	def __init__(self, c):
		self.c = c
		
	def mult(self):
		return self.a * self.c

test = Test(6)
print(test.mult())
