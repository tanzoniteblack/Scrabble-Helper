import pickle, sys
from itertools import *

def findwords(letters, word_list)
	letters = [letter for letter in letters]
	choices = [word_list[letter] for letter in letters]
	poss_all = list(set.intersection(*choices))

	subsets = [letters]
	for x in range(2, len(letters), 1):
		print("\nUsing %d letters:" % x)
		words = []
		for combo in combinations(letters, x):
			choices = [word_list[letter] for letter in combo]
			poss = set.intersection(*choices)
			for word in poss:
				if len(word) <= x + 1:
					words.append(word)
		words.sort()
		print(words)

	print("\nUsing all letters:")
	poss_all.sort()
	print(poss_all)
