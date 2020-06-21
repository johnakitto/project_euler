import gmpy2, time
start_time = time.time()

is_square = lambda n,p: ((n-p)/2)**0.5 % 1 == 0

n = 9
primes = [2,3,5,7]
goldbach_is_right = True
while goldbach_is_right:
	if gmpy2.is_prime(n):
		primes.append(n)
	n += 2
	if not gmpy2.is_prime(n):
		goldbach_is_right = False
		for prime in primes:
			if is_square(n,prime):
				goldbach_is_right = True
				break

print()
print('solution: '+str(n))
print('runtime: '+str(time.time() - start_time)+' sec')
print()
