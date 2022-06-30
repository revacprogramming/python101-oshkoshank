<<<<<<< HEAD
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print (href[position].contents[0])
    html = urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
=======
# Databases
# https://www.py4e.com/lessons/database
Def main()
>>>>>>> 0a1408adc11339b793153d649907af69b9cbd6ab
