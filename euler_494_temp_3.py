import math
import time

# ------------------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------------------

global_bit_list = []

def powers_of_two(n):
	""" Creates and returns a list of powers of two from 
		which we will build our Collatz prefix sequences.
	"""
	powers = []
	for i in range(4,n+8,2):
		powers.append(2**i)

	return(powers)


def create_sequences(parent_tree_position, parent_value, parent_bit_list):
	""" Generates Collatz prefix sequences that take m steps 
		to get to a given power of two. 
	"""
	next_even_number = parent_value * 2
	even_child_tree_position = parent_tree_position * 2	
	even_bit_list = parent_bit_list + [0]

	if(even_child_tree_position >= 2 ** (sequence_length - 1)):
		# print(list(reversed(even_bit_list)))
		global_bit_list.append(even_bit_list)
	else:
		create_sequences(even_child_tree_position, next_even_number, even_bit_list)


	next_odd_number = (parent_value - 1) / 3
	# If the next odd number is going to be a fraction, stop going down that path.
	if(next_odd_number % 1 != 0 or next_odd_number % 2 == 0):
		return

	odd_child_tree_position = (parent_tree_position * 2) + 1
	odd_bit_list = parent_bit_list + [1]

	if(odd_child_tree_position >= 2 ** (sequence_length - 1)):
		# print(list(reversed(odd_bit_list)))
		global_bit_list.append(odd_bit_list)
		return
	else:
		create_sequences(odd_child_tree_position, int(next_odd_number), odd_bit_list)
		return

# ------------------------------------------------------------------------------------------
# USER INPUT
# ------------------------------------------------------------------------------------------

# print("")
# user_starting_power = input("Enter a starting power of two: ")

# if(not user_starting_power.isdigit()):
# 	print("The starting power must be a positive integer. \n")
# 	quit()
# elif(float(user_starting_power) == 0):
# 	print("The starting power must be a positive integer. \n")
# 	quit()
# elif(((2 ** int(user_starting_power)) - 1) % 3 != 0):
# 	print("There are no sequences of any length that reach %i. \n" % (2 ** int(user_starting_power)))
# 	quit()

# starting_power = 2 ** int(user_starting_power)
# print("We are now looking for sequences that reach %i. \n" % (starting_power))


print("")
user_powers_checked = input("How many powers of two do you want to check? ")

if(not user_powers_checked.isdigit()):
	print("The powers checked must be a positive integer. \n")
	quit()
elif(float(user_powers_checked) == 0):
	print("The starting power must be a positive integer. \n")
	quit()

powers_checked = int(user_powers_checked)
powers_list = powers_of_two(powers_checked)


user_sequence_length = input("Enter a sequence length: ")

if(not user_sequence_length.isdigit()):
	print("The sequence length must be a positive integer. \n")
	quit()
elif(float(user_sequence_length) == 0):
	print("The sequence length must be a positive integer. \n")
	quit()

sequence_length = int(user_sequence_length)

# ------------------------------------------------------------------------------------------
# CORE LOGIC
# ------------------------------------------------------------------------------------------

start_time = time.time()

print("")
for starting_power in powers_list:
	starting_number = int((starting_power - 1) / 3)
	create_sequences(1, starting_number, [])

up_down_permutations = len(set(tuple(sequence) for sequence in global_bit_list))
print("%i unique up-down permutations of length %i." % (up_down_permutations, sequence_length))

print("")
print("runtime: %s" % (time.time() - start_time))
print("")

