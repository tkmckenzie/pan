import numpy as np
import pygame
import random

class GameObject:
	def get_pos(self):
		return(np.int32(np.round(self.pos)))

class Atom(GameObject):
	def __init__(self, App):
		self.App = App
		
		self.radius = 10
		self.pos = np.array([float(random.randint(self.radius, App.size[0] - self.radius)), float(random.randint(self.radius, App.size[1] - self.radius))])
		self.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
		self.drawn = False
		
		self.num_neutrons = 10
	
	def distance(self, other_pos):
		return np.sqrt((self.pos[0] - other_pos[0])**2 + (self.pos[1] - other_pos[1])**2)
	
	def fission(self):
		return [Neutron(self.pos, self.App) for i in range(self.num_neutrons)]

class Neutron(GameObject):
	def __init__(self, init_pos, App):
		self.pos = np.array(init_pos)
		self.velocity_abs = 60 / App.framerate
		
		self.velocity_vec = np.array([random.random() * 2 - 1, random.random() * 2 - 1])
		self.velocity_vec *= self.velocity_abs / np.sqrt(sum(self.velocity_vec**2))
	
	def update_pos(self):
		self.pos += self.velocity_vec
	