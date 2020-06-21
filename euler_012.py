import time, math

def triangle_numbers(threshold):

	start, factors, = 1, 2
	while factors <= threshold:

		triangle_number = 0
		start += 1
		factors = 2

		for n in range(1, start+1):
			triangle_number += n

		sqrt = math.sqrt(triangle_number)
		if triangle_number % sqrt == 0:
			factors += 1
			for n in range(2, math.ceil(sqrt)):
				if triangle_number % n == 0:
					factors += 2
		else:
			for n in range(2, math.floor(sqrt)+1):
				if triangle_number % n == 0:
					factors += 2

	return (triangle_number, factors)

print()
threshold = int(input('enter n for the 1st triangle # with > n factors: '))
start_time = time.time()
solution = triangle_numbers(threshold)
print('%d has %d factors' % (solution[0], solution[1]))
print('runtime: %s sec' % (time.time() - start_time))
print()
