'''
Carlos Landaverde
CS100 Section 001
11/13/2024
Homework 8
'''
import random

def twoWords(length, firstletter): # initialize the function
    word_list = [] # initialize the list that will be returned
    
    while True: # begin the while loop
        word = input("Enter a " + str(length) + "-letter word please: ") # prompt for a word
        if len(word) == length: # check if the word is the same length as the specified length
            word_list.append(word) # append to the list if it is true
            break # break the while loop
    
    while True: # begin the while loop
        word2 = input("Enter a word beginning with " + firstletter + " please: ") # prompt for a word
        if word2[0].lower() == firstletter.lower(): # check if the word's first letter is the same as the specified first letter (regardless of capitalization)
            word_list.append(word2) # append to the list if the above condition is true
            break # break the while loop
    
    return word_list # return the list



def twoWordsV2(length, firstletter): # initialize the function
    word_list = [] # initialize the list

    word = input("Enter a " + str(length) + "-letter word please: ") # ask for a word of specified length
    while len(word) != length: # begin the while loop and loop if the word is not at the specified length
        word = input("Enter a " + str(length) + "-letter word please: ") # prompt for a word should the condition be true
    word_list.append(word) # append the word after the while loop ends
    
    word2 = input("Enter a word beginning with " + firstletter + " please: ") # ask for a word of specified first letter
    while word2[0].lower() != firstletter.lower(): # begin the while loop and loop if the word does not start with the specified letter (regardless of capitalization)
        word2 = input("Enter a word beginning with " + firstletter + " please: ") # ask for a word of specified first letter
    word_list.append(word2) # append the word after the while loop ends

    return word_list # return the list 

def enterNewPassword():
    password = '' # initialize an empty password
    password_is_valid = False # default false
    digits = '0123456789' # digits 0 - 9

    while not password_is_valid: # loop while password_is_valid is False
        password_is_length = False # default false
        password_has_digit = False # default false
        
        password = input("Enter a password (8-15 characters, at least one digit): ") # prompt for a password

        if len(password) >= 8 and len(password) <= 15: # check if the password's length is between 8 and 15 (inclusive)
            password_is_length = True # password length is True if the above condition is satisfied
        else: # otherwise, specify if the password is too short or too long
            if len(password) > 15:
                print("Password is too long!")
            elif len(password) < 8:
                print("Password is too short!")

        for char in password: # check every character in password
            if char in digits: # check if the character appears in digits
                password_has_digit = True # if it does appear, digit in password is True
        if not password_has_digit: # if the password has no digits, say that it contains to digits
            print("Password contains no digits!")
        
        if password_is_length and password_has_digit: # if the password is a valid length and contains a digit, set valid password to True
            password_is_valid = True # end the loop by changing the validity to True

    return password # return the password
   
def GuessNumber():
    random_number = random.randint(0, 50)
    guessed = False
    guess_count = 1
    print("I'm thinking of a number in the range 0-50. You have five tries to guess it.")
    
    while guess_count < 6:
        
        guess = int(input("Guess " + str(guess_count) + "? "))
        
        if guess > random_number:
            print(str(guess) + " is too high.")
            guess_count += 1
        
        elif guess < random_number:
            print(str(guess) + " is too low.")
            guess_count += 1
        
        elif guess == random_number:
            guessed = True
            break

    if guessed:
        print("You are right! I was thinking of " + str(random_number) + "!")
    else:
        print("The correct answer was " + str(random_number) + ".")
    
print(twoWords(4, 'B')) # testing

print(twoWordsV2(4, 'B')) # testing

print("Password entered: " + enterNewPassword()) # testing

GuessNumber() # testing
        
