import time
start_time = time.time()

tri = lambda n: n*(n+1)//2
is_penta = lambda x: ((1+(1+24*x)**0.5)/6) % 1 == 0
is_hexa = lambda x: ((1+(1+8*x)**0.5)/4) % 1 == 0

n = 286
equivalence_found = False
while not equivalence_found:
	check_number = tri(n)
	if is_penta(check_number) and is_hexa(check_number):
		print()
		print('solution: '+str(check_number))
		equivalence_found = True
	n += 1

print('runtime: '+str(time.time() - start_time)+' sec')
print()
