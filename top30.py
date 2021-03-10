#!/usr/bin/python
print ""
print "Content-Type: text/html\n"
print ""

print '<!DOCTYPE html> <html>'

def wordTally():
    inStream = open('lit.txt', 'r')
    novel = inStream.read()
    inStream.close()
    d = {}
    novel = novel.replace('\n',' ') #removes all \n line breaks
    novel = novel.replace('--',' ') #removes all -- (special case)
    novel = novel.lower()
    wordList = novel.split(' ') #splits into indiv words
    for word in wordList:
        word = word.strip('''.!?,;:-()[]{}'"''')
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

print '''
<h1>Thirty Most Frequent Words in War and Peace by Leo Tolstoy</h1>
'''

def getTop30()
{
    max30Dict = {}
    maxFreq = 0
    minFreq = 1000000
    for k, v in in d.items():
        if len(max30Dict) < 30:
            max30Dict[k] = v
            if v > maxFreq:
                maxFreq = v
            if v < minFreq:
                minFreq = v
        else:
            if v > maxFreq:
                # get the min freq and substitue with maxFreq k, v
                del d(minFreq)
                max30Dict[k] = v


}


def top30():
    d = wordTally()
    HTMLtable="<table border='1'<tr><td><b>Word</b></td>" + \
               "<td><b>Number of Apperances</b></td></tr>"
    x = 0 #All placeholder values for readability sake
    valList=d.values()       
    while x < 30: #while we have less than 30 max
        for key in d:
            if d[key] == max(valList):
                HTMLtable += "<tr><td>"+ str(key) +"</td><td>"+ str(max(valList)) +"</td></tr>"
                d.remove(key)
                valList.remove(max(valList))
                print max(valList)
                print HTMLtable
                x += 1
    print HTMLtable + "</table>" + "</html>"

top30()
