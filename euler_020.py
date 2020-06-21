import time, math
start_time = time.time()

print()
print('solution: '+ str(sum(int(d) for d in str(math.factorial(100)))))
print('runtime: %s sec' % (time.time() - start_time))
print()
