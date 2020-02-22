#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

# Use words.txt as the file name

#i used the fname as variable for handling the filename
fname = input("Enter file name: ")

#i used fh as the handler for the file
fh = open(fname)

#i used the definite loop
for line in fh:
    
    #print the itteration variable converted to upper and rstrip
    print(line.upper().rstrip())
