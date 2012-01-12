import pickle, sys
from itertools import *
#from collections import *

def score(word):
	return sum(points[letter] for letter in word)

pkl_file = open(sys.argv[1], "rb")
word_list = pickle.load(pkl_file)
pkl_file.close()

points = {"a":1 , "b":3 , "c":3, "d":2 , "e":1 , "f":4 , "g":2 , "h":4 , "i":1 , "j":8 , "k":5 , "l":1 , "m":3 , "n":1 , "o":1 , "p":3 , "q":10 , "r":1 , "s":1 , "t":1 , "u":1 , "v":4, "w":4 , "x":8 , "y":4 , "z":10}

loop = True
letters = input("Enter letters in your hand: ")
while loop == True:
	letters = letters.rstrip()
	letters = [letter for letter in letters]
	choices = [word_list[letter] for letter in letters]
	poss_all = list(set.intersection(*choices))

	unique = set(letters)
#	wrd_cnt = Counter(letters)
	subsets = [letters]
	for x in range(2, len(unique) + 1, 1):
		print("\nUsing %d letters:" % x)
		words_from_letters = set()
		words = set()
		for combo in combinations(letters, x):
			choices = [word_list[letter] for letter in combo]
			poss = set.intersection(*choices)
			for word in poss:
				outofword = 0
				for letter in word:
					if letter not in letters:
						outofword += 1
						if outofword > 1:
							break
				if outofword == 1:
					words.add((word, score(word)))
				if outofword == 0:
					words_from_letters.add((word, score(word)))
		print("Words with only letters given: ")
		words_from_letters = list(words_from_letters)
		words_from_letters.sort(key=lambda x:x[1], reverse=True)
		print(words_from_letters)
		words = list(words)
		words.sort(key=lambda x:x[1], reverse=True)
		print("Words with an additional letter: ")
		print(words)


	cont = input("Type n to close, or type in next hand to continue: ")
	if cont == "n":
		loop = False
	else:
		letters = cont

