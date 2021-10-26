import xml.etree.ElementTree as et 
import sqlite3

tree=et.ElementTree(file='d:\\Python\\menu.xml')
root = tree.getroot()
rootname = root.tag
connection=sqlite3.connect(root.tag + '.sqlite')
cursor= connection.cursor()
for child in root:
    table = '''CREATE TABLE %s (price TEXT, name TEXT);''' % child.tag
    cursor.execute(table)
    for gc in child:
        com = """INSERT INTO %s VALUES (\"%s\", \"%s\");""" % (child.tag, gc.attrib['price'], gc.text)
        cursor.execute(com)
    
    cursor.execute('SELECT * FROM %s' % child.tag)
    print(cursor.fetchall())
            
connection.commit()
cursor.close()
connection.close()


