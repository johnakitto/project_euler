import time, numpy as np
start_time = time.time()

r0 = [0,3,6,6,5,5,5,7,6,6]
r1 = [3,6,9,9,8,8,8,10,9,9]
r2 = [3,6,9,9,8,8,8,10,9,9]
r3 = [5,8,11,11,10,10,10,12,11,11]
r4 = [4,8,10,10,9,9,9,11,10,10]
r5 = [4,7,10,10,9,9,9,11,10,10]
r6 = [3,7,9,9,8,8,8,10,9,9]
r7 = [5,9,11,11,10,10,10,12,11,11]
r8 = [5,8,11,11,10,10,10,12,11,11]
r9 = [4,8,10,10,9,9,9,11,10,10]

D = np.matrix([r0,r1,r2,r3,r4,r5,r6,r7,r8,r9])

l = 11
for n in range(1,1000):
	if n < 10:
		l += D[n,0]
	elif n >= 10 and n < 100:
		l += D[int(str(n)[1]),int(str(n)[0])]
	elif n >= 100 and n < 1000 and n % 100 != 0:
		l += D[int(str(n)[0]),0] + 10 + D[int(str(n)[2]),int(str(n)[1])]
	else:
		l += D[int(str(n)[0]),0] + 7 + D[int(str(n)[2]),int(str(n)[1])]

print()
print('solution: '+ str(l))
print('runtime: %s sec' % (time.time() - start_time))
print()
