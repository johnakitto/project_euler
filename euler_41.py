import time, gmpy2, itertools as it
start_time = time.time()

def largest_pandigital_prime(digits):

	largest_prime = None
	for pandigital in it.permutations(digits):
		if gmpy2.is_prime(int(''.join(pandigital))):
			largest_prime = ''.join(pandigital)
			break

	return largest_prime

digits = '987654321'
pandigital_prime_found = False
while not pandigital_prime_found:
	if largest_pandigital_prime(digits) != None:
		pandigital_prime_found = True
		print()
		print('largest pandigital prime: '+ largest_pandigital_prime(digits))
	digits = digits[1:]

print('runtime: %s sec' % (time.time() - start_time))
print()
