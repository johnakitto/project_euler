import time
start_time = time.time()

print()
print('solution: '+ str(sum([x for x in range(1,1000) if x%3==0 or x%5==0])))
print('runtime: %s sec' % (time.time() - start_time))
print()
