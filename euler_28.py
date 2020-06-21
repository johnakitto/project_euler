import time

print()
width = int(input('sum of diagonals for spiral of width: '))
while width % 2 == 0:
	width = int(input('spiral width must be odd: '))
start_time = time.time()

total = 1
gap_size = 0
diagonal_number = 1
while diagonal_number < width**2:
	gap_size += 2
	for i in range(4):
		diagonal_number += gap_size
		total += diagonal_number

print('sum of diagonals: '+ str(total))
print('runtime: %s sec' % (time.time() - start_time))
print()
