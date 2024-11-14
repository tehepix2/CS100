'''
write a program that prompts the user for the class size. The program creates a list of that many 
user-input student names (lower case). 
It then creates and prints to the screen a string containing the sudents initials. 
For example, if the class list is ['john', 'adam', 'jake', 'jill', 'eva'] the program should print:
jajje
'''

class_list = [] # empty starting list

class_size = int(input("Enter class size: ")) # prompts for the size of the class

for student in range(class_size): # loops as any times as class_size
    name = input("Enter a name (lowercase): ") # prompts for a name
    class_list.append(name) # adds the name to class_list

initials = '' # empty initial string
for student in class_list:
    initials += student[0] # concatenate the first letter of every student in class_list to initials

print("Initials: " + initials) # display initials



# print only vowel initials

vinitials = '' # empty initial string
for student in class_list: # goes through every element of class_list
    if student[0] in 'aeiou': # checks if the first letter of each element in class_list is a vowel (the spaghetti code alternative is also acceptable but looked down upon)
        vinitials += student[0] # concatonates the initial if it is a vowel

print("Vowel initials: " + vinitials) # prints all of the initials that are a vowel

