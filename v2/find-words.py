from collections import *
from itertools import *
import sys, pickle

#open wordlist as directed from sys.in and unpickle it
pkl_file = open(sys.argv[1], "rb")
word_list = pickle.load(pkl_file)
pkl_file.close()

#declare worth of letters
points = {"a":1 , "b":3 , "c":3, "d":2 , "e":1 , "f":4 , "g":2 , "h":4 , "i":1 , "j":8 , "k":5 , "l":1 , "m":3 , "n":1 , "o":1 , "p":3 , "q":10 , "r":1 , "s":1 , "t":1 , "u":1 , "v":4, "w":4 , "x":8 , "y":4 , "z":10}

# function to calculate worth of word
def score(word):
	return sum(points[letter] for letter in word)

#start main loop and ask for first hand
loop = True
letters = input("Enter letters in your hand: ")
while loop == True:
	#strip letters of any misc. characters at the end of input
	letters = letters.rstrip()
	#create a counter from the letters
	letter_count = Counter(letters)
	
	for x in range(2, len(letters) + 1, 1):
		print("\nUsing %d letters from your hand:" % x)
		words_from_letters = set()
		words = set()
		for combo in combinations(letters, x):
			combo_count = Counter(combo)
			choices = [word_list[letter][letter_count[letter]] for letter in combo]
			poss = set.intersection(*choices)
			for word in poss:
				if len(word) == x:
					word_letter_count = Counter(word)
					if word_letter_count == combo_count:
						words_from_letters.add((word, score(word)))
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
							words.add((word, score(word)))
		
		if len(words_from_letters) != 0:
			print("With only letters given: ")
			words_from_letters = list(words_from_letters)
			words_from_letters.sort(key=lambda x:x[1], reverse=True)
			print(words_from_letters)
		if len(words) != 0:
			print("Words with 1 additional letter: ")
			words = list(words)
			words.sort(key=lambda x:x[1], reverse=True)
			print(words)
	
	letters = input("Type n to close, or type next hand to continue: ")
	if letters == "n":
		loop = False
			
