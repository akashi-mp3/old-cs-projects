#Tears for Fears -- Lorenz Vargas, Chris Zhao
#IntroCS2 pd09
#HW48 -- Text Analysis, Webified
#2015-05-07


'''
The Algorithm/Plan:
1. Set var inStream to open(WarAndPeace.txt, 'r')
2. Stringify inStream and set it to local var novel
Working on novel:
3. Init an empty bucket dictionary, d
4. Replace all occurences of \n and -- (-- is unique to our copy)
5. Split novel by spaces, and store new list in var wordList
6. Use a for loop, for every word in wordList
7. Strip the word of punctuation
8. For each item, ask if it has a bucket in d.
    a. If no, create a bucket with value
    b. If yes, add 1 to value in the bucket
9. Close inStream

The Special Cases:
Punctuation - If the word has a punctuation in it, the code will strip the word of punctuation to get rid of it.
Capitalization - Every word in the story will have the .lower() method applied to it.
Apostrophes -
Words with Hyphens - Our code should already handle this.

The Log:
5/7/2015
*Converted War and Peace text into string
*Created wordCounter with largely functional punctuation removal (improve this later on)
*Has a dictionary with word frequencies
*Capitalization fixed

We decided to work on these couple steps first so that, at the very least, we end up with a dictionary that has word frequencies even if it is still very unrefined.
Punctuation was the first special case to be addressed because it was the easiest and most convenient to implement.

The Future:
*Improve punctuation removal
*Deal with capitalization
'''

inStream = open('lit.txt', 'r')

novel = inStream.read()
inStream.close()

def wordCounter(novel):
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
print wordCounter(novel)


    



