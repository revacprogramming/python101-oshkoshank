fh = open('romeo.txt','r')
l = []
for line in fh:
    line = line.rstrip()
    line = line.split(' ')
    for word in line:
        if word not in l:
            l.append(word)
print(sorted(l))