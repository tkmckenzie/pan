import numpy as np
from primes import sieve
from scipy.special import expi

def li(x):
	return expi(np.log(x))
li_2 = li(2)
def prime_count_approx(x):
#	return li(x) - li_2
	return x / np.log(x)

def square_range(side_length):
	# Gives largest number in square with sides equal to side_length
	return side_length**2
def num_diagonals(side_length):
	if side_length < 1:
		return 0
	elif side_length == 1:
		return 1
	else:
		side_length = 2 * np.floor((side_length - 1) / 2) + 1 # Making sure side_length is an odd integer
		num_layers = (side_length - 1) / 2
		return 1 + 4 * num_layers

def is_lower_right(n):
	s = np.sqrt(n)
	s_reduc = (s - 1) / 2
	return s_reduc == np.floor(s_reduc)
def is_lower_left(n):
	s = (1 + np.sqrt(4 * n - 3)) / 2
	s_reduc = (s - 1) / 2
	return s_reduc == np.floor(s_reduc)
def is_upper_left(n):
	s = 1 + np.sqrt(n - 1)
	s_reduc = (s - 1) / 2
	return s_reduc == np.floor(s_reduc)
def is_upper_right(n):
	s = (3 + np.sqrt(4 * n - 3)) / 2
	s_reduc = (s - 1) / 2
	return s_reduc == np.floor(s_reduc)

def diagonal_primes(side_length):
	primes = np.array(sieve(square_range(side_length)))
	is_diagonal = is_lower_right(primes) | is_lower_left(primes) | is_upper_left(primes) | is_upper_right(primes)
	return primes[is_diagonal]
def num_diagonal_primes(side_length):
	primes = np.array(sieve(square_range(side_length)))
	is_diagonal = is_lower_right(primes) | is_lower_left(primes) | is_upper_left(primes) | is_upper_right(primes)
	return sum(is_diagonal)
def proportion_diagonal_primes(side_length):
	return num_diagonal_primes(side_length) / num_diagonals(side_length)

def proportion_diagonal_primes_approx(side_length):
	num_primes_approx = prime_count_approx(square_range(side_length))
	num_diags = num_diagonals(side_length)
	num_primes_diags_approx = num_primes_approx * num_diags / square_range(side_length)
	return num_primes_diags_approx / num_diags
