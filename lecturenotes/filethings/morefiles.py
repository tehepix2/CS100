'''
Define a function func3(name1, name2) that takes 2 parameters:
1. name1, the name of an input file containing student names and exam scores
2. name2, the name of an output file
The function writes to the output file, the name of the students in the input file who got an A. An A is a score >= 90.
'''

def func3(name1, name2):
    read_file = open(name1)
    write_file = open(name2, 'w')

    line_list = read_file.readlines()
    for line in line_list:
        if int(line.split()[1]) >= 90:
            write_file.write(str(line.split()[0]) + '\n')
    read_file.close()
    write_file.close()

func3('data.txt', 'output.txt')

'''
Write a function vowelWords() that finds and returns the total number of words in a text file that start in a vowel. 
The function takes one parameter: filename, the name of a file containing words and whitespaces.
For example, if file contains:
'An apple a day keeps the doctor away'
print(vowelWords('input.txt')) 
4
'''

def vowelWords(filename):
    vowels = 'aeiouAEIOU'
    count = 0

    word_file = open(filename)

    text = word_file.read().split()
    
    word_file.close()
    for word in text:
        if word[0] in vowels:
            count += 1
    
    return count

print(vowelWords('wordfile.txt'))

def vowelWords2(filename, outputfile):
    vowels = 'aeiouAEIOU'

    word_file = open(filename)
    output_file = open(outputfile, 'w')

    text = word_file.readlines()

    for line in text:
        for word in line.split():
            if word[-1] in vowels:
                output_file.write(str(word) + " ")
        output_file.write('\n')
  
    word_file.close()
    output_file.close()

vowelWords2('wordfile.txt', 'vowelfile.txt')

    
あ = 50

