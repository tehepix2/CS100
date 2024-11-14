# initialize a file object
my_file = open("myfile.txt", 'w') # opens a file in the current directory if the absolute path is not specified
                                  # mode 'r' means it is in read mode, it can only be read

# close the file
my_file.close()

'''
File Modes
'r' -> reading (default if second parameter is not specified) does not work if file does not exist
'w' Writing (if file exists, content is wiped) file does not have to exist
'a' Append (if file exists, writes are appended [at the end of the line])
'r+' Reading and Writing
't' text (default)
'b' binary
'''