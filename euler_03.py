import math, gmpy2, time

# THIS IS INCORRECT (TRY 645)
def prime_factors(x):

	sqrt_x = math.ceil(x**0.5)
	factors, prime_factors = [], []

	if x % 2 == 0:
		factors.append(2)
		prime_factors.append(2)
		factors.append(x//2)
		for n in range(4,sqrt_x,2):
			if x % n == 0:
				factors.append(n)
				factors.append(x//n)

	if x % 3 == 0:
		factors.append(3)
		factors.append(int(x/3))

	for n in range(5,sqrt_x,6):
		if x % n == 0:
			factors.append(n)
			factors.append(x//n)

	for n in range(7,sqrt_x,6):
		if x % n == 0:
			factors.append(n)
			factors.append(x//n)

	for factor in factors:

		# Miller-Rabin primality test
		if gmpy2.is_prime(factor):
			prime_factors.append(factor)

	return sorted(prime_factors)

print()
number_to_factor = int(input('enter number: '))
start_time = time.time()
prime_factorization = prime_factors(number_to_factor)

print('prime factors:')
print(prime_factorization)
print('runtime: '+str(time.time() - start_time)+' sec')
print()
