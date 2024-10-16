"""
Carlos Landaverde
CS 100 Section 001
HW 04, October 15, 2024
"""

months = [ # creating a list with all months of the year
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December"
    ]

for month in months: # itierating through list of months
    if "J" in month[0]: # check if the first letter of the month is J
        print(month) # prints the month if the first letter is J

for number in range(0,100): # goes through numbers 0 - 99 (100 is exclusive)
    if (number % 5 == 0) and (number % 2 == 0): # checks if the number is divisible by 5 and 2 (modulus of the number needs to be 0)
        print(number) # prints the number if it is divisible by 5 and 2

horton = "A person's a person, no matter how small." # assigning the variables
vowels = "aeiouAEIOU"

for letter in horton: # goes through every letter in horton
    for vowel in vowels: # goes through every letter in vowels
        if vowel in letter: # checks if the vowel is equal to the current iteration of a letter in horton
            print(vowel) # prints the vowel if it the current iteration of the letter in hoton is a vowel
