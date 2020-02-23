fname = input("Enter file name: ")
fh = open(fname)
lst = list()
bag = ""
#for each line in fh handler
for line in fh:

    #remove spaces, since split, result is in a list
    storage = line.rstrip().split()
    
    #for each words in storage
    for words in storage:
        
        #if words is not yet inside lst
        if words not in lst:
            
            #append the new word
            lst.append(words)
            
#sort the list then print
lst.sort()
print(lst)