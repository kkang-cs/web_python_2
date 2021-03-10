#!Python

import cgi
form = cgi.FieldStorage()
title = form["title_n"].value
description=form['description_n'].value

opened_file =open('data/'+title,'w')
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()
