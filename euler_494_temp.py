import time, math

# ------------------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------------------

def powers_of_two(n):
	""" Creates and returns a list of powers of two from
		which we will build our Collatz prefix sequences.
	"""
	powers = []
	for i in range(3,n+1):
		powers.append(2**i)

	return powers


def print_sequences(parent_tree_position, parent_value, parent_path_list):
	""" Generates Collatz prefix sequences that take m steps
		to get to a given power of two.
	"""
	next_even_number = parent_value * 2
	even_child_tree_position = parent_tree_position * 2
	even_path_list = parent_path_list + [next_even_number]

	if(even_child_tree_position >= 2 ** (sequence_length - 1)):
		print(list(reversed(even_path_list)))
	else:
		print_sequences(even_child_tree_position, next_even_number, even_path_list)


	next_odd_number = (parent_value - 1) / 3
	# If the next odd number is going to be a fraction, stop going down that path.
	if(next_odd_number % 1 != 0 or next_odd_number % 2 == 0):
		return

	odd_child_tree_position = (parent_tree_position * 2) + 1
	odd_path_list = parent_path_list + [int(next_odd_number)]

	if(odd_child_tree_position >= 2 ** (sequence_length - 1)):
		print(list(reversed(odd_path_list)))
		return
	else:
		print_sequences(odd_child_tree_position, int(next_odd_number), odd_path_list)
		return

# ------------------------------------------------------------------------------------------
# USER INPUT
# ------------------------------------------------------------------------------------------

print("")
user_starting_power = input("Enter a starting power of two: ")

if(not user_starting_power.isdigit()):
	print("The starting power must be a positive integer. \n")
	quit()
elif(float(user_starting_power) == 0):
	print("The starting power must be a positive integer. \n")
	quit()
elif(((2 ** int(user_starting_power)) - 1) % 3 != 0):
	print("There are no sequences of any length that reach %i. \n" % (2 ** int(user_starting_power)))
	quit()

starting_power = 2 ** int(user_starting_power)

print("We are now looking for sequences that reach %i. \n" % (starting_power))

user_sequence_length = input("Enter a sequence length: ")

if(not user_starting_power.isdigit()):
	print("The starting power must be a positive integer. \n")
	quit()
elif(float(user_sequence_length) == 0):
	print("The sequence length must be a positive integer. \n")
	quit()

sequence_length = int(user_sequence_length)

# ------------------------------------------------------------------------------------------
# CORE LOGIC
# ------------------------------------------------------------------------------------------

start_time = time.time()

starting_number = int((starting_power - 1) / 3)

print("")
print_sequences(1, starting_number, [starting_number])
print("")
print("runtime: %s" % (time.time() - start_time))
print("")

