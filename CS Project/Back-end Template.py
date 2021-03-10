#!/usr/bin/python
print ''
print 'Content-Type: text/html'
#-------------essentials!--------------------------

#------------- Opening Bookends -------------------
import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved
print '<html>'
print '<head><title> INSERT TITLE HERE </title></head>'
print '<body>'

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
# STUFF GOES HERE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#================ HTML-generating code ============
# STUFF GOES HERE
#==================================================

#------------- Closing Bookends -------------------
print '</body>'
print '</html>'


