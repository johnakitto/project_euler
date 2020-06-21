import time, math
start_time = time.time()

# INEFFICIENT SOLUTION (TAKES ~23 SECONDS)
curious_numbers = [n for n in range(10**7) if sum([math.factorial(int(i)) for i in str(n)]) == n]

print()
print('solution: '+ str(sum(curious_numbers)))
print('runtime: %s sec' % (time.time() - start_time))
print()
