'''
Carlos Landaverde
11/27/2024
Homework 10
CS100 Section 001
'''

def initialLetterCount(word_list):
    letter_dict = {}

    for word in word_list:
        if len(word) > 0:
            if word[0] in letter_dict.keys():
                letter_dict[word[0]] += 1
            else:
                letter_dict[word[0]] = 1

    return letter_dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton)) # testing example 

test_2 = ['Ingenious', 'is', 'an', 'Arts'] # testing if capitalization would break it
print(initialLetterCount(test_2))

test_3 = ['', '', 'Amazing', 'ace', '', ''] # testing if empty strings would break it
print(initialLetterCount(test_3))

def initialLetters(word_list):
    letter_dict = {}

    for word in word_list:
        if len(word) > 0:
            if word[0] in letter_dict.keys():
                if word not in letter_dict[word[0]]:
                    letter_dict[word[0]].append(word)
            else:
                letter_dict[word[0]] = [word]

    return letter_dict

# this is all assuming that capitalization still matters
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton)) # testing example 

test_2 = ['Ingenious', 'is', 'an', 'Arts'] # testing if capitalization would break it
print(initialLetters(test_2))

test_3 = ['', '', 'Amazing', 'ace', '', ''] # testing if empty strings would break it
print(initialLetters(test_3))

def shareOneLetter(word_list):
    share_dict = {}

    for word in word_list:
        if len(word) > 0: # very nifty for loop, i got lost in it but it works
            if word in share_dict.keys():
                for word1 in word_list:
                    for letter in word1:
                        if letter in word:
                            if word1 not in share_dict[word]:
                                share_dict[word].append(word1)
            else:
                share_dict[word] = []
                for word1 in word_list:
                    for letter in word1:
                        if letter in word:
                            if word1 not in share_dict[word]:
                                share_dict[word].append(word1)
                

    return share_dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareOneLetter(horton)) # testing example 

test_2 = ['Ingenious', 'is', 'an', 'Arts'] # testing if capitalization would break it
print(shareOneLetter(test_2))

test_3 = ['', '', 'Amazing', 'ace', '', ''] # testing if empty strings would break it
print(shareOneLetter(test_3))
