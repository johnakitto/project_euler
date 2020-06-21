import time
start_time = time.time()

word_sum = lambda word: sum([ord(letter.lower())-96 for letter in word])
triangle_word = lambda s: (0.5*((8*s + 1)**0.5 - 1)) % 1 == 0
words = [word.strip('\n').strip('"') for word in [line.split(',') for line in open('euler_042.txt')][0]]

print()
print(str(sum([triangle_word(word_sum(word)) for word in words])) +' triangle words')
print('runtime: %s sec' % (time.time() - start_time))
print()
