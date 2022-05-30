fhand = open("romeo.txt")
lst = list()
for line in fhand:
    line = line.rstrip().split()
    #line = line.split()
    for i in line:
        if i not in lst:
            lst.append(i)

lst.sort()
print(lst)

"""Open the file romeo.txt and read it line by line. For each line, split the line` into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order."""