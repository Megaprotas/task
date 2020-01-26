import os
import sys

# import collections
# import string

dictionary = []

print(sys.argv)


def read_dictionary():
    with open('word.txt', 'r') as file:
        for i in file:
            lowercase_let = i.lower()
            print(lowercase_let)
            dictionary.append(lowercase_let)


#check if word is in dictionary
def does_word_exsist(word):
    # dictionary.lowercase - every string
    if word in dictionary:
        print ('word is in dictionary')
        return True
    else:
        print ('word is not in dict')
        return False


def chain_maker(first_word, last_word):
    #check lenght of words and presence in dic)t , so only same length words are being used
    print(first_word)
    print(last_word)
    if not len(first_word) != len(last_word) and does_word_exsist(first_word) and does_word_exsist(last_word):
        # iteration of first word
        iter = [i for i in first_word]
        # variable to store difference
        number = 0
        for j in last_word:
            if j in iter:
                iter += 1
        print(sys.argv)
        return 1+len(first_word) - number
    else:
        return ('')

first_word = sys.argv[1]
last_word = sys.argv[2]
read_dictionary()

print(chain_maker(first_word, last_word))
