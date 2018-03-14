import pymysql
from matplotlib.pyplot import title

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='wiki-page',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
connectionlink = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='wiki-links',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
cursorlink = connectionlink.cursor()

def title_to_id(title):
    query = "SELECT page_id FROM page WHERE page_title = '" + title + "'"
    cursor.execute(query)

    if cursor.rowcount == 0:
        return
    else:
        id_title = cursor.fetchmany()
    return id_title

def linking(pfrom):
    list_id = []
    query = "SELECT pl_title FROM pagelinks WHERE pl_from = " + pfrom
    cursorlink.execute(query)

    if cursorlink.rowcount == 0:
        return
    else:
        listlinks = cursorlink.fetchmany(size=50)

    list_title = [link['pl_title'].decode('utf-8') for link in listlinks]

    list_ids = [title_to_id(title) for title in list_title]

    for link in list_ids:
        if link != None:
            list_id.append(link[0]['page_id'])

    return list_id

#test
list_ids = (linking('11'))
print list_ids