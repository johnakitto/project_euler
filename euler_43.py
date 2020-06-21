import time, itertools as it
start_time = time.time()

first_7_primes = [2,3,5,7,11,13,17]
pandigitals = [''.join(x) for x in it.permutations('0123456789') if x[0]!='0']

special_pandigitals = []
for pandigital in pandigitals:
	special = True
	for i in range(1,8):
		if int(pandigital[i]+pandigital[i+1]+pandigital[i+2]) % first_7_primes[i-1] != 0:
			special = False
			break
	if special:
		special_pandigitals.append(int(pandigital))

print()
print('sum of special pandigitals: '+ str(sum(special_pandigitals)))
print('runtime: '+str(time.time() - start_time)+' sec')
print()
