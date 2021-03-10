#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi, cgitb, hashlib
cgitb.enable()

top = "<!DOCTYPE HTML>\n<html><head><title>Login</title></head><body>"
style = """<style>
		head, body {
			background: #58ACFA;
			   }
		a:link, a:visited, a:hover, a:active {
			color: black;
			}
	</style>"""
bottom = "</body></html>"
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
    
def make(user, aPass):
    outStream = open('users.csv','a')
    m.update(aPass)
    aPass = m.hexdigest()
    data = user + "," + aPass + "\n"
    outStream.write(data)
    outStream.close()
    return "Account successfully created."

digits = "0123456789"

def passCheck(aPass):
    if "," in aPass:
        return False
    if len(aPass) < 8:
        return False
    if len(aPass) > 15:
        return False
    for char in aPass:
        if char in digits:
            return True
    return False

def check():
    inputs = FStoD()
    dName = inputs['dUser']
    p1 = inputs['pass1']
    p2 = inputs['pass2']
    users = importCSV('users.csv')
    names = []
    passes = []
    retStr = top+style
    for account in users:
        account = account.split(",")
        for data in account:
            data = data.split(",")
        names += account[::3]
        passes += account[1::3]
    if dName in names:
        retStr+= "This username isn't available. Try again."
    else:
        if passCheck(p1):
            retStr+= make(dName, p1)
        else:
            retStr+= "Password invalid. Must be 8-15 characters, with at least one number, and no commas."
    retStr += bottom
    return retStr

print check()
