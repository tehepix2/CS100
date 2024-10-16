#1 
grades = [] # initialize the grades list
grades.append('A') 
grades.append('B')
grades.append('C')
grades.append('D')
grades.append('F') # adding the grades to the list
grades.append('D')
grades.append('A')
grades.append('C')
grades.append('F')
grades.append('A') 
print(grades) # show the completed list

frequency = [] # initialize frequency list
frequency.append(grades.count('A')) # appends the number of A grades to frequency
frequency.append(grades.count('B')) # appends the number of B grades to frequency
frequency.append(grades.count('C')) # appends the number of C grades to frequency
frequency.append(grades.count('D')) # appends the number of D grades to frequency
frequency.append(grades.count('F')) # appends the number of F grades to frequency
print(frequency)

#2 
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua'] # initialize the dog breed list
print(dog_breeds)
herding_dogs = dog_breeds[0:2] # slice the first two elements of the dog breeds list an assign it to herding dogs (this works since the slice automatically creates a list)
print(herding_dogs)
tiny_dogs = [] # initialize the tiny_dogs list
tiny_dogs.append(dog_breeds[3]) # appends the index 3 of dog_breeds, the last item, to tiny_dogs.
print(tiny_dogs)
print('Persian' in dog_breeds) # checks if Persian is present in dog_breeds, and returns false, in this case

#3
first_name = input("Enter your name: ") # prompts the user for their first name
last_name = input("Enter your last name: ") # prompts the user for their last name
name_list = [] # initializes the list for the names
name_list.append(first_name) # appends the first name to name_list
name_list.append(last_name) # appends the last name to name_list
print("List: " + str(name_list)) # displays the list
print("Initials: " + name_list[0][0] + name_list[1][0]) # prints the initials; first the index of the name, and then the first index of the letter for both first and last name
print("Average length: " + str((len(name_list[0]) + len(name_list[1])) / 2)) # takes the length of both names, adds then, divides by 2, converts to string, and then prints
