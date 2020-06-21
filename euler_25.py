import time

print()
digits = int(input('the first Fibonacci number with how many digits? '))
start_time = time.time()

F1 = F2 = 1
Fi = 2
index = 2
while len(str(Fi)) < digits:
	index += 1
	Fi = F1 + F2
	F1 = F2
	F2 = Fi

print('index: '+ str(index))
print('runtime: %s sec' % (time.time() - start_time))
print()
