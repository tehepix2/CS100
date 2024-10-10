days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')

for day in days:
    print("Hello") # prints hello 5 times, as there are 5 elements in the array

print("\n")

scores = [92, 45, 65, 87, 100]

# no matter what temp variable is used, like el in the example below, 
# it will behave the same. if it was i, or number, or score, it will go through ever element of scores.
for el in scores: # this will output every element in scores.
    print(el)

print("\n")

for score in scores: # outputs hello for every element in scores.
    print("Hello")

print("\n")

oneTwoThree = [1, 2, 3]

# for i in oneTwoThree:   # this is as infinite loop as the list keeps growing 
#     oneTwoThree.append(i + 3)
#     print("i =", i)
#     print('oneTwoThree =', oneTwoThree) # DO NOT UNCOMMENT THIS UNLESS YOU WANT TO BE STUCK IN AN INFINITE LOOP

'''
Given the list of exam scores, scores = [99, 76, 89, 92, 56], Write a program that creates and prints to the screen a list containing all A scores. 
In this example, the program should print [99, 92]. An A is a score of 90 and above.
'''

scores = [99, 76, 89, 92, 56]
aScore = []

for score in scores:
    if score >= 90:
        aScore.append(score)

#Redo the problem below 
for i in range (0, scores.len()):
    if scores[i] >= 90:
        aScore.append(scores[i])



