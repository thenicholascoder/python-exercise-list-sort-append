#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

#prompts for a filename
fname = input("Enter file name: ")

#then opens that file 
fh = open(fname)

#variable for every line starts with X-DSPAM-Confidence:
count = 0

#variable for total
total = 0

#and reads through the file
for line in fh:
    
    #if the line has no XDSPAM.. it will return to top of loop
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
        
    #sequential line, these will run if it has XDSPAM..
    #add count for every line that has XDSPAM
    count = count + 1
    
    #get the number of the line that starts from [20] above
    #then store it inside num
    num = float(line[20:])
    
    #get the total of the values
    total = total + num
    
#get the average as said in instruction
ave = total / count
print("Average spam confidence: "+ str(ave))
