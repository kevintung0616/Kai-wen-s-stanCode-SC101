"""
File: boggle.py
Name: Kai-wen Tung

----------------------------------------
TODO: This program simulate Boggle
First an user input 4*4 alphabet. Then, the program recursively finds all words input by an user in Boggle matching
the words in the dictionary

Test:
f y c l
i o m g
o r i l
h j h u
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	row_list = []

	for i in range(4):
		s = input(str(i + 1) + ' row of letters: ')
		s = s.lower()

		if len(s) == 7:  # 確保使用者輸入4個字母+3個空格
			row = s.split()  # 去除空格與換行字元

			if len(row) == 4:  # 去除空格與換行字元後，每行長度應該為4
				row_list.append(row)

			else:
				print('Illegal input')
				break

		else:
			print('Illegal input')
			break

	start = time.time()

	python_list = read_dictionary(row_list)

	find_anagrams(row_list, python_list)

	end = time.time()

	print('----------------------------------')
	print(f'The speed of your anagram algorithm: {end - start} seconds.')


def find_anagrams(row_list, python_list):
	word_list = [] # Create a a list 'word_list' to store all words, and its default status is empty
	for i in range(4):
		for j in range(4):
			coordinate = []  # coordinate必須放在for loop裡面，使coordinate隨每次[i,j]更新，而不會累積
			first_character = row_list[i][j]  # Start a word with the first character from the (i, j) in the row_list
			coordinate.append([i, j])  # Store the coordinate (i,j) in  a list 'coordinate'
			find_anagrams_helper(row_list, first_character, word_list, i, j, coordinate, python_list)  # Create a helper to find anagrams

	print('There are ' + str(len(word_list)) + ' words in total')


def find_anagrams_helper(s, word, word_list, x, y, coordinate, python_list):
	if len(word) >= 4 and word in python_list and word not in word_list:  # Base case
		print('Found: ', word)
		word_list.append(word)  # Add the word to the word list

	# Loop over all possible neighboring coordinates [(x-1,x,x+1) (y-1,y,y+1)]
	for i in range(-1, 2):
		for j in range(-1, 2):
			if 0 <= x + i <= 3 and 0 <= y + j <= 3 and [x + i, y + j] not in coordinate:
				word = word + s[x + i][y + j]
				coordinate.append([x + i, y + j])

				if has_prefix(word, python_list):  # Explore
					# coordinate (x,y) should be updated with the latest coordinate (x + i, y + j)
					find_anagrams_helper(s, word, word_list, x + i, y + j, coordinate, python_list)

				word = word[:-1]  # Backtracking unchoose the string 'word'
				coordinate.pop()  # Backtracking unchoose the list 'index'


def read_dictionary(row_list):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	To reduce the time complexity of the algorithm, only store the words start with any alphabet input by an user in the dictionary
	"""
	s = ''
	# Loop over every character in the row_list to create a string
	for i in range(4):
		for j in range(4):
			if row_list[i][j] not in s:  # Delete the repeating letter in the string to reduce the time complexity
				s = s + row_list[i][j]

	python_list = []  # Create a list "python_list" to store every words in the dictionary
	with open(FILE, 'r') as d:
		for name in d:
			for ch in s:
				# Only store those words whose length >=4 and whose prefix is the input alphabets to reduce the time complexity
				if len(name) >= 4 and name.startswith(ch):
					python_list.append(name.strip())
	return python_list


def has_prefix(sub_s, python_list):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for name in python_list:

		if name.startswith(sub_s):
			return True

	return False


if __name__ == '__main__':
	main()
