#!/usr/bin/python
print "Content-type: text/html"
print ""
#Team Cuban Raft Riders -- Lorenz Vargas and Julie Chan
#IntroCS2 pd09
#HW40 -- Put Your Plan Into Action...
#2015-04-24
'''
Mechanization for Madlibizator:
1. Create lists for nouns, adjectives, adverbs, and verbs with choice words in each list.
2. Create a different random word function for each list which chooses a random index and return the string with that index.
3. In the madlibification fxn, we assign variables noun, adj, adv, and verb with the random word generator in step 2.
4. Make a function that does splits words by spaces using string.split()
5. Make a fillBlanks which will identify a noun, adj, adv, or verb and replace it with a random word of the same type.
6. Add the variables to the madlib where so desired.

What's New in V2?
New lists for tenses of verbs (expanded placeholders)
New list for places (expanded placeholders)
'''

import random

#takes a string containing placeholders of the form <NOUN>, <VERB>, etc. and returns a string where all placeholders have been replaced with a random string from the appropriate list of strings.
#Uses global variables nouns, verbs, adjs, advs.

#Algo for fillBlanks
#1. Split the story using the spaces as the divisions. You get a list.
#2. Init an index counter
#3. While ind is less than len of list, see if any placeholders present
#4. If so, replace them with the random worder by accessing their indices.
#5. Once finished, join the list and ret as string.

nouns = ['model','Goomba','thuggee','cat','mug','bae','pickle','trophy','spelunker','mafioso','major-general','Hobbit','wizard','potato']
verbpres = ['sanctifies','desecrates','poops','devours','bamboozles','eschews','canoodles','defenestrates','vanquishes','synergizes']
verbpast = ['sanctified','desecrated','poopd','devoured','bamboozled','eschewd','canoodled','defenestrated','vanquishd','synergized']
verbfut =  ['sanctify','desecrate','poop','devour','bamboozle','eschew','canoodle','defenestrate','vanquish','synergize']
adjs = ['lackadaisical','fungible','cheeky','dingy','floozy','namby-pamby','loopy','slovenly','bellicose','rhadamanthine','spunky','supercalifragilisticexpialidocious']
advs = ['sluggishly','splendidly','amazingly','courageously','lackadaisically','unethically','awkwardly','frenetically','extraordinarily','supercalifragilisticexpialidociously']
place = ['Montreal', 'Colorado', 'Papua New Guinea', 'Narnia', 'The Wizarding World of Harry Potter', 'Romania']
placeholders = ['<ADJECTIVE>','<NOUN>','<VERBPr>','<VERBPa>','<ADVERB>', '<PLACE>', '<VERBFut>']

def randWord(L):
    chosenOne = L[(random.randrange(len(L)))]
    return chosenOne

def fillBlanks(sentence): #only deals with single sentences for now
    wordList = sentence.split(' ')
    ind = 0
    while ind < len(wordList):
        word = wordList[ind]
        if word in placeholders:
            if word == '<ADJECTIVE>':
                wordList[ind] = randWord(adjs)
            elif word == '<NOUN>':
                wordList[ind] = randWord(nouns)
            elif word == '<VERBPr>':
                wordList[ind] = randWord(verbpres)
            elif word == '<VERBPa>':
                wordList[ind] = randWord(verbpast)
            elif word == '<VERBFut>':
                wordList[ind] = randWord(verbfut)
            elif word == '<ADVERB>':
                wordList[ind] = randWord(advs)
            elif word == '<PLACE>':
                wordList[ind] = randWord(place)
        ind += 1
    return ' '.join(wordList) + '.'

print fillBlanks('The <ADJECTIVE> <NOUN> <ADVERB> <VERBPr> the <ADJECTIVE> <NOUN>')

def madlibify(story):
    sentlist = story.split('.')
    story = ' '
    for sent in sentlist:
        story += fillBlanks(sent)
    return story[:-1]

story = '''
<html>
<h1>A Story for the Ages</h1>
Once upon a time, there lived a <u> <NOUN> </u> in <u> <PLACE> </u> , a kingdom far far away.
</br>
Now, he wasn't particularly special but he sure was <u> <ADVERB> </u>.
</br>
He <u> <VERBPa> </u> through his days and <u> <VERBPr> </u> through his nights, a very <u> <ADJECTIVE> </u> life indeed.
</br>
But what he wanted more that anything in theworld was to be a <u> <NOUN> </u> , to <u> <VERBFut> </u> the forest and to <u> <VERBFut> </u> thepeople.
</html>
'''
print madlibify(story)

        
    


