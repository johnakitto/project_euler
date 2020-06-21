import time
start_time = time.time()

biggest = 0
for n1 in range(100,1000):
	for n2 in range(n1,1000):
		x = n1 * n2
		if str(x) == str(x)[::-1]:
			if x > biggest:
				biggest = x

print()
print('solution: '+ str(biggest))
print('runtime: %s sec' % (time.time() - start_time))
print()
