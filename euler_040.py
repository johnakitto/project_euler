import time
start_time = time.time()

decimal_concatenation = ''.join(str(i) for i in range(1,1000000))
champernowne = 1
for i in [(10**i)-1 for i in range(7)]:
	champernowne *= int(decimal_concatenation[i])

print()
print('champernowne constant: '+ str(champernowne))
print('runtime: %s sec' % (time.time() - start_time))
print()
