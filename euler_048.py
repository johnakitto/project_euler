import time
start_time = time.time()

series_sum = 0
for n in range(1,1001):
	series_sum += n**n

print()
print('solution: '+str(series_sum)[-10:])
print('runtime: '+str(time.time() - start_time)+' sec')
print()
