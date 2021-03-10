#!/usr/bin/python
print 'Content-Type: text/html\n'
print ''

#Lorenz Vargas
#IntroCS2 pd09
#HW55 -- GET Started Simply
#2015-05-20

print '<html>'

import os

XDDD = os.environ

if 'QUERY_STRING' in XDDD:
    for var in XDDD:
        if var == 'QUERY_STRING':
            if XDDD[var] != '':
                print XDDD[var]
            else:
                print 'no query string given'
else:
    print 'key QUERY_STRING not found'
        

print '</html>'




