import gmpy2, math, time
start_time = time.time()

# THIS IS EXTREMELY INEFFICIENT

def distinct_prime_factors(x, distinct_primes):

	prime_factors = []

	if x % 2 == 0:
		prime_factors.append(2)
		for n in range(4,x,2):
			if x % n == 0:
				if gmpy2.is_prime(x//n):
					prime_factors.append(x//n)
					number_of_prime_factors = len(set(prime_factors))
					if number_of_prime_factors > distinct_primes:
						return number_of_prime_factors

	if x % 3 == 0:
		prime_factors.append(3)

	for n in range(5,x,6):
		if x % n == 0:
			if gmpy2.is_prime(n):
				prime_factors.append(n)
				number_of_prime_factors = len(set(prime_factors))
				if number_of_prime_factors > distinct_primes:
					return number_of_prime_factors

	for n in range(7,x,6):
		if x % n == 0:
			if gmpy2.is_prime(n):
				prime_factors.append(n)
				number_of_prime_factors = len(set(prime_factors))
				if number_of_prime_factors > distinct_primes:
					return number_of_prime_factors

	return len(set(prime_factors))

n = 2
distinct_primes = 4
consecutive_numbers = []
while len(consecutive_numbers) < distinct_primes:

	print(n, end='\r')

	if consecutive_numbers != []:
		if n > consecutive_numbers[-1] + 1:
			consecutive_numbers = []

	if distinct_prime_factors(n, distinct_primes) == distinct_primes:
		consecutive_numbers.append(n)

	n += 1

print()
print('solution: '+str(consecutive_numbers[0]))
print('runtime: '+str(time.time() - start_time)+' sec')
print()
