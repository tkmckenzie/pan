from chain_reaction import App
from modules import *
import numpy as np
import pygame

class Bot:
	def __init__(self, App):
		# Post events with pygame.event.post
		self._running = True
		self.App = App
		
		# num_atoms: [5, 10, 15, 25, 40, 55, 75, 100]
		# required_explosions: [1, 3, 5, 10, 18, 30, 50, 75]
		self.desired_explosions = [5, 8, 10, 20, 35, 55, 75, 100]
		
	def on_loop(self):
		if not self.App.explosion_triggered:
			solution_found = False
			for atom in self.App.atoms:
				explosion = Explosion(atom.pos, atom.color, self.App)
				num_explosions = self.simulate_explosion(explosion, self.App.atoms)
				
				if num_explosions >= self.desired_explosions[self.App.current_round]:
					solution_found = True
					self.App.create_explosion(atom.pos)
					break
			
			if not solution_found:
				pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key = pygame.K_r))
	
	def simulate_explosion(self, explosion, atoms):
		atoms_copy = list(map(lambda atom: atom.__copy__(), atoms))
		explosions = [explosion]
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
		
		return num_explosions
	
	def on_execute(self):
		if self.App.on_init() == False:
			self._running = False
		
		self.App.begin_round()
		
		while self._running and self.App._running:
			
			# Run bot routines
			self.on_loop()
			
			# Run pygame routines
			for event in pygame.event.get():
				self.App.on_event(event)
			
			self.App.on_loop()
			self.App.on_render()
			
			self.App.clock.tick(self.App.framerate)
		
		# App cleanup
		self.App.on_cleanup()
		
if __name__ == '__main__':
	theApp = App()
	bot = Bot(theApp)
	bot.on_execute()
