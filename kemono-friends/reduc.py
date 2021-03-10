f = open('warandpeace.txt', 'r')
l = f.read().split()
f.close()

#filter creates list of ele for which a func returns TRUE.

def freq(word, l):
    return len(filter(lambda w: w==word, l))

def g_freq(words, l):
    return len(filter(lambda w: w in words, l))

print "freq('Andrew', l):", freq('Andrew', l)
print "freq('war', l):", freq('war', l)

group = ['war','and','peace']
print "g_freq(['war','and','peace'], l):", g_freq(group, l)


def all_freq(res, ele):
        if ele.lower() not in res:
                res[ele.lower()] = 1
        else:
                res[ele.lower()] += 1

        return res

def most_freq():
        freq_dict = reduce(all_freq, l, {})
        max_freq = 0
        keys = freq_dict.keys()
        for i in range(len(keys)):
                if freq_dict[keys[i]] > max_freq:
                        best_girl = keys[i]
                        max_freq = freq_dict[keys[i]]
        return (best_girl, max_freq)

rem = most_freq()
print "War and Peace's Most Frequent Word: '" + rem[0] + "' (" + str(rem[1]) + ")"

