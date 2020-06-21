import time
start_time = time.time()

sum_of_fifths = []
for number in range(2, ((9**5)*6)+1):
	sum_of_digits = 0
	for i in range(len(str(number))):
		sum_of_digits += int(str(number)[i])**5
	if sum_of_digits == number:
		sum_of_fifths.append(number)

print()
print('solution: '+ str(sum(sum_of_fifths)))
print('runtime: %s sec' % (time.time() - start_time))
print()
