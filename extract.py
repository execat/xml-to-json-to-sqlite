import json
import sqlite3

db = json.loads(open("plugins.nowhitespace.json").read())
items = db[u'channel'][u'item']

conn = sqlite3.connect('sqlite_file.db')
c = conn.cursor()

sql = 'create table plugins (title text, desc text, date text, categories text, author text, link text, enclosure_text text, enclosure_bytes int)'

c.execute(sql)

for item in items:
    title = item[u'title']
    desc = item[u'description']
    date = item[u'pubDate']
    cat = ""
    for f in item[u'category']:
        if isinstance(f, dict):
            cat = cat + ", " + f[u'#text']
    cat = cat[2:]
    creator = item[u'creator']
    link = item[u'link']

    if u'enclosure' in item.keys():
        enclosure_bytes = item[u'enclosure'][u'@length']
        enclosure_text = item[u'enclosure'][u'@url']

    params = (title, desc, date, cat, creator, link, enclosure_text, enclosure_bytes)

    #print query
    #c.execute(query)

    c.execute("insert into plugins values (?, ?, ?, ?, ?, ?, ?, ?)", params)

conn.commit()
conn.close()
