#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi, cgitb, hashlib
cgitb.enable()

top = "<!DOCTYPE HTML>\n<html><head><title>Login</title></head><body>"
bottom = "</body></html>"
style = """<style>
		head, body {
			background: #58ACFA;
			   }
		a:link, a:visited, a:hover, a:active {
			color: black;
			}
	</style>"""
m = hashlib.md5()

def importCSV(filename):
    instream = open(filename,"r")
    lines = instream.readlines()
    instream.close()
    return lines
    
def FStoD(): #cgi to dict
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

def check():
    inputs = FStoD()
    users = importCSV("users.csv")
    uName = inputs['user']
    m.update(inputs['pass'])
    uPass = m.hexdigest()
    names = []
    passes = []
    retStr = top + style
    for account in users:
        account = account.split(",")
        for data in account:
            data = data.split(",")
        names += account[::3]
        passes += account[1::3]
    if uName in names:
        if uPass == passes[names.index(uName)].strip():
            retStr+= """<form method="POST" action= \"welc.py\">
                <input type="text" name="account" value=""" + uName + """ hidden>
                <input type="submit" name="Submit" value="Continue to site!">
            </form>"""
        else:
            retStr+= "Wrong password. Go back and try again."
    else:
        retStr+= "Username does not exist. Go back and try again."
    retStr+= bottom
    return retStr
print check()
