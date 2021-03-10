#Brandon Huang and Big L
#Workshop 1

import random

inStream = open('occupations.csv','r')
occupation = inStream.readlines()
inStream.close()

dictionary = {}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def store(string):
    for data in occupation:
        stripped = data.rstrip() #stripped data of /n
        temp = stripped.split(',')
        if is_number(temp[1]):
            dictionary[temp[0]] = float(temp[1])

store(occupation)
#print dictionary

dictionary.pop('Total', None)

def weighted():
    rand = random.random() * 100
    currentPercent = 0.0
    for stuff in dictionary:
        if rand < currentPercent + dictionary[stuff]:
            return stuff
        else:
            currentPercent += dictionary[stuff]

print weighted()
