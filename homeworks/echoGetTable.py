#!/usr/bin/python
print 'Content-Type: text/html\n'
print ''

#Lorenz Vargas
#IntroCS2 pd09
#HW55 -- GET Started Simply
#2015-05-20

print '<html>'
print '<table style="width:30%">'

import os

XDDD = os.environ

for var in XDDD:
    print '<tr>'
    print '\t<td>'+str(var)+'</td>'
    print '\t<td>'+str(XDDD[var])+'</td>'
    print '</tr>'

print '</table>'
print '</html>'
