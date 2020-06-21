import time, matplotlib.pyplot as plt

print()
threshold = int(input('how many powers of 2 do you want to print? '))
start_time = time.time()

sum_of_digits = [0] * (threshold+1)
number_of_digits = [0] * (threshold+1)
for number in range(threshold+1):
	power = 2 ** number
	sum_of_digits[number] = sum([int(digit) for digit in list(str(power))])
	number_of_digits[number] = len(str(power))
	# print(str(sum_of_digits[number])+', '+str(number_of_digits[number]))

fig = plt.figure(figsize=(6,8))
fig.subplots_adjust(left=0.15, right=0.95, top=0.9, hspace=.5)

sub1 = fig.add_subplot(2,1,1)
sub1.scatter(
	range(threshold+1),
	sum_of_digits,
	color='k',
	s=1
)
sub1.set_xlabel('Power of 2')
sub1.set_ylabel('Sum of Digits')
sub1.set_title('Sum of Digits vs. Power of 2')

sub2 = fig.add_subplot(2,1,2, sharex=sub1, sharey=sub1)
sub2.scatter(
	range(threshold+1),
	number_of_digits,
	color='b',
	s=1
)
sub2.set_xlabel('Power of 2')
sub2.set_ylabel('Number of Digits')
sub2.set_title('Number of Digits vs. Power of 2')

print('runtime: %s sec' % (time.time() - start_time))
print()
plt.show()
