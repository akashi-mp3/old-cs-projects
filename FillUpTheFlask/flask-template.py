#Lorenz Vargas
#Attempt at flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def wut():
    return "Wut ahm ai dewing?"

@app.route('/wat')
def wat():
    return "Wat uhm ay duing?"

@app.route('/wot')
def wot():
    return "Wot ohm ey dawing?"

if __name__ == '__main__':
    app.run()
