fhand = open("romeo.txt")

lst = list()

for line in fhand:
    line = line.rstrip()
    line = line.split()
    for i in line:
        if i not in lst:
            lst.append(i)

lst.sort()
    
print(lst)
