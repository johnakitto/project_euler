import gmpy2, time
start_time = time.time()

truncatable_primes = []
n_test = 11
step = 2

while len(truncatable_primes) < 11:

	if gmpy2.is_prime(n_test):
		truncatable_prime = True
		for i in range(1, len(str(n_test))):
			if not gmpy2.is_prime(int(str(n_test)[i:])) or \
			not gmpy2.is_prime(int(str(n_test)[:-i])):
				truncatable_prime = False
				break

		if truncatable_prime:
			truncatable_primes.append(n_test)

	n_test += step
	step = 2 if step==4 else 4

print()
print('sum of left/right truncatable primes: '+ str(sum(truncatable_primes)))
print('runtime: %s sec' % (time.time() - start_time))
print()
