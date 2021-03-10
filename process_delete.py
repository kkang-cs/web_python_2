#!Python

import cgi, os
form = cgi.FieldStorage()
pageID = form["pageID"].value

os.remove('data/'+pageID)

#Redirection
print("Location: index.py")
print()
