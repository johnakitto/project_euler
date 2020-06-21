import time, numpy as np
start_time = time.time()

r0  = '75'.split()
r1  = '95 64'.split()
r2  = '17 47 82'.split()
r3  = '18 35 87 10'.split()
r4  = '20 04 82 47 65'.split()
r5  = '19 01 23 75 03 34'.split()
r6  = '88 02 77 73 07 63 67'.split()
r7  = '99 65 04 28 06 16 70 92'.split()
r8  = '41 41 26 56 83 40 80 70 33'.split()
r9  = '41 48 72 33 47 32 37 16 94 29'.split()
r10 = '53 71 44 65 25 43 91 52 97 51 14'.split()
r11 = '70 11 33 28 77 73 17 78 39 68 17 57'.split()
r12 = '91 71 52 38 17 14 91 43 58 50 27 29 48'.split()
r13 = '63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split()
r14 = '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split()

T = np.array([r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14])

for i in range(len(T)):
	for j in range(len(T[i])):
		T[i][j] = int(T[i][j])

def best_path(i):
	if i < 0:
		print('solution: '+ str(T[0][0]))
	else:
		for j in range(len(T[i])):
			if T[i+1][j] >= T[i+1][j+1]:
				T[i][j] += T[i+1][j]
			else:
				T[i][j] += T[i+1][j+1]
		best_path(i-1)

print()
best_path(13)
print('runtime: %s sec' % (time.time() - start_time))
print()
