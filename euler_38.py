import time
start_time = time.time()

largest_pandigital_product = 0
digits_1_to_9 = list(range(1,10))
for n in range(10000):

	concatenated_product = str(n)
	multiplier = 2
	move_to_next_n = False
	while len(concatenated_product) < 9:

		if '0' in concatenated_product:
			move_to_next_n = True
			break
		elif sorted(concatenated_product) != sorted(set(concatenated_product)):
			move_to_next_n = True
			break

		concatenated_product += str(n * multiplier)
		multiplier += 1

	if move_to_next_n:
		continue

	if [int(i) for i in sorted(concatenated_product)] == digits_1_to_9:
		if int(concatenated_product) > largest_pandigital_product:
			largest_pandigital_product = int(concatenated_product)
			corresponding_integer = n

print()
print('largest pandigital product: '+ str(largest_pandigital_product))
print('corresponding integer n: '+ str(corresponding_integer))
print('runtime: %s sec' % (time.time() - start_time))
print()
