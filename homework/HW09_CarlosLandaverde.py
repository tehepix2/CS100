'''
Carlos Landaverde
CS100 Section 001
11/20/2024
Homework 9
'''

import string 

def file_copy(in_file, out_file):
    output_file = open(out_file, 'w')
    input_file = open(in_file, 'r')
    

    output_file.write(input_file.read())

    input_file.close()
    output_file.close()

file_copy('created_equal.txt', 'copy.txt')

copy_f = open('copy.txt')
print(copy_f.read())
copy_f.close()

def file_stats(in_file):
    input_file = open(in_file, 'r')
    text = input_file.read()
    
    lines = 0
    for line in text.split('\n'):
        if line != '':
            lines += 1
    print("Lines: " + str(lines))

    words = 0
    for line in text.split('\n'):
        if line != '':
            for word in line.split():
                words += 1
    print("Words: " + str(words))

    characters = 0
    for line in text.strip():
        characters += 1
    print("Characters: " + str(characters))
    input_file.close()

file_stats("created_equal.txt")

def repeat_words(in_file, out_file):
    input_file = open(in_file, 'r')
    output_file = open(out_file, 'w')

    text = input_file.read().lower()
    repeat_list = []
    for line in text.split('\n'):
        repeat_words = []
        for word in line.split():
            if line.count(word.strip(string.punctuation)) > 1:
                repeat_words.append(word.strip(string.punctuation))
        for word in repeat_words:
            while repeat_words.count(word) > 1:
                repeat_words.remove(word)
        repeat_list.append(repeat_words)
    for list in repeat_list:
        for word in list:
            output_file.write(word + " ")
        output_file.write('\n')

        

            

repeat_words('catInTheHat.txt', 'catRepWords.txt')