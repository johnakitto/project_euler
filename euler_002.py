import time
start_time = time.time()

fibonacci = [1,2]
while fibonacci[-1] <= 4000000:
	fibonacci.append(fibonacci[-1]+fibonacci[-2])

print()
print('solution: '+ str(sum([x for x in fibonacci if x%2==0])))
print('runtime: %s sec' % (time.time() - start_time))
print()
