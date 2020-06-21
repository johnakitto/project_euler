import time, fractions
start_time = time.time()

curious_fractions = []
for numerator in range(10,100):
	for denominator in range(numerator+1,100):
		numerator_list = list(str(numerator))
		denominator_list = list(str(denominator))
		for i in range(2):
			for j in range(2):
				if numerator_list[i] == denominator_list[j]:
					if [numerator_list[i], denominator_list[i]] != ['0','0']:
						del numerator_list[i]
						del denominator_list[j]
						if denominator_list != ['0']:
							if int(''.join(numerator_list)) / int(''.join(denominator_list)) == numerator / denominator:
								curious_fractions.append((numerator, denominator))
								# print(str(numerator)+'/'+str(denominator))
					break

			if len(numerator_list) == 1:
				break

curious_numerator = 1
for numerator in [fraction[0] for fraction in curious_fractions]:
	curious_numerator *= numerator

curious_denominator = 1
for denominator in [fraction[1] for fraction in curious_fractions]:
	curious_denominator *= denominator

final_numerator = fractions.Fraction(curious_numerator, curious_denominator).numerator
final_denominator = fractions.Fraction(curious_numerator, curious_denominator).denominator

print()
print('solution: '+ str(final_numerator)+'/'+str(final_denominator))
print('runtime: %s sec' % (time.time() - start_time))
print()
