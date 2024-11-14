def getNegativeNumber():
    while (True):
        num = int(input("Enter a negative number: "))
        if num < 0:
            return num
        else:
            print("Not a negative number.")
   
print(getNegativeNumber())