import time, math

def string_of_primes(a,b):

	n = -1
	still_prime = True
	while still_prime:

		n += 1
		f = int((n**2) + (a*n) + b)

		if f < 2:
			break
		else:
			# test whether f is prime
			for factor in range(2,math.ceil((f**0.5)+1)):
				if f % factor == 0:
					still_prime = False
					break

	# return the length of the string of primes
	return(n)

def max_string_of_primes(x):

	longest_string = 0
	a_winner = b_winner = 0

	# test all the combinations of a and b coefficients
	for a in range(-x+1,x):
		for b in range(-x,x+1):
			if string_of_primes(a,b) > longest_string:
				longest_string = string_of_primes(a,b)
				a_winner, b_winner = a, b

	print('f(n) = n^2 + %dn + %d' % (a_winner, b_winner))
	print('generates %d consecutive primes' % (longest_string))
	print('a * b = '+ str(a_winner * b_winner))

print()
user = int(input('longest string of primes for |a| < '))
start_time = time.time()
max_string_of_primes(user)
print('runtime: %s' % (time.time() - start_time))
print()
