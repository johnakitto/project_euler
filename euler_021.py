import time, math, matplotlib.pyplot as plt

# THIS THROWS AN INDEX ERROR OCCASIONALLY
print()
x = int(input('enter a number: '))
start_time = time.time()

D = [0] * x
D[2] = 1
D[3] = 1
D[4] = 3

for n in range(5, x):
	count = 1
	if n**0.5 % 1 == 0:
		count += int(n**0.5)
		for d in range(2, math.floor(n**0.5)):
			if n % d == 0:
				count += int(d) + int(n/d)
	else:
		for d in range(2, math.floor(n**0.5)+1):
			if n % d == 0:
				count += int(d) + int(n/d)

	D[n] = count

X, Y = [], []
s = 0
for n in range(2, x):
	if D[n] < x+1 and D[n] != n and D[n] != 0:
		if n == D[D[n]]:
			# print(str(n) +' '+ str(D[n]))
			s += n + D[n]
			D[D[n]] = 0
			X.append(n); X.append(D[n])
			Y.append(D[n]); Y.append(n)

plt.scatter(X, Y, color='k', s=1)
plt.xlabel('n')
plt.ylabel('Sum of divisors < n (if amicable)')
plt.title('Amicable Numbers: An Investigation\n')

print('sum of amicable numbers < '+ str(x) +': '+ str(s))
print('runtime: %s sec' % (time.time() - start_time))
print()
plt.show()
