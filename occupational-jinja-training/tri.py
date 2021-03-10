#Big L is the coolest cat in the village

from flask import Flask, render_template
app = Flask(__name__) #create Flask objec

import random

inStream = open('occupations.csv','r')
occupation = inStream.readlines()
inStream.close()

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    return "Big L is the coolest cat in the village. Be like him."

occupations = {}

#helper functions
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def store(string):
    for data in occupation:
        stripped = data.rstrip() #stripped data of /n
        temp = stripped.split(',')
        if is_number(temp[1]):
            occupations[temp[0]] = float(temp[1])

store(occupations) #create dictionary
occupations.pop('Total', None)
occupations.pop('Job Class', None)

def randomize():
    return random.choice(occupations.keys())

#end helper functions


@app.route("/occupations")
def occupy():
    return render_template('model.html', collection = occupations, job = randomize())
    
if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
