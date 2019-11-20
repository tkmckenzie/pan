import numpy as np
import pygame
from modules import *

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.width, self.height = 1440, 900
		
		self.clock = pygame.time.Clock()
		self.framerate = 60
		
	def on_init(self):
		self.initialize_pygame()
		self.initialize_objects()
	
	def initialize_pygame(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size)
		self._running = True
	
	def initialize_objects(self):
		pygame.draw.rect(self._display_surf, pygame.Color(0, 0, 0), pygame.Rect((0, 0, self.width, self.height)))
		
		self.atoms = [Atom(self) for i in range(25)]
		for atom in self.atoms:
			pygame.draw.circle(self._display_surf, atom.color, atom.get_pos(), atom.get_radius())
		
		self.explosions = []
		
		self.explosion_triggered = False
		
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN and not self.explosion_triggered:
			mouse_pos = pygame.mouse.get_pos()
			self.explosions.append(Explosion(mouse_pos, self))
			self.explosion_triggered = True
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_n:
				self.initialize_objects()
				self.explosion_triggered = False
			if event.key == pygame.K_ESCAPE:
				self._running = False
	
	def on_loop(self):
		for atom in self.atoms:
			pygame.draw.circle(self._display_surf, pygame.Color(0, 0, 0), atom.get_pos(), atom.get_radius())
			atom.update_pos()
			if any([atom.is_collison(explosion) for explosion in self.explosions]):
				self.explosions.append(Explosion(atom.pos, self))
				self.atoms.remove(atom)
		
		for explosion in self.explosions:
			pygame.draw.circle(self._display_surf, pygame.Color(0, 0, 0), explosion.get_pos(), explosion.get_radius())
			explosion.update_radius()
			if explosion.nonexistent:
				self.explosions.remove(explosion)
	
	def on_render(self):
		for atom in self.atoms:
			pygame.draw.circle(self._display_surf, atom.color, atom.get_pos(), atom.get_radius())
		
		for explosion in self.explosions:
			pygame.draw.circle(self._display_surf, explosion.color, explosion.get_pos(), explosion.get_radius())
		
		pygame.display.flip()
	
	def on_cleanup(self):
		pygame.quit()
		
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
		
		while self._running:
			for event in pygame.event.get():
				self.on_event(event)
			
			self.on_loop()
			self.on_render()
			
			self.clock.tick(self.framerate)

		self.on_cleanup()

if __name__ == '__main__':
	theApp = App()
	theApp.on_execute()
