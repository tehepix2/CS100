user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print(user_name + ", you are eligible to vote!")
else: 
    print(user_name + ", you are not eligible to vote!")

'''
Write a program that displays on the screen an appropriate message based on a user input temp.
The possible messages are:
>86 "It is got
    Be sure to drink liquids"
[61 - 85] "It is warm"
[52 - 60] "It is cool"
[32 - 49] "It is cold"
<32 it is freezing

Bonus: If temp is an unrealistic value, print an error message
e.g. Error: input is unrealistic
'''
    