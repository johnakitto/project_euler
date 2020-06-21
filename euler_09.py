import time
start_time = time.time()

a, b = 1, 1
hit = False
while hit is False:
	b += 1
	for delta_a in range(b-a):
		if (((a+delta_a)**2 + b**2)**0.5) + (a+delta_a) + b == 1000:
			hit = True
			a += delta_a

print()
print('a,b,c = '+str(a)+','+str(b)+','+str(int((a**2 + b**2)**0.5)))
print('product of side lengths: '+ str(a * b * int(((a**2)+(b**2))**0.5)))
print('runtime: '+str(time.time()-start_time)+' sec')
print()
