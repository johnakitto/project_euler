import time

print()
threshold = int(input('sum of palindromic n in base10 and base2 for n < '))
start_time = time.time()

double_base_palidromes = []
for n in range(threshold):
	if str(n) == ''.join(reversed(str(n))):
		if bin(n)[2:] == ''.join(reversed(bin(n)[2:])):
			double_base_palidromes.append(n)

print('solution: ' +str(sum(double_base_palidromes)))
print('runtime: %s sec' % (time.time() - start_time))
print()
