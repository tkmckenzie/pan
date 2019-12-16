from modules import *
import numpy as np
import sys

from chain_reaction import *

# call: python gen_neural_data.py <number of initial atoms> <number of simulations>
#num_atoms = int(sys.argv[1])
#num_sims = int(sys.argv[2])
num_atoms = 25
num_sims = 1

theApp = App()

for sim in range(num_sims):
	atoms = [Atom(theApp) for i in range(num_atoms)]
	atoms_pos = [atom.pos for atom in atoms]
	atoms_vel = [atom.velocity_vec for atom in atoms]
	
	explosion_results = []
	for atom in atoms:
		atom_pos = np.array(atom.pos)
		atoms_copy = list(map(lambda atom: atom.__copy__(), atoms))
		explosions = [Explosion(atom_pos, atom.color, theApp)]
		while len(explosions) > 0:
			for atom in atoms_copy:
				atom.update_pos()
				
				if any([atom.is_collision(explosion) for explosion in explosions]):
					explosions.append(atom.explode())
					atoms_copy.remove(atom)
			
			for explosion in explosions:
				explosion.update_radius()
				
				if explosion.nonexistent:
					explosions.remove(explosion)
		
		num_explosions = len(atoms) - len(atoms_copy)
		explosion_results.append((atom_pos, num_explosions))
