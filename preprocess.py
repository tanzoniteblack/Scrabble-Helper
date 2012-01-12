import sys, pickle
from collections import *

list_source = open(sys.argv[1]).read().split()

output = open(sys.argv[2], "wb")
word_list = {letter:set() for letter in "abcdefghijklmnopqrstuvwxyz"}

scrabble_counts = {"a":9, "b":2, "c":2, "d":4, "e":12, "f":2, "g":3, "h":2, "i":9, "j":1, "k":1, "l":4, "m":2, "n":6, "o":8, "p":2, "q":1, "r":6, "s":4, "t":6, "u":4, "v":2, "w":2, "x":1, "y":2, "z":1}

for word in list_source:
	if len(word) < 9:
		counts = Counter(word)
		valid = True
		for letter in word:
			if counts[letter] > scrabble_counts[letter]:
				valid = False
				break
		if valid == True:
			for letter in word:
				word_list[letter].add(word)

pickle.dump(word_list, output)
