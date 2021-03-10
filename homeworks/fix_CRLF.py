## the MAGIC NEWLINE FIXER
##
## by
##  _____ _   _     ___ ___     
## |_   _| |_| |_ _|  _|  _|_ _ 
##   | | |   | | | |  _|  _| | |
##   |_| |_|_|_|___|_| |_| |_  |
##                         |___|
## 
## Remedies the Windows newline problem:
##   MS uses CRLF (carriage return + line feed)
##   POSIX systems use LF (line feed aka newline)
##   This script replaces all occurrences of former with latter.
##
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Usage:
## $ python fix_CRLF.py <fileToFix>    
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import sys  # system tools for file I/O

if len(sys.argv)>1:         # make sure file to fix provided
    fileName=sys.argv[1]    
    # store contents of file as string
    f=open(fileName)
    s=f.read()
    f.close()
    # reopen file for writing
    f=open(fileName,'w')
    # overwrite file, w/ CRLF -> LF
    f.write(s.replace('\r\n','\n'))
    f.close()
else:
    print "Error: No arguments given. (File to fix not specified.)"
    print "Proper syntax: 'python new_line_fixer.py fileToFix'"
