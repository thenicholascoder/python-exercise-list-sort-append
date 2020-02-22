fname = input("Enter file name: ")
fh = open(fname)
lst = list()
temporarylst = list()
for line in fh:
	temporarylst = line.rstrip().split()
for pieces in temporarylst:
	lst.append(pieces)
for piece in lst:
	lst.append(piece)
lst.sort()
prnt(lst)