#!/usr/bin/python
print "Content-type: text/html"
print ""

import random

print '''
<html>
<pre>
'''

hair = ['|', 'w', 't', '.', '#']
eyes = ['O','0','?','!', '*','~', '-', '@']
nose = ['l', 'T', 't', 'Y']
mouth = ['O','Q', 'w', '*', '-']

def face():
    print hair[random.randrange(len(hair))]*5
    print eyes[random.randrange(len(eyes))]*2
    print nose[random.randrange(len(nose))]
    print mouth[random.randrange(len(mouth))]

face()

print '''
</pre>
</html>
'''
