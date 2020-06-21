import time, math

# ------------------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------------------

def create_sequences(parent_tree_position, parent_value, parent_bit_list):
	''' Generates Collatz prefix sequences that take m steps
		to get to a given power of two. '''

	global global_bit_list
	next_even_number = parent_value * 2
	even_child_tree_position = parent_tree_position * 2
	even_bit_list = parent_bit_list + [0]

	if even_child_tree_position >= 2 ** (sequence_length - 1):
		print(list(reversed(even_bit_list)))
		global_bit_list.append(list(reversed(even_bit_list)))
	else:
		create_sequences(even_child_tree_position, next_even_number, even_bit_list)


	next_odd_number = (parent_value - 1) / 3
	# If the next odd number is going to be a fraction or even, stop going down that path.
	if next_odd_number % 1 != 0 or next_odd_number % 2 == 0:
		return

	odd_child_tree_position = (parent_tree_position * 2) + 1
	odd_bit_list = parent_bit_list + [1]

	if odd_child_tree_position >= 2 ** (sequence_length - 1):
		print(list(reversed(odd_bit_list)))
		global_bit_list.append(list(reversed(odd_bit_list)))
		return
	else:
		create_sequences(odd_child_tree_position, int(next_odd_number), odd_bit_list)
		return


# ------------------------------------------------------------------------------------------
# USER INPUT
# ------------------------------------------------------------------------------------------

print()
user_powers_checked = input('How many powers of two do you want to check? ')

if not user_powers_checked.isdigit():
	print('The powers checked must be a positive integer.\n')
	quit()
elif float(user_powers_checked) == 0:
	print('The powers checked must be a positive integer.\n')
	quit()

powers_list = [2**i for i in range(4,4+(2*int(user_powers_checked)),2)]

user_sequence_length = input('Enter a sequence length: ')

if not user_sequence_length.isdigit():
	print('The sequence length must be a positive integer.\n')
	quit()
elif float(user_sequence_length) == 0:
	print('The sequence length must be a positive integer.\n')
	quit()

sequence_length = int(user_sequence_length)
print()


# ------------------------------------------------------------------------------------------
# CORE LOGIC
# ------------------------------------------------------------------------------------------

start_time = time.time()

global_bit_list = []
for starting_power in powers_list:

	starting_number = (starting_power - 1) // 3

	print(starting_power)
	print('------------------------')
	create_sequences(1, starting_number, [])
	global_bit_list = list(set(tuple(sequence) for sequence in global_bit_list))
	print()

print('unique permutations:')
print('------------------------')
for sequence in sorted(global_bit_list):
	print(list(sequence))
print()

up_down_permutations = len(global_bit_list)
print('%i unique up-down permutations of length %i.' % (up_down_permutations, sequence_length))

print()
print('runtime: %s' % (time.time() - start_time))
print()

