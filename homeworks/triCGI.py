#!/usr/bin/python
print 'Content-Type: text/html\n'
print ''

#The Lone Wolf - Lorenz Vargas<br>
#IntroCS2 pd09<br>
#HW57 -- Clever Genii, Inc.<br>
#5-22-2015<br><br>

import cgi
#import cgitb
import math

#cgitb.enable()

numbers = []

XDDD = cgi.FieldStorage()
for k in XDDD.keys():
    numbers.append(float(XDDD[k].value))

print 'Given triangle with sides'
print  numbers

print '<br>'

def perimeter(): #quick p finder
    perimeter = 0
    for number in numbers:
       perimeter += number
    return perimeter

p = perimeter()
print 'Perimeter: ' + str(p)

halfP = p/2
def area():
    operation = halfP*(halfP-numbers[0])*(halfP-numbers[1])*(halfP-numbers[2])
    area = math.sqrt(operation) #Heron's formula
    return area

print '<br>'

a = area()
print 'Area: ' + str(a)

print '</html>'

