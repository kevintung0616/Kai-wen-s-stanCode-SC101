"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
python_list = []              # Create Python_list to store e every name in the dictionary.txt


def main():

    while True:
        s = input("find anagrams for: ")  # Input a string to find its anagrams from a dictionary
        start = time.time()
        read_dictionary()  # Read the dictionary

        if s == EXIT:  # Terminate the program if an user inputs a string matches the EXIT constant
            break

        else:
            find_anagrams(s)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    global python_list # Define a list "python_list" as a global variable
    print("Reading....")
    with open(FILE, 'r') as d:
        for name in d:  # Loop over every name in the dictionary
            name = name.strip()  # Tokenize each name into a string
            python_list.append(name)  # Add each name into the python_list



def find_anagrams(s):
    """
    :param s:
    :return:
    """
    print("Searching")

    anagram_list = []  # Create a list 'anagram_list' to store all anagrams, and its default status is empty
    find_anagrams_helper(s, '', anagram_list, [])  # Create a helper to find anagrams
    print(str(len(anagram_list)) + ' anagrams: ' + str(anagram_list))  # After the helper finds every anagram, print all the anagrams


def find_anagrams_helper(s, word, anagram_list, index):
    # s is the input string
    # word is all possible combination of alphabets in 's'
    # anagram_list is a list storing all anagrams of 's'
    # index is a list storing the index of each alphabet in 'word'

    if len(word) == len(s):  # Base Case
        # If a word exists in the python_list but hasn't been in anagram_list, it would be an anagram
        if word in python_list and word not in anagram_list:
            print("Found:  ", word)
            print("Searching ...")
            anagram_list.append(word) # Add the anagram in anagram_list

    else:
        for i in range(len(s)):  # Loop over each character in the input string 's'

            # If the index of a alphabet 'i' first appears, this alphabet will be chosen
            # Should Use index 'i' rather than an alphabet s[i], because an alphabet may appear more than once,
            # such as 'n' in 'contains'

            if i not in index:
                word = word + s[i]  # choose the character and add it into the string 'word'
                index.append(i)  # Store the index 'i' in the list 'index'

                if has_prefix(word):

                    # Explore, do recursion to find all possible anagrams
                    find_anagrams_helper(s, word, anagram_list, index)

                word = word[:-1]  # Backtracking unchoose the string 'word'
                index.pop()  # Backtracking unchoose the list 'index'



def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for name in python_list:

        if name.startswith(sub_s):
            return True

    return False



if __name__ == '__main__':
    main()
