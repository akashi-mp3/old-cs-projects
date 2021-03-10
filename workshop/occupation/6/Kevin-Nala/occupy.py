import random

def get_file():
    f = open("occupations.csv", "r")
    L = f.readlines()[1:-1]
    for i in range(len(L)):
        L[i] = L[i].replace('\"', '')
        x = L[i].rfind(",")
        L[i] = [ L[i][:x], L[i][x+1:-1] ]
    return L

def get_occs( L ):
    M = []
    for x in L:
        M += [x[0]]
    return M

def get_pcts( L ):
    M = []
    for x in L:
        M += [float(x[1])]
    return M

def set_ranges( L ):
    M = [ L[0] ]
    L = L[1:]
    for i in range(len(L)):
        M += [ round( (M[i]+L[i]), 1 ) ]
    return M

def pull_rand_occ( r, L ):
    rand = random.random() * 99.8
    x = 0
    while x < len(r):
        if rand <= r[x] :
            break
        x += 1
    return L[x]

lines = get_file()

dict = { "Occupations" : get_occs( lines ),
         "Percentages" : get_pcts( lines ) }

ranges = set_ranges( dict["Percentages"] )

for i in range(15):
    print pull_rand_occ( ranges, dict["Occupations"] )
