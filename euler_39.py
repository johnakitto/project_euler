import time, matplotlib.pyplot as plt
from math import sqrt

thresholds, runtimes = [], []
for threshold in range(2001):
	print(threshold, end='\r')
	start_time = time.time()
	max_perimeter, max_solutions = 0, 0
	for perimeter in range(threshold+1):
		solutions = 0
		for x in range(int(perimeter // (2+sqrt(2)))):
			y = (perimeter * (perimeter - 2*x)) / (2 * (perimeter - x))
			if y % 1 == 0 and 2*x*y - 2*perimeter*(x+y) + perimeter**2 == 0:
				solutions += 1
		if solutions > max_solutions:
			max_solutions = solutions
			max_perimeter = perimeter

	thresholds.append(threshold)
	runtimes.append(time.time() - start_time)

plt.scatter(
	thresholds,
	runtimes,
	color='k',
	s=1)
plt.xlabel('Perimeter Threshold')
plt.ylabel('Runtime (sec)')
plt.title('Max Pythagorean Triples for Perimeter < Threshold\n')

print()
print('perimeter value: '+ str(max_perimeter))
print('total solutions: '+ str(max_solutions))
print('runtime: %s sec' % (time.time() - start_time))
print()

plt.show()
