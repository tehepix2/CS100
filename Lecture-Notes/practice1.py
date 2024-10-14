classSize = int(input("Enter a class size: "))
scoresList = []

for student in range(classSize):
    score = int(input("Enter a score: "))
    scoresList.append(score)

print("Your class scores: " + str(scoresList))

aList = []
for score in scoresList:
    if score >= 90:
        aList.append(score)

print("Scores that are an A: " + str(aList))

# modify this code to not utilize a list loop (use range instead)

aList2 = []
for index in range(len(scoresList)):
    if scoresList[index] >= 90:
        aList2.append(scoresList[index])

print("Scores that are an A without using a list loop: " + str(aList2))