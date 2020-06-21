import time, numpy as np, matplotlib.pyplot as plt

def collatz(x):

	lengths = [-1] * (x+1)
	total_steps_saved = 0

	# maybe you should start at x and work backwards instead?
	for number in range(2,x+1):
		steps = steps_saved = 0
		i = number
		if lengths[number] == 0:
			# print('---------')
			continue
		else:
			while i != 1:

				if i < number and lengths[i] != 0:
					steps += lengths[i]
					steps_saved = lengths[i]
					break
				elif i > number and i <= x:
					lengths[i] = 0

				if i % 2 == 0:
					i = i // 2
					steps += 1
				else:
					i = ((3*i)+1) // 2
					steps += 2

			lengths[number] = steps
			total_steps_saved += steps_saved
			# print('(%d, %d, %d)' % (number, steps, steps_saved))

	winning_number = np.argmax(lengths)
	winning_chain = max(lengths)
	print()
	print('winner: %d' % (winning_number))
	print('chain: %d' % (winning_chain))
	print('steps saved: %d' % (total_steps_saved))

	plt.scatter(range(x+1), lengths, color='k', s=1)
	plt.xlabel('Starting Number')
	plt.ylabel('Iterations to 1')
	plt.title('Collatz Conjecture: Iterations vs. Starting Number\n')

print()
testing = int(input('Please enter a number: '))
start_time = time.time()
collatz(testing)
print('runtime: %s sec' % (time.time() - start_time))
print()
plt.show()
