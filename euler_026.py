import time, matplotlib.pyplot as plt

print()
largest_divisor = int(input('check integer divisors of 1 less than: '))
start_time = time.time()

dividend = 1
divisor_with_longest_repeating_decimal = 0
longest_repeating_length = 0
repeating_lengths = [0]

for divisor in range(1, largest_divisor+1):

	answer, remainders, repeating_length = [], [1], -1
	while repeating_length == -1:

		digit = len(remainders)
		temp_dividend = remainders[digit-1]
		while temp_dividend < divisor:
			temp_dividend *= 10
		answer.append(temp_dividend // divisor)
		remainders.append(temp_dividend % divisor)

		if remainders[digit] == 0:
			repeating_length = 0
		elif remainders[digit] in remainders[:digit-1]:
			repeating_length = digit - remainders.index(remainders[digit])

	repeating_lengths.append(repeating_length)
	if repeating_length > longest_repeating_length:
		divisor_with_longest_repeating_decimal = divisor
		longest_repeating_length = repeating_length

print('dividend = '+ str(dividend))
print('divisor with longest repeating decimal = '+ str(divisor_with_longest_repeating_decimal))
print('repeating decimal length = '+ str(longest_repeating_length))
print('runtime: %s sec' % (time.time() - start_time))
print()

plt.scatter(
	list(range(len(repeating_lengths))),
	repeating_lengths,
	color='k',
	s=2)
plt.xlabel('Divisor (d)')
plt.ylabel('Longest Recurring Decimal Sequence (Digits)')
plt.title('Recurring Decimal Sequences of 1/d\n')
plt.show()
