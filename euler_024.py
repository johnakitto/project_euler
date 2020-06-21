import time, math
start_time = time.time()

n = 1000000
digits = [0,1,2,3,4,5,6,7,8,9]
num_digits = len(digits)
answer = [0,0,0,0,0,0,0,0,0,0]

answer[0] = math.floor(num_digits * n/math.factorial(num_digits))
digits.remove(answer[0])
# The above logic only works if d=10. Rethink this for generic d

for i in range(1, num_digits):
	count = 0
	for item in digits:
		if item < answer[i-1]:
			count += 1
		else:
			break

	numerator = n - (count * math.factorial(num_digits-i))
	denominator = math.factorial(num_digits-i)

	j = 0
	while (numerator / denominator) > (j / (num_digits-i)):
		answer[i] = digits[j]
		j += 1

	digits.remove(int(answer[i]))
	n = numerator

print()
print('millionth: '+''.join(str(i) for i in answer))
print('runtime: %s sec' % (time.time() - start_time))
print()
