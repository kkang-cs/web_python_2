#!Python
print("Content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
#print(files)
listStr=''
for item in files:
    listStr= listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)


form = cgi.FieldStorage()
if 'id' in form:
    pageID = form["id"].value
    description = open('data/'+pageID, 'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageID)
    delete_action='''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageID" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageID)
else:
    pageID = 'Welcome'
    description ='Hello web'
    update_link =''
    delete_action =''
print('''<!doctype html>
<html>
<head>
  <title> aaa </title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
    {delete_action}
  </ol>
  <a href="create.py">create</a>
  {update_link}
  <p style="margin-top:40px">
  <h3>{title}</h3>
  <br> {desc}
  </p>
</body>
</html>
'''.format(title=pageID, desc=description, listStr=listStr, update_link=update_link, delete_action=delete_action))
