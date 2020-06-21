import time
start_time = time.time()

pandigital_products = []
for a in range(1,100):
	for b in range(100,10000):
		if sorted([int(digit) for digit in str(a)+str(b)+str(a*b)]) == list(range(1,10)):
			pandigital_products.append(a*b)

print()
print('solution: '+ str(sum(set(pandigital_products))))
print('runtime: %s sec' % (time.time() - start_time))
print()
