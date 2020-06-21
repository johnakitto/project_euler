import math
import time

starting_power = 2 ** int(input("Enter a starting power of two: "))

if((starting_power - 1) % 3 != 0):
	print("There are no sequences of any length that reach %i \n" % (starting_power))
	quit()

sequence_length = int(input("Enter a sequence length: ")) - 1

start_time = time.time()

starting_number = int((starting_power - 1) / 3)
sequence_list = [0,starting_number]

steps_remaining = sequence_length
while(steps_remaining > 0):

	first_root_index = int(len(sequence_list) / 2)
	last_root_index = len(sequence_list)

	for i in range(first_root_index,last_root_index):

		next_even_number = sequence_list[i] * 2
		next_odd_number = (sequence_list[i] - 1) / 3

		sequence_list.append(int(next_even_number))

		if(next_odd_number % 1 == 0):
			sequence_list.append(int(next_odd_number))
		else:
			sequence_list.append(0)

	steps_remaining -= 1

# def print_sequences(index, path_list):

# 	path_list = path_list + [sequence_list[index]]

# 	if(index >= len(sequence_list)/2):
# 		if(sequence_list[index] != 0):
# 			print(list(reversed(path_list)))
# 		return
# 	else:
# 		print_sequences(index * 2, path_list)
# 		print_sequences((index * 2) + 1, path_list)
# 		return

print("")
print(sequence_list)
# print("")
# print_sequences(1,[])
print("")
print("runtime: %s" % (time.time() - start_time))
print("")



