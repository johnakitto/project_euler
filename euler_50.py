import time, gmpy2
start_time = time.time()

def primes_below(n):
	''' returns list of primes < n '''

	primes = [2,3,5]
	n_test, step_size = 7, 4

	while primes[-1] < n:
		if gmpy2.is_prime(n_test):
			primes.append(n_test)
		n_test += step_size
		step_size = 2 if step_size==4 else 4

	return primes[:-1]


def consecutive_prime_sums(primes):
	''' returns dict of longest consecutive prime sum for each prime '''

	largest_prime, number_of_primes = max(primes), len(primes)
	prime_sum_terms = {prime: [] for prime in primes}

	for i in range(number_of_primes):
		for terms in range(2, number_of_primes-i):

			consecutive_sum = 0
			term_list = []
			for k in range(i, i+terms):
				consecutive_sum += primes[k]
				term_list.append(primes[k])

			if consecutive_sum > largest_prime:
				break

			if gmpy2.is_prime(consecutive_sum):
				if len(prime_sum_terms[consecutive_sum]) < terms:
					prime_sum_terms[consecutive_sum] = term_list

	return prime_sum_terms

prime_sums = consecutive_prime_sums(primes_below(10**6))
prime_with_longest_prime_sum = max(prime_sums, key=lambda key: len(prime_sums[key]))
terms = prime_sums[prime_with_longest_prime_sum]

solution_text =  str(prime_with_longest_prime_sum)+' = '
solution_text += str(terms[0])+'+'+str(terms[1])+'+...+'+str(terms[-1])
solution_text += ' ('+str(len(terms))+' terms)'

print()
print('solution: '+solution_text)
print('runtime: '+str(time.time() - start_time)+' sec')
print()
