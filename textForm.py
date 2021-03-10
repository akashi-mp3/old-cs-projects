#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
formData = cgi.FieldStorage()
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    for k in formData.keys():
        d[k] = formData[k].value
    return d
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><head><title> Codify Form </title></head></html>\n"
htmlStr += "<body>"

# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<h3>Check it out!</h3>"
htmlStr += "<h4>Dictionary of form data:</h4>"
htmlStr += str( FStoD() )
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

htmlStr += "</body></html>"


print htmlStr
