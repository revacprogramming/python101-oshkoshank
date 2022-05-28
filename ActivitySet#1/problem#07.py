file = input("Enter the file name: ")
fh = open(file,'r')
count = 0
total = 0
for l in fh:
    if(l.startswith("X-DSPAM-Confidence:")):
        s_i = l.find(" ")
        num = float(l[s_i+1:])
        total += num
        count += 1
print("The average value is",(total/count))