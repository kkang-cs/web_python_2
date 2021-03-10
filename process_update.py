#!Python

import cgi, os
form = cgi.FieldStorage()
pageID = form["pageID"].value
title = form["title_n"].value
description=form['description_n'].value

opened_file =open('data/'+pageID,'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageID, 'data/'+title)

#Redirection
print("Location: index.py?id="+title)
print()
