#!/usr/bin/python
print 'Content-Type: text/html\n'
print ''

#Lorenz Vargas
#IntroCS2 pd09
#HW
#2015-5-21

import os

XDDD = os.environ

print '<html>'

if 'QUERY_STRING' in XDDD:
    print 'Given a right triangle with sides 3, 4, and 5'
    queryString = XDDD['QUERY_STRING']
    tempQ = queryString.split('&')

    for x in range(len(tempQ)):
        tempQ[x] = tempQ[x].split(tempQ[x][1]) #split by second char

    d = {}

    for n in tempQ:
        d[n[0]] = float(int(n[1])) #store letter and number in dictionary

    print 'Perimeter: ' + str(d['a']+d['b']+d['c']) #perimeter
    print 'Area: ' + str(0.5*d['a']*d['b']) #area

else:
    print 'QUERY_STRING not found'

print '</html>'
