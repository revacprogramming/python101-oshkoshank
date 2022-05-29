"""Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

file = open("mbox-short.txt",'r')
mail = {}
for l in file:
    if l.startswith("From:"): 
        m = l.split(" ")[1]
        m = m.rstrip()
        mail[m] =( mail.get(m,0)+1)
count = 0
for i in mail:
    if(mail[i] > count):
        count = mail[i]
        email = i
print(email,count)