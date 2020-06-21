import time

print()
max_divisor = int(input('Smallest number divisible by 1,2,3,...,'))
start_time = time.time()

dividend, found = 0, False
while not found:
	dividend += max_divisor
	found = True
	for divisor in range(max_divisor, 1, -1):
		if dividend % divisor != 0:
			found = False
			break

print('solution: '+ str(dividend))
print('runtime: %s sec' % (time.time() - start_time))
print()
