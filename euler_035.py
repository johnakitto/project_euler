import math, gmpy2, time

def circular_primes(threshold):

	circular_primes = [2,3,5,7]
	n_test = 11
	step = 2

	while n_test < threshold:

		if gmpy2.is_prime(n_test):

			circular_prime = True
			n = str(n_test)
			for offset in range(1, len(n)):

				n_new = ''
				for index in range(len(n)):
					n_new += n[(index+offset) % len(n)]

				if not gmpy2.is_prime(int(n_new)):
					circular_prime = False
					break

			if circular_prime:
				circular_primes.append(n_test)

		n_test += step
		step = 2 if step==4 else 4

	return len(circular_primes)

print()
threshold = int(input('number of cicular primes < '))
start_time = time.time()
print('solution: '+ str(circular_primes(threshold)))
print('runtime: %s sec' % (time.time() - start_time))
print()
