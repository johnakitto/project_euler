import math, gmpy2, time

def nth_prime(n):

	primes = [2,3,5]
	n_test = 7
	step = 4

	while len(primes) < n:

		# Miller-Rabin Primality Test
		if gmpy2.is_prime(n_test):
			primes.append(n_test)

		n_test += step
		step = 2 if step==4 else 4

	return primes[-1]

print()
n = int(input('enter n for the nth prime: '))
start_time = time.time()
print('solution: '+ str(nth_prime(n)))
print('runtime: %s sec' % (time.time() - start_time))
print()
