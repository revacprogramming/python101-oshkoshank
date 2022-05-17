"""Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below."""

l = None
s = None

while True:
    n =input("Enter your numbers: ")
    if n == 'done':
       break
    try:
        n = int(n)
        if l is None or n > l:
            l = n
        if s is None or s > n:
              s = n

    except:
           print("Shut up and enter a proper number you idiot !!!!")
           
print("The largest number amount you entered is ",l)
print("The smallest number amount you entered is ",s)


