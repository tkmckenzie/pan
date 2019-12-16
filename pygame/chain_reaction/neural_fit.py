from chain_reaction import *
from modules import *

import keras
import numpy as np
import pygame

class InputGenerator(object):
	def __init__(self, num_atoms):
		self.App = App()
		self.num_atoms = num_atoms
	
	def __iter__(self):
		return self
	
	def __next__(self):
		self.atoms = [Atom(self.App) for i in range(self.num_atoms)]

class SimulationLayer(keras.layers.Layer):
	def __init__(self, input_generator, **kwargs):
		self.input_generator = input_generator
		super(SimulationLayer, self).__init__(**kwargs)
	
	def build(self, input_shape):
		if input_shape[1] != 2: raise ValueError('Input to SimulationLayer must have dimension 2.')
		super(SimulationLayer, self).build(input_shape)
	
	def call(self, x):
		explosion_pos = x * self.input_generator.App.size
		
		atoms_copy = list(map(lambda atom: atom.__copy__(), self.input_generator.atoms))
		explosions = [Explosion(explosion_pos, pygame.Color(0, 0, 0), self.input_generator.App)]
		
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
		
		num_explosions = len(self.input_generator.atoms) - len(atoms_copy)
		
		return num_explosions

num_atoms = 25
input_generator = InputGenerator(num_atoms)
input_generator.__next__()

model = keras.Sequential([
	keras.layers.Conv2D(filters = num_atoms * 2, kernel_size = (1, 1), input_shape = (num_atoms, 2, 2), data_format = 'channels_last'),
	keras.layers.Conv2D(filters = num_atoms * 2, kernel_size = (1, 1)),
	keras.layers.MaxPool2D(),
	keras.layers.Dropout(0.25),
	
	keras.layers.Flatten(),
	keras.layers.Dense(num_atoms * 4, activation = 'relu'),
	
	keras.layers.Dense(2, activation = 'sigmoid'),
	
	SimulationLayer(input_generator)
])
model.compile(optimizer = 'rmsprop',
			  loss = 'categorical_crossentropy',
			  metrics = ['accuracy'])