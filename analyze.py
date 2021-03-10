#!/usr/bin/python
print 'Content-Type: text/html\n'
print ''

'''
DEV LOG
05-15:
Lorenz/Kathy - plan formulated, datasets chosen
05-16:
Kathy - worked on preprocessing and list-based approach to problem, tables merged, nearly complete
05-17:
Kathy/Lorenz - switched to dictionary based approach and chose data within set
to analyze
Kathy - basic graphs completed
Lorenz - worked on analysis and a few formatting issues
'''

analysis = '''
<html>
<h1>Correlation between SAT Scores and AP Tests Passed and DOE Grades</h1>
<i>by Guns and Roses -- Kathy Lau and Lorenz Vargas <br>
IntroCS2 pd09 <br>
HW53 -- Present Your Findings <br>
2015-05-17
</i>
<p>
<br><br>
By looking at the schools in New York City with the highest SAT scores and comparing how many AP tests are passed in these schools, a positive correlation can be found.
<br>
Generally speaking, the schools with the highest SAT scores pass the most AP exams. This can be explained by the academic rigor of the highest scoring schools as these
<br>
schools generally offer more AP courses. Another factor to consider is student population. Inevitably, a school with a higher population will take more AP tests assuming
<br>
that AP courses are offered at that school. As one reaches the middle and lower range of SAT scores, the number of AP tests passed fluctuates because of these key differences
<br>
within each school. Accounting for these differences in addition to comparing how many AP tests each of these schools take overall would provide a clearer picture of the relationship.
<br>
Finally, the table on the bottom shows that schools with a higher DOE grade have a slightly higher SAT grade than the schools with grades below it.
<br><br>
The data upon which this report is based on is freely available online at the following links.
<br>
<a href="http://schools.nyc.gov/Accountability/data/TestResults/default.htm">Here for the SAT data</a>
<br>
<a href="https://data.cityofnewyork.us/Education/AP-Results/9ct9-prf9">Here for the AP data</a>
<br>
<a href="https://data.cityofnewyork.us/Education/School-Progress-Reports-All-Schools-2009-10/ffnc-f3aa">Here for the DoE letter grade data</a>
<br> <br>
They are also available locally in CSV format.
<br>
<a href="data01.csv">SAT Data</a>
<br>
<a href="data02.csv">AP Data</a>
<br>
<a href="data03.csv">DoE Letter Grade Data</a>
</p>
'''
# imports CSV file; returns it as a list of strings
def importCSV(CSVfile):
    f = open(CSVfile, 'r') 
    satL = f.readlines() 
    f.close()
    return satL

# FIX COMMAS
def preprocess(L):
    newL = []
    for s in L:
        s = s.strip('\n').split(',')
        while s[2][0] == ' ': # commas in school names
            s[1] = s[1] + ',' + s[2] # combine part1 + , + part2
            del s[2]
            s[1] = s[1].strip('"')
        while s[2][0]=='"': #take out commas in numbers
            s[2]=s[2].strip('"')
            s[3]=s[3].strip('"')
            s[2]=s[2]+s[3]
            del s[3]
        newL += [s]
    return newL
 

# processed data thus far
satInfo = preprocess(importCSV('data01.csv'))
apInfo=preprocess(importCSV('data02.csv'))
progInfo=preprocess(importCSV('data03.csv'))

def SATdictionary(filename):
    retDict = {}
    for i in filename[1:]: #skip table header
        if "s" not in i:
                el = (int(i[3]) + int(i[4]) + int(i[5])) #add the writing,reading and math parts
                retDict[str(i[1])] =el #school id : score
    return retDict

satD=SATdictionary(satInfo) #dictionary of school code : SAT score

def APpdictionary(filename):
    retDict = {}
    for i in filename[1:]:
        if "s" not in i:
            el = int(i[4]) # num of APs passed column
            retDict[str(i[1])] = el #school id: aps passed
    return retDict

appD=APpdictionary(apInfo) #dictionary of school code : APs passed

def APtdictionary(filename):
    retD={}
    for i in filename[1:]:
        el=i[3]
        retDict[str(i[1])]=el
    return retDict

def GRdictionary(filename):
    retDict={}
    for i in filename[1:]:
        el=i[7]
        i[2]=i[2].upper()
        retDict[str(i[2])]=el
    return retDict

grD=GRdictionary(progInfo)
#Matches the school codes from both return dictionaries
def freq():
    d1 = satD
    d2 = appD
    retDict = {}
    for i in d1:
        try:
            a = d1[i]
            b = d2[i]
            retDict[a] = b#match element in one to element in 2, and add them as corresponding terms in the retDict
        except:
            pass#if something went wrong ("N/A", no match) skip it
    return retDict

d3=freq()

def simpleTable():
    retStr='<table ><th>School</th><th>SAT SCORE</th><th>APS PASSED</th><th>GRADE</th>'
    for i in sorted(d3, reverse=True):
        retStr+='<tr>'
        for j in satD:
            if i == satD[j]:
                retStr+="<td>" + j + "</td>"
                break
        retStr+='<td>' + str(i) + '</td>'
        retStr+='<td>' + str(d3[i]) + '</td>'
        if j in grD:
            retStr+='<td>'+str(grD[j])+'</td>'
        else:
            retStr+='<td>'+'s'+'</td>'
        retStr+='</tr>'
    retStr+= '</table></html>'
    return retStr

def topgraph(d,n):
        val=d.values()
        s=''
        for i in range(n):
            m=max(val)
            for i in d:
                if d[i]==m:
                    s+= i[:18] + str('='*(m/100))+str(len(str('='*(m/100))))+'<br>\n' 
                    val.remove(m)
        return s

def lowgraph(d,n):
        val=d.values()
        s=''
        for i in range(n):
            m=min(val)
            for i in d:
                if d[i]==m:
                    s+= i[:18] + str('='*(m/100))+str(len(str('='*(m/100))))+'<br>\n' 
                    val.remove(m)
        return s

            
topSAT='<b>TOP 10 SAT SCHOOLS:<br></b>' + topgraph(satD,10)
topAP='<b>TOP 10 APs PASSED:<br></b>' + topgraph(appD,10)
lowSAT='<b>BOTTOM 10 SAT SCHOOLS:<br></b>' + lowgraph(satD,10)
lowAP='<b>BOTTOM 10 APs PASSED:<br></b>' + lowgraph(appD,1)
info="<h3>HORIZONTAL BAR GRAPHS-- EACH = REPRESENTS A 100</h3><br>"
style='''<html>
<style>
p > a{
text-decoration: none;
color: #0091EB;
}
p > a:hover{
text-decoration:underline;
}

table{
    font-family: Consolas, monaco, monospace;

}
td{ 
   border: 1px solid black;
}
th{
    text-align: left;
    background: #1BF;
    border-top-right-radius:25px;
    border-top-left-radius:25px;
    border: 0px;
    padding: 15px;
}
tbody tr:nth-child(odd){
    background: #BEF;
}
tbody tr:hover{
    background: #3EEF93;

}


</style>'''



def mean(L):
    sumAll=0
    for i in L: sumAll+=i
    return sumAll/float(len(L))


def scoresAnalysis(): #returns a list of sat scores sorted by grade. 
    a=[]
    b=[]
    c=[]
    d=[]
    f=[]
    for i in satInfo:
        for j in progInfo:
            if i[0]==j[0]: 
                grade=j[7]
                try:
                    score=int(i[3])+int(i[4])+int(i[5])
                except:
                    progInfo.remove(j)
                    break
                if grade=='A':
                    a.append(score)
                if grade=='B':
                    b.append(score)
                if grade=='C':
                    c.append(score)
                if grade=='D':
                    d.append(score)
                if grade=='F':
                    f.append(score)
                progInfo.remove(j) 
                break 
    return [a,b,c,d,f]

def AnalysisTable(d1,d2):
    scores=scoresAnalysis()
    table="<table><th>Grade</th><th>Mean SAT Score</th><th># Of Schools</th>"
    listt=[['A',mean(scores[0]),len(scores[0])],
           ['B',mean(scores[1]),len(scores[1])],
           ['C',mean(scores[2]),len(scores[2])],
           ['D',mean(scores[3]),len(scores[3])],
           ['F',mean(scores[4]),len(scores[4])]]
    for row in listt:
        table+='<tr>'
        for a in row:
            table+='<td>'+str(a)+'</td>'
        table+='</tr>'
    table+= '</table>'
    return table

doe= AnalysisTable('data01.csv','data03.csv')

def export(CSVfile, HTMLfile):
    apInfo=preprocess(importCSV('data02.csv'))
    m = simpleTable()
    stats=style
    words='<br><h2>DOE GRADES ANALYSIS</h2>'
    more='<br><br> <b>*For the following table, s denotes no data</b><h2>SAT/APs/GRADES TABLE</h2>'
    stats+=analysis +info+'<font color="#1938FD">'+topSAT+'<br><br>'+topAP+'<br><br>'+lowSAT+\
    '<br><br>'+lowAP+'</font>'+words+doe+more+ m
    stats+='</html>'
    outStream = open('analysis.html','w')
    outStream.write(stats) 
    outStream.close()

export('data02.csv', 'analysis.html')
