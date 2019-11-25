import numpy as np
import pygame
import random

init_radius = 10

class GameObject:
	def get_pos(self):
		return(np.int32(np.round(self.pos)))
		
	def get_radius(self):
		return(int(np.round(self.radius)))
		
	def distance(self, other):
		return np.sqrt(sum((self.pos - other.pos)**2))
		
	def draw_color(self):
		return pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	
	def is_collison(self, other):
		if self.distance(other) <= self.radius + other.radius:
			return True
		else:
			return False

class Atom(GameObject):
	def __init__(self, App):
		self.App = App
		
		self.radius = float(init_radius)
		
		self.pos = np.array([float(random.randint(self.radius, App.size[0] - self.radius)), float(random.randint(self.radius, App.size[1] - self.radius))])
		
		self.velocity_abs = 90 / App.framerate
		self.velocity_vec = np.array([random.random() * 2 - 1, random.random() * 2 - 1])
		self.velocity_vec *= self.velocity_abs / np.sqrt(sum(self.velocity_vec**2))
		
		self.color = self.draw_color()
		
	def update_pos(self):
		self.pos += self.velocity_vec * (1 - self.App.pause)
		
		if self.pos[0] <= self.radius:
			self.pos[0] = 2 * self.radius - self.pos[0]
			self.velocity_vec[0] *= -1
		elif self.pos[0] >= self.App.width - self.radius:
			self.pos[0] = 2 * (self.App.width - self.radius) - self.pos[0]
			self.velocity_vec[0] *= -1
		
		if self.pos[1] <= self.radius:
			self.pos[1] = 2 * self.radius - self.pos[1]
			self.velocity_vec[1] *= -1
		elif self.pos[1] >= self.App.height - self.radius:
			self.pos[1] = 2 * (self.App.height - self.radius) - self.pos[1]
			self.velocity_vec[1] *= -1
	
	def explode(self):
		return Explosion(self.pos, self.color, self.App)

class Explosion(GameObject):
	def __init__(self, pos, color, App):
		self.App = App
		
		self.pos = np.array(pos)
		
		self.radius = float(init_radius)
		self.max_radius = 15 * self.radius
		
		self.radius_velocity = 1.5 * 90 / App.framerate
		self.radius_growing = True
		self.radius_stationary = False
		self.radius_shrinking = False
		
		self.nonexistent = False
		
		self.radius_stationary_duration = 75
		
#		self.color = self.draw_color()
		if color == None:
			self.color = self.draw_color()
		else:
			self.color = color
	
	def update_radius(self):
		if self.radius_growing:
			self.radius += self.radius_velocity * (1 - self.App.pause)
			if self.radius >= self.max_radius:
				self.radius = self.max_radius
				self.radius_growing = False
				self.radius_stationary = True
				self.radius_stationary_period = 0
		elif self.radius_stationary:
			self.radius_stationary_period += 1 * (1 - self.App.pause)
			if self.radius_stationary_period >= self.radius_stationary_duration:
				self.radius_stationary = False
				self.radius_shrinking = True
		else:
			self.radius -= self.radius_velocity * (1 - self.App.pause)
			if self.radius <= 0:
				self.radius = 0
				self.nonexistent = True
		
#		self.color = self.draw_color()
	