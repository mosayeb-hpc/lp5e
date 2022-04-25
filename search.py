import os
import sys

book = input('enter book name: ')
directory = input('enter dir path: ')

F = open('list.txt', 'w')

for (i, j, k) in os.walk(directory):
    for b in k:
        if book in b.lower():
            print(i, '\n', '-' * 100, file=F)
            print(b, file= F)

F.close()
        

