# initialize a file object
my_file = open("myfile.txt", 'w') # opens a file in the current directory if the absolute path is not specified
                                  # mode 'r' means it is in read mode, it can only be read

# close the file
my_file.close()

my_file = open("myfile.txt", 'w') # reopen the file

my_file.write("Bingus\nYour Mother") # writes the word, "bingus" and "Your mother" to the text file

my_file.close() # close it to change the mode

my_file = open("myfile.txt", 'r') # open the file on read mode

for line in my_file: # check every line in the file (when using a for loop in a file, it goes through every line and not every character)
    print(line, end=" ")
'''
File Modes
'r' -> reading (default if second parameter is not specified) does not work if file does not exist
'w' Writing (if file exists, content is wiped) file does not have to exist
'a' Append (if file exists, writes are appended [at the end of the line])
'r+' Reading and Writing
't' text (default)
'b' binary
'''