import time
start_time = time.time()

penta = lambda n: n*(3*n-1)//2
is_penta = lambda x: ((1+(1+24*x)**0.5)/6) % 1 == 0

pentas = [1,5,12]
penta_found = False
while not penta_found:
	j = len(pentas)-2
	for i in range(j):
		if is_penta(pentas[j]+pentas[i]) and is_penta(pentas[j]-pentas[i]):
			print()
			print(pentas[i], pentas[j], pentas[j]-pentas[i])
			penta_found = True
			break
	pentas.append(penta(len(pentas)+1))

# Why does finding the first instance of this phenomenon
# guarantee the difference between the pentagonal numbers
# is minimized?

print('runtime: '+str(time.time() - start_time)+' sec')
print()
