import gmpy2, time, collections, itertools
start_time = time.time()

def prime_arithmetic_sequence(prime):
	''' returns list of prime arithmetic sequence if one exists '''

	all_permutations = set(int(''.join(d)) for d in itertools.permutations(str(prime)))
	prime_permutations = sorted([n for n in all_permutations if gmpy2.is_prime(n) and n>=1000])
	if len(prime_permutations) < 3:
		return []

	difference_dict = {}
	for i in range(len(prime_permutations)-1):
		for j in range(i+1, len(prime_permutations)):
			small_prime, big_prime = prime_permutations[i], prime_permutations[j]
			difference_text = str(big_prime)+'-'+str(small_prime)
			difference_dict[difference_text] = big_prime - small_prime

	difference_counts = collections.Counter(difference_dict.values())
	differences_to_check = []
	for difference, count in difference_counts.items():
		if count == 2:
			differences_to_check.append(difference)

	for difference_to_check in differences_to_check:
		potential_sequence = []
		for text, difference in difference_dict.items():
			if difference == difference_to_check:
				potential_sequence.append(text)
		potential_sequence_set = sorted(set(int(i) for i in '-'.join(potential_sequence).split('-')))
		if len(potential_sequence_set) == 3:
			return potential_sequence_set

	return []

n = 1013
sequence_found = False
while not sequence_found:
	if gmpy2.is_prime(n):
		sequence = prime_arithmetic_sequence(n)
		if len(sequence) > 0 and sequence != [1487, 4817, 8147]:
				sequence_found = True
				print()
				print('solution: '+str(sequence))
				print('runtime: '+str(time.time() - start_time)+' sec')
				print()

	n = n+4 if str(n)[-1]==3 else n+2
