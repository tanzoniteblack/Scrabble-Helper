from collections import *
import sys, pickle

#open source and output as directed from sys.in
source = open(sys.argv[1])
output = open(sys.argv[2], "wb")

#initialize set
word_list = {}

count = 0
#add words to sets
for word in source:
	count += 1
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

pickle.dump(word_list, output)	