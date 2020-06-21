import time, math
start_time = time.time()

abundant_numbers = []
for n in range(5,28124):
	count = 1

	if n**0.5 % 1 == 0:
		count += int(n**0.5)
		for d in range(2, math.floor(n**0.5)):
			if n % d == 0:
				count += int(d) + int(n/d)
	else:
		for d in range(2, math.floor(n**0.5)+1):
			if n % d == 0:
				count += int(d) + int(n/d)

	if count > n:
		abundant_numbers.append(n)

abundant_sums = []
for i in range(len(abundant_numbers)):
	for j in range(i+1):
		abundant_sum = abundant_numbers[i] + abundant_numbers[j]
		if abundant_sum < 28124:
			abundant_sums.append(abundant_sum)

non_abundant_sums = list(set(range(1,28124)) - set(abundant_sums))

print()
print('sum of all numbers not the sum of 2 abundant numbers: '+ str(sum(non_abundant_sums)))
print('largest number not the sum of 2 abundant numbers: '+ str(max(non_abundant_sums)))
print('runtime: %s sec' % (time.time() - start_time))
print()
