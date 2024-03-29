from collections import *
from itertools import *
import sys

#def __init__():
#open wordlist as directed from sys.in and unpickle it
#initialize set
source = open("wordlist.txt")
word_list = {}

#count = 0
#add words to sets
for word in source:
#	count += 1
	#strip \n from word
	word = word.rstrip()	
	
	# perform letter count of word
	letter_counts = Counter(word)
	
	#put in set based off of number of times that letter occurs
	for letter in letter_counts:
		# if letter not already in dictionary, initialize it with an {}
		if letter not in word_list:
			word_list[letter] = {}
		# if this number of occurences not already in letter of dict, initialize it as a set
		if letter_counts[letter] not in word_list[letter]:
			word_list[letter][letter_counts[letter]] = set()
		#add word to set
		word_list[letter][letter_counts[letter]].add(word)

#combine smaller counts into the larger ones for quicker processing
#iterate through letters in word_list
for letter in word_list:
	#iterate through counts in word_list
	for count1 in word_list[letter]:
		#iterate through again
		for count2 in word_list[letter]:
			if count2 < count1:
				word_list[letter][count1] = word_list[letter][count1].union(word_list[letter][count2])

#declare worth of letters
points = {"a":1 , "b":3 , "c":3, "d":2 , "e":1 , "f":4 , "g":2 , "h":4 , "i":1 , "j":8 , "k":5 , "l":1 , "m":3 , "n":1 , "o":1 , "p":3 , "q":10 , "r":1 , "s":1 , "t":1 , "u":1 , "v":4, "w":4 , "x":8 , "y":4 , "z":10}

# function to calculate worth of word
def score(word):
	return sum(points[letter] for letter in word)

#start main loop and ask for first hand
def find_words(letters):
	#fold case
	letters = letters.lower()

	#remove non A-Z
	letters = [letter for letter in letters if letter in "abcdefghijklmnopqrstuvwxyz"]
	
	#create a counter from the letters
	letter_count = Counter(letters)
	results = {"only":[], "extra":[]}

	for x in range(2, len(letters) + 1, 1):
		words_from_letters = set()
		words = set()
		for combo in combinations(letters, x):
			combo_count = Counter(combo)
			choices = [word_list[letter][letter_count[letter]] for letter in combo if letter_count[letter] in word_list[letter]]
			if choices:
				poss = set.intersection(*choices)
			else:
				poss = set()
			for word in poss:
				if len(word) == x:
					word_letter_count = Counter(word)
					if word_letter_count == combo_count:
						words_from_letters.add((word, score(word), x))
				if len(word) == x+1:
					word_letter_count = Counter(word)
					if len(word_letter_count) == len(combo_count) + 1:
						extras = 0
						for letter in word_letter_count:
							if word_letter_count[letter] > combo_count[letter]:
								if word_letter_count[letter] != combo_count[letter] + 1:
									extras += 2
									break
								else:
									extras += 1
							if extras > 1:
								break
						if extras == 1:
							words.add((word, score(word), x))

		if words_from_letters:
			words_from_letters = list(words_from_letters)
#			words_from_letters.sort(key=lambda x:x[1], reverse=True)
			results["only"] += words_from_letters
		if words:
			words = list(words)
#			words.sort(key=lambda x:x[1], reverse=True)
			results["extra"] += words
	return results
