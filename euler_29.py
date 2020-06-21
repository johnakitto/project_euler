import time
start_time = time.time()

sequence = [a**b for a in range(2,101) for b in range(2,101)]

print()
print(str(len(set(sequence))) +' distinct terms')
print(str(len(sequence) - len(set(sequence))) +' duplicates')
print('runtime: %s sec' % (time.time() - start_time))
print()
