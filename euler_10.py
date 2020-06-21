import math, gmpy2, time

def sum_of_primes(threshold):

	primes = [2,3,5]
	n_test = 7
	step = 4

	while n_test < threshold:
		if gmpy2.is_prime(n_test):
			primes.append(n_test)
		n_test += step
		step = 2 if step==4 else 4

	return sum(primes)

print()
threshold = int(input('sum all primes < '))
start_time = time.time()
print(sum_of_primes(threshold))
print('runtime: %s sec' % (time.time() - start_time))
print()
