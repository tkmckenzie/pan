import numpy as np
import os
import pickle as pkl
import pygame
from modules import *

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.width, self.height = 1440, 900
		
		self.clock = pygame.time.Clock()
		self.framerate = 60
		
		self.round_dict = {'num_atoms': [5, 10, 15, 25, 40, 55, 75, 100],
					 'required_explosions': [1, 3, 5, 10, 18, 30, 50, 75]}
		self.current_round = 0
		self.num_rounds = len(self.round_dict['num_atoms'])
		
		self.score = 0
		
		if 'gamedata.pkl' in os.listdir():
			with open('gamedata.pkl', 'rb') as f:
				self.gamedata = pkl.load(f)
		else:
			self.gamedata = {'high_score': 0}
		
	def on_init(self):
		self.initialize_pygame()
	
	def initialize_pygame(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size)
		self._running = True
		
		self.font = pygame.font.SysFont(None, 48)
	
	def initialize_objects(self, num_atoms):
		pygame.draw.rect(self._display_surf, pygame.Color(0, 0, 0), pygame.Rect((0, 0, self.width, self.height)))
		
		self.atoms = [Atom(self) for i in range(num_atoms)]
		for atom in self.atoms:
			pygame.draw.circle(self._display_surf, atom.color, atom.get_pos(), atom.get_radius())
		
		self.explosions = []
		
		self.explosion_triggered = False
		self.pause = False
		
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN and not self.explosion_triggered:
			mouse_pos = pygame.mouse.get_pos()
			self.explosions.append(Explosion(mouse_pos, None, self))
			self.explosion_triggered = True
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_n:
				self.score = 0
				self.current_round = 0
				self.begin_round()
			if event.key == pygame.K_r and not self.explosion_triggered:
				self.initialize_objects(self.round_dict['num_atoms'][self.current_round])
			if event.key == pygame.K_p:
				self.pause = not self.pause
			if event.key == pygame.K_ESCAPE:
				self._running = False
	
	def on_loop(self):
		for atom in self.atoms:
			pygame.draw.circle(self._display_surf, pygame.Color(0, 0, 0), atom.get_pos(), atom.get_radius())
			atom.update_pos()
			if any([atom.is_collison(explosion) for explosion in self.explosions]):
				self.explosions.append(atom.explode())
				self.atoms.remove(atom)
		
		for explosion in self.explosions:
			pygame.draw.circle(self._display_surf, pygame.Color(0, 0, 0), explosion.get_pos(), explosion.get_radius())
			explosion.update_radius()
			if explosion.nonexistent:
				self.explosions.remove(explosion)
				
		if self.explosion_triggered and len(self.explosions) == 0:
			self.on_round_end()
	
	def on_render(self):
		for atom in self.atoms:
			pygame.draw.circle(self._display_surf, atom.color, atom.get_pos(), atom.get_radius())
		
		for explosion in self.explosions:
			pygame.draw.circle(self._display_surf, explosion.color, explosion.get_pos(), explosion.get_radius())
		
		pygame.display.flip()
		
	def draw_text(self, text_list):
		num_lines = len(text_list)
		self._display_surf.fill((0, 0, 0))
		
		for i in range(num_lines):
			text = text_list[i]
			text = self.font.render(text, True, (255, 255, 255), (0, 0, 0))
			text_rect = text.get_rect()
			text_rect.centerx = self._display_surf.get_rect().centerx
			text_rect.centery = self._display_surf.get_rect().centery + int(48 * ((2 * i + 1) - num_lines) / 2)
			
			self._display_surf.blit(text, text_rect)
		pygame.display.flip()
		
		self.wait_for_click()
		self._display_surf.fill((0, 0, 0))
		pygame.display.flip()
		
	def wait_for_click(self):
		while self._running:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					return True
				if event.type == pygame.QUIT:
					self._running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self._running = False
	
	def begin_round(self):
		self.draw_text(['Need %i/%i explosions' % (self.round_dict['required_explosions'][self.current_round], self.round_dict['num_atoms'][self.current_round]), 'Current score: %i' % self.score])
		self.initialize_objects(self.round_dict['num_atoms'][self.current_round])
	
	def on_round_end(self):
		num_explosions = self.round_dict['num_atoms'][self.current_round] - len(self.atoms)
		self.draw_text(['%i/%i needed explosions occurred' % (num_explosions, self.round_dict['required_explosions'][self.current_round])])
		self.score += num_explosions
		
		if self.current_round == (self.num_rounds - 1) or num_explosions < self.round_dict['required_explosions'][self.current_round]:
			message = ['Game over']
			if self.score > self.gamedata['high_score']:
				self.gamedata['high_score'] = self.score
				with open('gamedata.pkl', 'wb') as f:
					pkl.dump(self.gamedata, f)
				message += ['New high score!!!']
			message += ['Score: %i' % self.score, 'High score: %i' % self.gamedata['high_score']]
			self.draw_text(message)
			
			self.score = 0
			self.current_round = 0
		else:
			self.current_round += 1
		
		self.begin_round()
	
	def on_cleanup(self):
		pygame.quit()
		
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
		
		self.begin_round()
		
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
