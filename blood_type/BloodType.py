import random

class Person:
	def __init__(self, abo_type, rh_type):
		self.abo_type = abo_type
		self.rh_type = rh_type
	def procreate(self, other):
		self_abo = random.choice(self.abo_type)
		self_rh = random.choice(self.rh_type)
		other_abo = random.choice(other.abo_type)
		other_rh = random.choice(other.rh_type)
		
		new_abo = [self_abo, other_abo]
		new_rh = [self_rh, other_rh]
		
		return Person(new_abo, new_rh)
	def expressed_type(self):
		if all([gene == 'O' for gene in self.abo_type]):
			expressed_abo = 'O'
		else:
			expressed_abo = ''.join(sorted(set([gene for gene in self.abo_type if gene != 'O'])))
		
		if all([gene == '-' for gene in self.rh_type]):
			expressed_rh = '-'
		else:
			expressed_rh = '+'
		
		return expressed_abo + expressed_rh

def randomPerson():
	possible_abo = ['A', 'B', 'O']
	possible_rh = ['+', '-']
	
	return Person(random.choices(possible_abo, k = 2),
			   random.choices(possible_rh, k = 2))
