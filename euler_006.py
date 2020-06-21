import time

print()
n = int(input('enter a number: '))
start_time = time.time()

sum_of_squares = sum([i**2 for i in range(1,n+1)])
square_of_sum = int((0.5*n*(n+1))**2)

print('solution: '+ str(square_of_sum - sum_of_squares))
print('runtime '+str(time.time() - start_time)+' sec')
print()
