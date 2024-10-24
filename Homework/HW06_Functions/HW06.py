
def hasFinalLetter(strList, letters): # defining the function
    hasList = [] # a list that will contain all values
    for string in strList: # for loop going through the strList
        if (string[-1] in letters): # checking if the last letter is in letters
            hasList.append(string) # appends to hasList if true
    return hasList # return the list

list1 = ["String", "Cheese", "Beans"] # creating variables for 3 different tests
letters1 = "owiWIgoes"

list2 = ["Ben", "Jen", "Sven"]
letters2 = "dfsfirISIDd"

list3 = ["Pencil", "Pen", "Marker"]
letters3 = "ofkKSDJifRrisdl"

print(hasFinalLetter(list1, letters1)) # returns list of 3 strings
print(hasFinalLetter(list2, letters2)) # returns list of 0 strings
print(hasFinalLetter(list3, letters3)) # returns list of 2 strings

def isDivisible(maxInt, twoInts): # declaring the function
    integerList = [] # list of integers 
    for number in range(1, maxInt): # checking numbers 1 - maxInt
        if (number % twoInts[0] == 0) and (number % twoInts[1] == 0): # checking if the number is divisible by item 1 and 2 of the tuple
            integerList.append(number) # appending the number if it is true
    return integerList # return the list of integers

max1 = 100 # declaring some test variables
max2 = 600
max3 = 14

tuple1 = (4, 8)
tuple2 = (8, 3)
tuple3 = (2, 7)

print(isDivisible(max1, tuple1)) # returns a list of 12 ints
print(isDivisible(max2, tuple2)) # returns a list of 24 ints
print(isDivisible(max3, tuple3)) # returns a list of 0 ints
