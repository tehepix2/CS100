'''
Carlos Landaverde
12/10/2024
CS100 Section 001
Homework 12
'''

def safeOpen(filename): # initialize the safeOpen function
    try:
        return open(filename) # try returning an open file
    except:
        return None # return None if error occurs

inputFile = safeOpen('ghost.txt') # testing the function
print(inputFile)

def safeFloat(x): # initialize the safeFloat function
    try:
        return float(x) # try casting x to a float
    except:
        return 0.0 # return 0.0 if casting fails
    
f = safeFloat('abc') # testing the function
print(f)

def averageSpeed(): # initializing the averageSpeed function

    file = input("Enter file name: ") # prompt for a file name
    if safeOpen(file) != None: # execute if file successfully opens
        sum = 0
        total = 0
        lines = open(file).readlines() # get a list of every line in the file
        for line in lines: # loop through every line
            for number in line.strip().split(): # loop through every number of line after stripping the \n
                if (safeFloat(number) != 0.0) and (safeFloat(number) > 2): # execute if the number is a proper float and greater than 2
                    sum += float(number) # add number to sum
                    total += 1 # add one to total
        if total != 0: # make sure to not break if no numbers work
            print("Average speed is " + str(sum / total) + " miles per hour.") # print the average
            
    else: # execute if the above fails
        print("File not found. Please try again.")
        file = input("Enter file name: ")
        if safeOpen(file) != None: # execute if file successfully opens
            sum = 0 
            total = 0
            lines = open(file).readlines() # get a list of every line in the file
            for line in lines: # loop through every line
                for number in line.strip().split(): # loop through every number of line after stripping the \n at the end of each line
                    if (safeFloat(number) != 0.0) and (safeFloat(number) > 2): # execute if the number is a proper float and greater than 2
                        sum += float(number) # add number to sum
                        total += 1 # add one to total
            if total != 0: # make sure to not break if no numbers work
                print("Average speed is " + str(sum / total) + " miles per hour.") # print the average 

        else: # execute if the above fails
            print('File not found. Yet another human error. Goodbye.') # say bye bye to the user


averageSpeed() # call the averageSpeed function

