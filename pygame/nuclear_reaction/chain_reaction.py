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
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size)
		self._running = True
		
		self.initialize_atoms()
	
	def initialize_atoms(self):
		pygame.draw.rect(self._display_surf, pygame.Color(0, 0, 0), pygame.Rect((0, 0, self.width, self.height)))
		
		self.atoms = [Atom(self) for i in range(100)]
		for atom in self.atoms:
			if not atom.drawn:
				pygame.draw.circle(self._display_surf, atom.color, atom.get_pos(), atom.radius)
				atom.drawn = True
		
		self.neutrons = []
		
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			selected_atoms = list(filter(lambda atom: atom.distance(mouse_pos) <= atom.radius, self.atoms))
			if len(selected_atoms) > 0:
				pygame.draw.circle(self._display_surf, pygame.Color(0, 0, 0), selected_atoms[0].get_pos(), selected_atoms[0].radius)
				self.atoms.remove(selected_atoms[0])
				self.neutrons.extend(selected_atoms[0].fission())
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_n:
				self.initialize_atoms()
			if event.key == pygame.K_ESCAPE:
				self._running = False
	
	def on_loop(self):
		for neutron in self.neutrons:
			pygame.draw.circle(self._display_surf, pygame.Color(0, 0, 0), neutron.get_pos(), 1)
			neutron.update_pos()
			
			neutron_pos = neutron.get_pos()
			if neutron_pos[0] <= 0 or neutron_pos[0] >= self.width or neutron_pos[1] <= 0 or neutron_pos[1] >= self.height:
				self.neutrons.remove(neutron)
			else:
				for jitter_h in [-1, 0, 1]:
					for jitter_v in [-1, 0, 1]:
						test_pos = neutron_pos + np.array([jitter_h, jitter_v])
						try:
							color = self._display_surf.get_at(test_pos)
						except:
							color = pygame.Color(0, 0, 0)
						if color != pygame.Color(0, 0, 0):
							impacted_atoms = list(filter(lambda atom: atom.distance(neutron.pos) <= atom.radius, self.atoms))
							for atom in impacted_atoms:
								pygame.draw.circle(self._display_surf, pygame.Color(0, 0, 0), atom.get_pos(), atom.radius)
								self.atoms.remove(atom)
								try:
									self.neutrons.remove(neutron)
								except ValueError:
									pass
								self.neutrons.extend(atom.fission())
	
	def on_render(self):
		for neutron in self.neutrons:
			pygame.draw.circle(self._display_surf, pygame.Color(255, 255, 255), neutron.get_pos(), 1)
				
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
