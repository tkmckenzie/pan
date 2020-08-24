import keras as k
import numpy as np
import tensorflow as tf
import TSP

# Read graph data
names = [0, 1, 2, 3, 4]
distance_matrix = [[0, 2, 10000, 12, 5],
				   [2, 0, 4, 8, 10000],
				   [10000, 4, 0, 3, 3],
				   [12, 8, 3, 0, 10],
				   [5, 10000, 3, 10, 0]]
graph = TSP.Graph(names, distance_matrix, 0, 0)

# Path generator network
path_generator = k.Sequential([k.layers.Dense(48 * 16, use_bias = False, input_shape = (100,)),
							   k.layers.BatchNormalization(),
							   k.layers.LeakyReLU(),
							   
							   k.layers.Dense(48 * 4, use_bias = False),
							   k.layers.BatchNormalization(),
							   k.layers.LeakyReLU(),
							   
							   k.layers.Dense(48 * 1, use_bias = False, activation = 'sigmoid')
		])

# Loss function and optimizer
mean_abs_error = k.losses.MAE
def generator_loss(output_vector):
	return mean_abs_error(tf.zeros_like(output_vector), output_vector)

generator_optimizer = k.optimizers.Adam(1e-4)

# Setting up optimization
epochs = 50
batch_size = 256
noise_dim = 100

def train_step():
	noise = tf.random_normal([batch_size, noise_dim])
	with tf.GradientTape() as tape:
		generator_output = path_generator(noise)
		
		gen_loss = generator_loss(generator_output)
	gradients = tape.gradient(gen_loss, path_generator.trainable_weights)
	generator_optimizer.get_update
		