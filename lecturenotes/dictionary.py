#P1
'''Write a function lengthStats() that takes one parameter:
1. text, a string containing words and white spaces
The function returns a dictionary of key:value pairs.The key represents
the length of a word in text and the value associated with that key is
the number of words in that length.
For example:
print(lengthStats('it is what it is python is a lot of fun'))
{2: 6, 4: 1, 6: 1, 1:1, 3:2}
'''

def lengthStats(text):
    dictionary = {}
    for word in text.split():
        if len(word) in dictionary.keys():
            dictionary[len(word)] += 1
        else:
            dictionary[len(word)] = 1
    return dictionary

print(lengthStats('it is what it is python is a lot of fun'))


    
#P2         
'''Write a function lengthStats2() that takes one parameter:
1. text, a string containing words and white spaces
The function returns a dictionary of key:value pairs.The key represents
the length a word in text and the value associated with that key is the
list of all the words in that length.
For example:
print(lengthStats('it is what it is python is a lot of fun'))
{2:['it', 'is','it','is','is','of'], 4:['what'], 6: ['python'], 1: ['a'],
3:['lot','fun']}
'''

def lengthStats2(text):
    dictionary = {}
    for word in text.split():
        if len(word) in dictionary.keys():
            dictionary[len(word)].append(word)
        else:
            dictionary[len(word)] = [word]
    return dictionary    

print(lengthStats2('it is what it is python is a lot of fun'))

#P3
'''Write a function lengthStats3() that takes one parameter:
1. text, a string containing words and white spaces
The function returns a dictionary of key:value pairs.The key represents
the length a word in text and the value associated with that key is the
list of all the distinct words in that length.
For example:
print(lengthStats('It is what it is python is a lot of fun'))
{2:['it', 'is','of'], 4:['what'], 6: ['python'], 1: ['a'], 3:['lot','fun']}
'''
def lengthStats3(text):
    dictionary = {}
    for word in text.split():
        if len(word) in dictionary.keys():
            if word.lower() not in dictionary[len(word)]:
                dictionary[len(word)].append(word.lower())
        else:
            dictionary[len(word)] = [word.lower()]
    return dictionary    

print(lengthStats3('It is what it is python is a lot of fun'))


#P4
'''Let scheduleDict be a dictionary of key: value pairs, where the key is a student name and value
is the list of classes the student is taking this semester. For example
{"john":['cs100','cs113','math101'], 'jill':['cs100','math101']}
Write a function reverseDict that takes a schedule dictionary parameter. The function returns a dictionary of
key value pairs, where the key is a course from schedule dictionary and the value is the list of students
taking that course. For example, if scheduleDict is the one above, the function will return
{'cs100':['john','jill'], 'cs113':['john'],'math101':['john','jill']}

'''
def reverseDict(schedule):
    dictionary = {}
    for student in schedule.keys():
        for course in schedule[student]:
            if course in dictionary.keys():
                dictionary[student].append(course)
            else:
                dictionary[student] = [course]
    return dictionary

print(reverseDict({"john":['cs100','cs113','math101'], 'jill':['cs100','math101']}))
    
#P5
'''Write a function wordStatsFromFile() that takes two filename parameters:
1, name1, input file containing words and white spaces
2. name2, output file.
The function reads the input files and writes to the output file the words
statistics in the format word: count.
For example, if the input file contains:
it is what it is
python is fun fun fun
the outputfile will contain:
it: 2
is: 3
what: 1
python: 1
fun: 3
'''
#P6
'''Write a function wordStatsFromFile2() that takes two filename parameters:
1, name1, input file containing words and white spaces
2. name2, output file.
The function reads the input files and writes to the output file the words
statistics in each line, in the format word: count.
For example, if the input file contains:
it is what it is
python is fun fun fun
the outputfile will contain:
it: 2 is: 2 what: 1
python: 1 is: 1 fun: 3'''
#P7
'''Write a function wordStatsFromFile3() that takes two parameters:
1, name1, input file containing words and white spaces
2. word, a string
The function reads the input files and returns the line with the highest
frequency of word. If more than such lines exist, return the last one. 
For example, if the input file input.txt contains:
it is what it is
python is fun fun fun
print(wordStatsFromFile3('input.txt','is')) will display -> it is what it is
Solve with and without use of dictionaries'''
#P8
'''Write a function wordStatsFromFile4() that two filename parameters:
1, name1, input file containing words and white spaces
2. name2, output file.
The function reads the input files and writes to the output file the unique
words in each line, regardless of letter case.
For example, if the input file contains:
It is what it is
python is fun fun fun
the outputfile will contain:
it is what
python is fun'''

#P9
'''Write a function mergeStatsFromFiles() that takes
three filename parameters:
1. file1, an input file name containng line in the format word: count
2. file2, an input file name containng line in the format word: count
3. file3, an output file name
The function writes to the output file the words statistics that combine
the counts from both input files. For example, if file1 contains:
it: 2
is: 3
what: 1
and file2 contains:
python: 1
is: 1
fun: 3
The output file should contains:
it: 2
is: 4
what: 1
python: 1
fun:3'''
#P10
'''The file inventory.txt contains the current inventory of items in stock.
It may contain duplicates of item: count, in error. Write a function
toReplenish() that takes 3 parameters:
1. file1, an input file containing item: count lines, including duplicates
2. target, an integer below which the item must be replenished
3. file2, an output file
The function writes to the file the items that must be replenished and the
corresponding number to order.
For example, if file1 contains:
bread: 120
eggs: 20
peanut butter: 43
milk: 51
eggs: 15
bread: 30

and the target is 90, the output file should contain:
eggs: 55
peanut butter: 47
milk: 39
'''


