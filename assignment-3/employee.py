import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.Connect(host='localhost', user="root",\
                                      password="F@h33m@14", database='db1',charset="utf8")
        print('Database Connected')
    except:
        print('Database Connection Failed') 
    return connection
connect_db()
 