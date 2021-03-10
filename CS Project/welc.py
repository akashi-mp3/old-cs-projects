#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi, cgitb
cgitb.enable()

#================================Preliminary Definitions============================
top = "<!DOCTYPE HTML>\n<html><head><title>Welcome!</title></head><body>"
bottom = "</body></html>"
corrs = "<a href=\"twitter_form.html\">I'd like to find correlations concerning Twitter data and word usage!</a>"
settings = "<a href=\"settings.html\">I'd like to change my settings.</a>"
prof = "<a href=\"prof.html\">I'd like to view my profile.</a>"
links = "<br>" + corrs + "<br>" + settings + "<br>" + prof
style = """<style>
		head, body {
			background: #58ACFA;
			   }
		a:link, a:visited, a:hover, a:active {
			color: black;
			}
	</style>"""

#=================================Functions==============================
def FStoD(): #cgi to dict
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d
    
def acknowledge():
    inputs = FStoD()
    user = inputs['account']
    retStr = top + style
    retStr += "<b>Welcome, <i>" + user + "</i>. What would you like to do today?</b><br>"
    retStr += links + bottom
    return retStr
    
print acknowledge()
