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
else:
    pageID = 'Welcome'
    description ='Hello web'

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - html</title>
  <meta charset="utf-8">
</head>
<body>

  <ol>
    {listStr}
  </ol>
  <form action="process_create.py" method="post">
      <input type="hidden" name="pageID" value="{form_default_title}">
      <p><input type="text" name="title_n" placeholder="title" value="{form_default_title}"></p>
      <p><textarea rows="4" name="description_n" placeholder="description">{form_defalut_description}</textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageID, desc=description, listStr=listStr, form_default_title=pageID, form_defalut_description=description))
