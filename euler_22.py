import time
start_time = time.time()

sorted_names = sorted(open('euler_22.txt','r').read().replace('"','').split(','))

total_score = 0
for i in range(len(sorted_names)):
	letter_score = 0
	for letter in sorted_names[i]:
		letter_score += ord(letter) - 64
	total_score += (i+1) * letter_score

print()
print('solution: '+ str(total_score))
print('runtime: %s sec' % (time.time() - start_time))
print()
